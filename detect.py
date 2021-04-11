import getopt, sys
import FND
# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]
options = "t:r:s:h"
long_options = ["Title:", "Text:", "Source:", "Help"]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
    # checking each argument
    for currentArgument, currentValue in arguments:

        if currentArgument in ("-h", "--Help"):
            print("Displaying Help")

        elif currentArgument in ("-s", "--Source"):
            FND.detector1(text = None, title = None, source = currentValue )

        elif currentArgument in ("-t", "--Title"):
            FND.detector1(text = None, title = currentValue , source = None)

        elif currentArgument in ("-r", "--Text"):
            FND.detector1(text = currentValue, title = None  , source = None)

except getopt.error as err:
    main.driver.close()
    print(str(err))