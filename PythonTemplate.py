# Import packages
import sys

# Write your functions
def helpful_function():
    return()

# Write the script. If you contain your script within:
# 'if__name__ == "__main__":' then you can run your script
# when this file is run but still import the file and use the functions elsewhere

if __name__ == "__main__" :
    ls = len(sys.argv)
    assert ls > 1, "Insert File" # If no files found, insert file will be printed
    print(ls)
    filename = sys.argv[1:ls]
    matchers = ['.py','.r',',']
    matching = [s for s in filename if any(xs in s for xs in matchers)]
    assert len(matching) >= 1, "Wrong File Format"
    # Setup CArbon monitoring
    # Running file filename
    # Record data of carbon usage during file execution
    exit()

