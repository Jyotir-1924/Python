f = open("write_file.txt", "w")
# The above code opens a file named "write_file.txt" in write mode.
# In write mode, if the file already exists, it will be overwritten.
# If the file does not exist, it will be created.
string = '''
This is a test file.
It contains multiple lines.
This is the third line.
'''
# The above code creates a multi-line string.
f.write(string)
# The above code writes the multi-line string to the file.
f.close()