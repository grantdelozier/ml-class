import os
import sys


if 'MLCLASS' in os.environ:
	print "MLCLASS variable set to ", os.environ['MLCLASS']
else:
	print >> sys.stderr, "WARNING: $MLCLASS environment variable not set"


def main():
    "blah"

if __name__ == "__main__":
    main()