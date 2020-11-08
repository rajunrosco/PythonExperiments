import datetime

def Practice_Datetime():
	
	birthday = datetime.date(1970, 1, 26)
	
	today = datetime.date.today()
	delaydays = 42
	delay = datetime.timedelta( days=delaydays )
	
	newdate = today + delay
	result = newdate.strftime("%A %B %d %Y")
	if newdate.strftime("%A").lower() == "friday":
		print "TGIF!"
	
	print result
	
	print "Birthday = "+birthday.strftime("%A, %B, %d, %Y")
	print "Birthday = "+birthday.strftime("%m/%d/%Y")
	delta = newdate - birthday
	
	print delta.days
	
def main():
	Practice_Datetime()
	
if __name__ == '__main__':
  main()
