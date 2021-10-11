path1 = r"C:\Users\WWW\Desktop\file_1.txt"
path2 = r"C:\Users\WWW\Desktop\file_2.txt"
file1 = open(path1)
file2 = open(path2, 'w')

string = file1.read()
string = string.swapcase()

file2.write(string)
file1.close()
file2.close()
