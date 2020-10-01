from bs4 import BeautifulSoup
import csv
import datetime
import getopt
import os
import pandas as pd
import requests 
import smtplib, ssl
import sys


MODULEROOT = os.path.dirname(os.path.realpath(__file__))
SCHEDULECONFIGFILE = MODULEROOT+"\\UpdateSoccerScheduleConfig.xlsx"
TEXTMESSAGE = """\
Subject: [EVENT UPDATE] {0}


NEW: {1} {2}
     @{3}

OLD: {4} {5}
     @{6}
"""

WELCOMEMESSAGE = """\
Subject: [WELCOME] {0}


You will automatically receive 
a text message notice when an 
event change happens for:
{1}

-BensonBot
"""



def LoadConfig(): # Returns a DataFrame.  If empty, can be tested with DataFrame.empty
    global SCHEDULECONFIGFILE
    dfConfig = pd.read_excel(SCHEDULECONFIGFILE)
    dfConfig.set_index("ScheduleNickname", inplace=True)
    return dfConfig


def LoadWebSchedule( url , teamname):  #load the webschedule only for our teamname
    GAMEDAYHEADER = ['Game', 'Venue', 'Time', 'Field', 'Group', 'Home Team', 'Score', '', 'Away Team', 'Score']
    DFSCHEDULEHEADER = GAMEDAYHEADER.copy()
    DFSCHEDULEHEADER.insert(0,'Date')

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    # Find all game dates by looking for 'center' html element  (this may change)
    GameDateList = soup.find_all('center')
    # Find all game day schedule tables by counting tables where the first row matches GAMEDAYHEADER
    GameTableCount = 0
    TableList = soup.find_all('table')
    for currenttable in TableList:
        data = [[' '.join(item.text.split()) for item in tcel.select("td")] for tcel in currenttable.select("tr")]
        if data[0] == GAMEDAYHEADER:
            GameTableCount=GameTableCount+1

    #Proceed if the amount of dates match the amount of Tables
    if GameTableCount == len(GameDateList):
        iCurrentGame=0
        ScheduleList = []
        for trow in soup.select("table"):
            data = [[' '.join(item.text.split()) for item in tcel.select("td")] for tcel in trow.select("tr")]
            if data[0] == GAMEDAYHEADER:
                for i in range(1, len(data)):
                    currentdata = data[i].copy()
                    currentdata.insert(0, GameDateList[iCurrentGame].text.replace('Bracket\xa0-\xa0',''))
                    ScheduleList.append( currentdata )
                iCurrentGame=iCurrentGame+1

        dfSchedule = pd.DataFrame(data=ScheduleList, columns=DFSCHEDULEHEADER, dtype=str)
        # "Game" is a unique game code used in the schedule.  set it as the index
        dfSchedule.set_index("Game",inplace=True)


        dfSchedule = dfSchedule[ (dfSchedule["Home Team"]==teamname) | (dfSchedule["Away Team"]==teamname) ]
        return dfSchedule
    else:
        return pd.DataFrame

def print_usage():
    """
    Help printout for current Script
    """

    print("")
    print("UpdateSoccerSchedule <OPTIONS> <ARG>")
    print("")
    print("<ARG> - Optional argument is the ScheduleNickname in the UpdateSoccerScheduleConfig.xlsx file")
    print("")
    print("  {: <15} {: >10}".format(*['-h, -?, --help','Displays this help output']))
    print("  {: <15} {: >10}".format(*['--testmail','Sends a test MMS message to env user']))
    print("  {: <15} {: >10}".format(*['--sendwelcome','Sends welcome MMS message to all users in ScheduleNickname']))


######################################################################################################################################################################
#
# Main()
#
######################################################################################################################################################################
    

