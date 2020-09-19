# Personal Python 3.6 Template
import getopt
import os
import sys
import shutil



def print_usage():
    """
    Help printout for current Script
    """

    print("")
    print("ScriptName <OPTIONS>")
    print("")
    print("  {: <15} {: >10}".format(*['-h, -?, --help','Displays this help output']))
    print("  {: <15} {: >10}".format(*['--test1','Test Scriptname'])) 
    print("  {: <15} {: >10}".format(*['--test2=value','Test Scriptname'])) 



######################################################################################################################################################################
#
# Main()
#
######################################################################################################################################################################
    

def Main(argv):

    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   '?h',                # each character represents a sort option -?, -H
                                   ['help','test1','test2=']      # each list entry represents a long option --help, etc.
                                   )
    except getopt.GetoptError as err:
        print (str(err))
        print_usage()
        sys.exit(1)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        print_usage()
        sys.exit(1)

    # Example:  python.exe PythonTemplate.py --test1 --test2=test2val file1 file2
    # Result:
    #    opts: [('--test1', ''), ('--test2', 'test2val')]
    #    args: ['file1', 'file2']
    print("opts: "+repr(opts))
    print("args: "+repr(args))

    optdict = {x[0]:x[1] for x in opts}    #dictionary comprehension to fill optdict

    #for opt, val in opts:
    #    if opt in ['-?','-h','--help']:
    #        print_usage()
    #        sys.exit(0)
    #    if opt in ['--test1','--test2']:
    #        print('TEST MODE')


    if set(['--test1','--test2']).issubset(optdict):
        print("test1 and test2")
        sys.exit(0)
    if set(['--help','--test2']).issubset(optdict):
        print("help and test2")
        sys.exit(0)
    if set(['--test1','--help']).issubset(optdict):
        print("help and test1")
        sys.exit(0)
    if '--test1' in opts:
        print("test1")
        sys.exit(0)




# If module is executed by name using python.exe, enter script through Main() method.  If it is imported as a module, Main() is never executed at it is used as a library
if __name__ == "__main__":
    Main(sys.argv)
