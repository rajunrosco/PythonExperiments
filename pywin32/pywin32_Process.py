


import os
import sys
import win32com.client

this_modulepath = os.path.dirname(os.path.realpath(__file__))

def get_processes(procname):
    pidList = []
    for proc in win32com.client.GetObject('winmgmts:').InstancesOf('win32_process'):
        if proc.Name.upper() == procname.upper():
            pidList.append( proc.Properties_('ProcessId'))
    return pidList


def kill_processes(procname):
    pidList = get_processes(procname)
    for pid in pidList:
        try:
            os.kill(int(pid), 0)
        except (OSError, TypeError) as e:
            print(e)
        except (SystemError) as e:
            print("kill {}: {}".format(procname, pid))


    
###############################################################################################
#
# Test Area
#
###############################################################################################

get_processes("excel.exe")

kill_processes("excel.exe")