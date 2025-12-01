# The pathlib library has a class called Path that is very helpful
# for navigating fodlers and files, so we import it.
from pathlib import Path

# This command will generate an object for the folder this very file is in.
HERE = Path(__file__).parent

# This command will generate an object for the input file, by combining the 
# path the file is on and the name of the file itself.
# PLEASE RENAME <FILENAME> to your puzzle input file name 
# AND ensure they're in the same folder.
INPUT = HERE / "<FILENAME>.txt"

# To read the file, there are multiple ways, but the standard, safe way
# is as follows. You don't need to know how it works, but if you wish to 
# look it up, it's called a context manager. The "r" stands for "read" as we
# only want to know what's in the file, not change it.
with open(INPUT, "r") as f:

    # we can create a string that contains the entire file, including linebreaks:
    file_content = f.read()

    f.seek(0)

    # or we can create a list that contains all the lines in the file. This
    # will make it easier to iterate through those lines, so that's what
    # I'd recommend.
    file_lines = f.readlines()

# note that when we go back to the base indentation level, the f object will
# be out of scope, so f.read will no longer work here.

# some cleanup you may ignore
file_lines = [line[:-1] for line in file_lines if line[-1]=="\n"]


print(file_content)
