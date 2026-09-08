# Reading entire file - .txt, .log, .csv, .json, .xml, .html, .py, etc.
filedata = open("FileContent.txt") # "C:\\Temp\\file.txt"
#print(filedata)
#Option - 1
#content = filedata.read()
#content = filedata.read(10)
#content = filedata.readline()
content = filedata.readlines()
print(content)

for i in content:
    if(i.find("Ramesh") >= 0):
        print("Ramesh is present in the file.")
        break
filedata.close()
