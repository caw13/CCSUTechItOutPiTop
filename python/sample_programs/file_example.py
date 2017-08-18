example_file = "file_example.txt"
try:
    # Reading from a file
    
    f = open(example_file)
    lines = f.read().splitlines()
    print(lines)
    first_line = lines[0]
    second_line = lines[1]
    # Or loop through all
    for line in lines:
        print("Line: %s" % line)
    
    f.close()
except IOError:
    print("Cannot find the file: %s" % example_file)

# Writing to a file
example_out_file = "file_example_output.txt"
f = open(example_out_file, "a")
word = input("Next word to add to the file: ")
f.write("The next word entered is: %s \n" % word)
f.close()
