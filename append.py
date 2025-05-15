f = open("write_file.txt", "a")
string = '''
This is a append test line.
This writes to the end of the file.
'''
f.write(string)
f.close()