''' 
Argument parsing: provides a way to dynamically configure script behavior from the command line.
Users can pass parameters to achieve varied outcome, making the script versatile.
'''

import sys
import getopt

def main(argv):
    # sys.argv[0] will be the running py name
    # sys.argv[1:] will be the entire list of arguments and options passed through command line
    # shortopts are the options. They should be single character only without a space.
    # longopts can contain multiple characters unlike shortopts
    try:
        opts, args = getopt.getopt(
            args=argv[1:],
            shortopts='hf:m:v',
            longopts=['help', 'filename=', 'message=', 'verbose'],
        )
        # Use of colon in shortopts indicates that -f and -m should be followed by a value
        # Use of equal sign in longopts indicates that --f and --m should be followed by a value
        # Square brackets in the usage string indicate that the argument is optional
        print('opts =', opts)
        print('args =', args)
    except getopt.GetoptError:
        print('usage: py scriptname.py -f <filename> -m <message> [-v]')
        sys.exit(1)
    
    filename = 'test.txt'
    message = ''
    verbose = False
    # When enabled, verbose mode outputs more information 
    # than the default mode, which can be helpful for debugging
    for opt, arg in opts:
        if opt in ('-f', '--filename'):
            filename = arg
        elif opt in ('-m', '--message'):
            message = arg
        elif opt in ('-h', '--help'):
            print('usage: py scriptname.py -f <filename> -m <message> [-v]')
        elif opt in ('-v', '--verbose'):
            verbose = True
    if verbose:
        # When users report issues, asking them to run the program in verbose mode can 
        # provide developers with the detailed information needed to reproduce and fix bugs.
        # Detailed info in this example are the following prints.
        print("Verbose mode is enabled.")
        print(f"Filename: {filename}")
        print(f"Message: {message}")
        print(f"Remaining args: {args}")
    
    if filename and message:
        print('Filename and Message:', filename, message)
        with open(filename, 'w+') as f:
            f.write(message)

if __name__=='__main__':
    # Command-line input: Options, if used, strictly should be 
    # passed first in sequence, followed by any number of arguments.
    main(sys.argv)