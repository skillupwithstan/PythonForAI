'''
#sample_list = []
#print(type(sample_list))

name_list = ["Arockia","Rajesh","Ravi"]
print(name_list[1])
print(len(name_list))

#print([None]*5)

name_list[1] = "Kumar"
print(name_list)

#Conditional Statement in Lists
list_of_network_devices = ["network1","network2","network3"]
network = "network4"
if network in list_of_network_devices:
    print(network + " is found")
else:
    print(network + " is not found")

#Looping in Lists
list_of_network_devices = ["network1","network2","network3"]

#print(range(4))

print("Iterating the list using range() class")
for index in range(len(list_of_network_devices)): #0,1,2:
    print(list_of_network_devices[index])

print("Iterating the list using the keyword in")
for network in list_of_network_devices:
    print(network)

list_of_network_devices.append("network4")
print(list_of_network_devices)
'''





sample_list = [2,4,7,10]
print(max(sample_list))

sample_list.append(12)
print(sample_list)

print(sample_list.index(10))

sample_list.pop(3)
print(sample_list)

sample_list.remove(7)
print(sample_list)

sample_list.sort()
print(sample_list)

sample_list.reverse()
print(sample_list)






