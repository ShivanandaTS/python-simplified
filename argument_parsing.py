''' 
Argument parsing: provides a way to dynamically configure script behavior from the command line.
Users can pass parameters to achieve varied outcome, making the script versatile.

'''

import sys
import getopt

def main(argv):
    # sys.argv[0] will be the running py name
    # sys.argv[1:] will be the entire list of arguments and options passed through command line
    # shortopts are the options that should be together without a space. Single character only.
    # Use of colon will pair the following argument with the option
    # longopts can contain multiple characters unlike shortopts
    # Use of equalto will pair the following argument with the option
    try:
        opts, args = getopt.getopt(args=argv[1:], shortopts='hf:m:', longopts=['help', 'filename=', 'message='])
        print('opts =', opts)
        print('args =', args)
    except getopt.GetoptError:
        print('usage: scriptname.py -f <filename> -m <message> [-v]')
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
            print('usage: scriptname.py -f <filename> -m <message> [-v]')
        elif opt in ('-v', '--verbose'):
            verbose = True
    if verbose:
        print('Verbose mode enabled')

    print('Filename and Message:', filename, message)
    with open(filename, 'w+') as f:
        f.write(message)

if __name__=='__main__':
    # Command-line input: Options, if used, strictly should be 
    # passed first in sequence, followed by any number of arguments.
    main(sys.argv)