'''
#Escaping Characters

out = "This is a \"Test Server\""
print(out) # This is a "Test Server"
######################################################
#Slicing String
str1 = "yellow flat"
#print(len(str1))
print(str1[0])     # => 'y'
print(str1[-1])    # => 't'
print(str1[0:6])   # => 'yellow'
print(str1[:4])    # => 'yell'
print(str1[-3:])   # => 'lat'
print(str1[:-3])   # => 'yellow f'

#########
out = "This is Nepolean"

#print first element
#print(out[15])

print(out[-1])

#print(out[0:4])

print(out[-5:-2])

print(len(out))

print(out[0:len(out)])

print(out[(len(out) - 8):len(out)])

######################################################
#Get Length Of a String
#Example - 1
servername = input("Enter the server name:")
print(servername)
print(len(servername))

#Example - 2
colors = ["red", "yellow", "green"]
print(colors)
print(type(colors))
print(len(colors)) # 3

######################################################

#String Concatenation
firstname = input("Enter the First Name:")
lastname = input("Enter the Last Name:")
print("User Name:", firstname + " " + lastname)

######################################################

#Sring Formatting
#Example - 1
msg1 = "Running {} out of {} servers."
print(msg1.format(3, 10)) # Running 3 out of 10 servers.

#Example - 2
msg2 = 'Server Name: {name} ; IP Address: {ip} ; Port: {port}.'
print(msg2.format(name='localhost', ip='53.23.12.4', port='443'))

######################################################

#Lower Case & Upper case change
greetings = "Welcome To Python"
print(greetings.lower())
print(greetings.upper())

######################################################

#Change Title 
heading = "dark knight"
print(heading.title())

######################################################

#Strip - Remove unwanted spaces/characters
text1 = "   apples and oranges   "  
print(text1.strip())       # => 'apples and oranges'

text2 = '...+...apples and oranges...-...'
# Here we strip just the "." characters
print(text2.strip('.'))

# Here we strip both "." and "+" characters
print(text2.strip('.+'))

# Here we strip ".", "+", and "-" characters
print(text2.strip('.+-'))

######################################################

#Splitting the String - Sub String
#text = "Red Apple"
#print(text)
#print(type(text))
#print(text.split())  # Prints: ['Red', 'Apple']
#print(type(text.split())) # class list
#print(text.split()[0] + "\n" + text.split()[1])
#print(text.split('l'))

user = "JeyaRaj:100:200:/home:/bin"
username = user.split(":")[2]
print(username)
print(type(username))
######################################################

#Find first occurance of a character index in a string
mountain_name = "Mount Everest"
print(mountain_name.find('Mount'))
print(mountain_name.find('Everest123'))
print(mountain_name.find('Everest'))

#if(mountain_name.find('Good') == "-1"):
#    print("This keyword is not found")
######################################################

#Replace a character/string
fruit = "I like Apple"
#print(fruit.replace('Apple', 'Mango'))
fruit_new = fruit.replace('Apple', 'Mango')
print(fruit)
print(fruit_new)

'''
######################################################
#Join multiple Strings - concatenates a list of strings together.
#List to String
x = " ".join(["This", "is", "Awesome"])  #"This" + "-" + "is" + "-" + "Awesome"
print(x)
'''
######################################################
#Exercise - 1:

servername1 = input("Enter the server1 name:")
servername2 = input("Enter the server2 name:")
servername3 = input("Enter the server3 name:")

print("Type 1: The entered server details are:",servername1,",",servername2,",",servername3)
print("Type 2: The entered server details are:",servername1 + "," + servername2 + "," + servername3)
print("Type 3: The entered server details are:", ",".join([servername1,servername2,servername3]))

######################################################

#Exercise - 2:

cloud = input("Enter the cloud environments (Use ',' for multiple values) :")
print(cloud.split(",")[0])

######################################################
'''