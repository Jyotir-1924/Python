f = open("read_file.txt", "r")

print(f.read())

for line in f:
    print(line)
    
f.close()
# The above code opens a file named "read_file.txt" in read mode and prints the file object.
# The file is then closed.