def Main(argv):
    global TEXTMESSAGE
    global SCHEDULECONFIGFILE

    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                    '?h',                # each character represents a sort option -?, -H
                                    ['help',
                                    'testmail',
                                    'sendwelcome']      # each list entry represents a long option --help, etc.
                                    )
    except getopt.GetoptError as err:
        print (str(err))
        print_usage()
        sys.exit(2)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        print_usage()
        sys.exit(2)

    port = 465  # For SSL
    password = os.environ.get("GMAILBOTPASS")
    sender_email = os.environ.get("GMAILBOT")
    ScheduleParam = None
    
    # Create a secure SSL context
    context = ssl.create_default_context()
    server =  smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
    server.login(sender_email, password)

    for opt, val in opts:
        if opt == '--testmail':
            receiver_email = os.environ.get("GMAILBOT_TO")
            TEXTMESSAGE = TEXTMESSAGE.format("Girls 14U Division 1 TEST","2:00 PM", "September 18, 2020", "Legacy Events Center", "2:00 PM", "September 18, 2020",  "Legacy Events Center",)
            print("[Log] Sending TEST MMS to: {}".format(receiver_email))
            server.sendmail(sender_email, receiver_email, TEXTMESSAGE)
            print("[Log] Script complete.")
            sys.exit(0)

        if opt == '--sendwelcome':
            if len(args) != 1:
                print("[Error] Argument missing: ScheduleNickname") 
                sys.exit(1)
            else:
                ScheduleParam = args[0]

            print("[Log] Loading soccer schedule configeration file: {}".format(SCHEDULECONFIGFILE))
            if not os.path.isfile(SCHEDULECONFIGFILE):
                print("[Error] Cannot find soccer schedule configeration file: {}".format(SCHEDULECONFIGFILE))
                sys.exit(1)

            dfConfig = LoadConfig()
            # Load only row with pertinent ScheduleNickname specified by ScheduleParam
            dfScheduleConfig = dfConfig[ dfConfig.index == ScheduleParam]
            if dfScheduleConfig.empty:
                print("[ERROR] Schedule Nickname not found to update")
                sys.exit(1)

            WelcomeList = dfScheduleConfig.loc[ScheduleParam,"MailingList"].split(';')

            for currentRecipient in WelcomeList:
                print("[Log] Sending welcome message to: {}".format(currentRecipient))
                welcomemessageMMS = WELCOMEMESSAGE.format(dfScheduleConfig.loc[ScheduleParam,"ScheduleName"] ,dfScheduleConfig.loc[ScheduleParam,"TeamName"] )
                server.sendmail(sender_email, currentRecipient,welcomemessageMMS )

            print("[Log] Script Complete")
            sys.exit(0)

    if len(args) != 1:
        print("[Error] Argument missing: ScheduleNickname") 
        sys.exit(1)
    else:
        ScheduleParam = args[0]

    ###############################################################################################################################
    # Load Configuration File
    print("[Log] Loading soccer schedule configeration file: {}".format(SCHEDULECONFIGFILE))
    if not os.path.isfile(SCHEDULECONFIGFILE):
        print("[Error] Cannot find soccer schedule configeration file: {}".format(SCHEDULECONFIGFILE))
        sys.exit(1)

    dfConfig = LoadConfig()
    # Load only row with pertinent ScheduleNickname specified by ScheduleParam
    dfScheduleConfig = dfConfig[ dfConfig.index == ScheduleParam]
    if dfScheduleConfig.empty:
        print("[ERROR] Schedule Nickname not found to update")
        sys.exit(1)

    MailingList = dfScheduleConfig.loc[ScheduleParam,"MailingList"].split(';')
    
    ###############################################################################################################################
    # Get the current schedule for ScheduleParam
    CurrentSoccerScheduleFile = "./{}.csv".format(ScheduleParam)
    print("[Log] Loading current schedule: {}".format(CurrentSoccerScheduleFile))
    if not os.path.isfile(CurrentSoccerScheduleFile):
        print("[Error] Cannot find current soccer schedule: {}".format(CurrentSoccerScheduleFile))
        sys.exit(1)
    
    dfCurrentSchedule = pd.read_csv(CurrentSoccerScheduleFile, dtype=str)
    dfCurrentSchedule.set_index("Game", inplace=True)


    ###############################################################################################################################
    # Load up-to-date schedule from Web URL
    ScheduleName = dfScheduleConfig.loc[ScheduleParam,"ScheduleName"]
    print("[Log] Query web for schedule updates for: {}".format( ScheduleName))
    dfWebSchedule = LoadWebSchedule( dfScheduleConfig.loc[ScheduleParam,"ScheduleURL"], dfScheduleConfig.loc[ScheduleParam,"TeamName"] )
    if dfWebSchedule.empty:
        print("[ERROR] Web Schedule not found for: {}".format( ScheduleName))
        sys.exit(1)


    dfJoin = pd.DataFrame.merge(dfCurrentSchedule, dfWebSchedule, how='inner', on='Game', suffixes=('_OLD','_WEB'))

    datechanged = dfJoin.Date_OLD != dfJoin.Date_WEB
    venuechanged = dfJoin.Venue_OLD != dfJoin.Venue_WEB
    timechanged = dfJoin.Time_OLD != dfJoin.Time_WEB

    dfChanged = dfJoin[ datechanged | venuechanged | timechanged ]

    if dfChanged.empty:
        print("[Log] No schedule changes detected")

    else:
        print("[Log] Updating current schedule to: {}".format(CurrentSoccerScheduleFile))
        dfWebSchedule.to_csv(CurrentSoccerScheduleFile, quoting=csv.QUOTE_NONNUMERIC)


        print("[Log] There has been a Venue or Time change to the schedule:")
        changelist=dfChanged[["Date_OLD","Venue_OLD","Time_OLD","Date_WEB","Venue_WEB","Time_WEB"]].values.tolist()
        for currentchange in changelist:
            dateold, venueold, timeold, datenew, venuenew, timenew = currentchange

            dateold_obj = datetime.datetime.strptime( dateold, '%A, %B %d, %Y')
            datenew_obj = datetime.datetime.strptime( datenew, '%A, %B %d, %Y')
            print("[Log] Change Event for: {}".format(ScheduleName))
            print("[Log]     New: {} {} @{}".format(datenew_obj.date().strftime('%A, %m-%d-%Y'),timenew,venuenew))
            print("[Log]     Old: {} {} @{}".format(dateold_obj.date().strftime('%A, %m-%d-%Y'),timeold,venueold))
            

            currentmessage = TEXTMESSAGE.format(ScheduleName, timenew, datenew_obj.date().strftime('%m-%d-%Y'), venuenew, timeold, dateold_obj.date().strftime('%m-%d-%Y'), venueold)
            for currentrecipient in MailingList:
                print("[Log] sending update email to: {}".format(currentrecipient))
                server.sendmail(sender_email, currentrecipient, currentmessage)

    print("[Log] Script complete.")    


# If module is executed by name using python.exe, enter script through Main() method.  If it is imported as a module, Main() is never executed at it is used as a library
if __name__ == "__main__":
    Main(sys.argv)
