a = int(input("Enter the First Number:"))
b = int(input("Enter the Second Number:"))

print("AND Result: ", a, b, (a==b) and (a>0))
print("OR Result: ", a, b,(a!=b) or (a<=b))
print("NOT Result: ", a, b,not(a!=b))
