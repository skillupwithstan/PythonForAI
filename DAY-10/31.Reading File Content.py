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

#print(content[2])
#print(filedata.read())

#print(type(content))
#print(content.split("\n"))
#print(type(content.split("\n")))
#print(int(content.split("\n")[1]))

#print(content.split()[0:3])
'''
for i in content.split("\n"):
    print(i,end="\n")

#Option - 2
print("************ READ LINES METHOD ***************")
filedata = open("D:\Python Course\sample.txt")
print(filedata.readlines())
print(type(filedata.readlines()))
print("************ READ METHOD ***************")
filedata1 = open("D:\Python Course\sample.txt")
print(filedata1.read())
print(type(filedata1.read()))

#for f in filedata.readlines():
#    print(f,end="")

filedata.close()
filedata1.close()

print("\n***************************")

# Reading the content line by line

#filedata = open("FileContent.txt","r")
filedata = open("D:\Python Course\sample.txt")
line1 = filedata.readline()    
print(line1,end="")
#line2 = filedata.readline()    
#print(line2,end="")
#line3 = filedata.readline()    
#print(line3,end="")
filedata.close()

print("\n****************************")

#Reading the contents of a file into a list

filedata = open("FileContent.txt","r")
list_var = filedata.readlines()
print(type(list_var))
for line in list_var:
    print(line,end="") 
filedata.close()

print("\n***************************")

# Reading the contents of a file into a string

fldata = open("FileContent.txt","r")
data = fldata.read(8)
print(data)
print(type(data))
fldata.close()

print("\n***************************")

# Iterating a file

fldata = open("FileContent.txt","r")
for line in fldata:
    #if(line != "Server-3"):
    print(line)
    #if(line.replace("\n","") != "Server-3"):
    #   print(line,end="")
fldata.close()



serverfile = open("FileContent.txt")
serverdata = serverfile.read()
if(serverdata.find("localhost") >= 0):
    print("Localhost is present on the file.")
else:
    print("Localhost is not present on the file.")
serverfile.close()

isavailable = False
for server in serverfile.read().split("\n"):
    if(server == "localhost"):
        print("Localhost is present on the file.")
        isavailable = True
        break
if(isavailable == False):
    print("Localhost is not present on the file.")
serverfile.close()
'''



