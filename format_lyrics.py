# I made this to quickly format text files
# Right it just capitalizes the first character of each line
#
# Usage:
# python format_lyrics.py -i <input_file> -o <output_file> -r <chars>
#
# Options details:
# -i <file>   specify input filename
# -o <file>   specify output filename (doesn't need to exist)
# -c          capitalizes each line
# -r <chars>  removes each instance of the specified characters

import sys, getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "i:o:r:c")
except getopt.GetoptError as err:
    print str(err)
    sys.exit(2)

# Set explicit defaults for options
capitalize = False
remove = []

# Pars args for input, output, options
for opt, arg in opts:
    if opt == '-i':
        source = open(arg, 'r')
    elif opt == '-o':
        dest = open(arg, 'w')
    elif opt == '-c':
        capitalize = True
    elif opt == '-r':
        remove = arg
    else:
        assert False, "unhandled option"

# Do your thing!
for line in source:
    new_line = line

    # Capitalize if necessary
    if capitalize:
        new_line = new_line[0].capitalize() + new_line[1:]

    # Remove desired characters
    if len(remove) > 0:
        for char in remove:
            new_line = new_line.replace(char, '')

    dest.write(new_line)

source.close()
dest.close()
