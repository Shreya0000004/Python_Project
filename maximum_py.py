# Python code for finding the maximum of 2 numbers
def maximum(a,b):
  if a>b:
    return a
  else:
    return b
 
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
print("The maximum number is:", maximum(a,b))

