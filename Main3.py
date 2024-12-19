def add (p,q):
    return p+q

def subract (p,q):
    return p-q

def multiply (p,q):
    return p*q

def divide (p,q):
    return p/q 

print("Please select operation: ")
print("a. Add ")
print("b. Subract ")
print("c. Multiply ")
print("d. Divide ")

choice= input("please enter choice a/b/c/d: ")

num_1=int(input("Enter first number: "))
num_2=int(input("Enter second number: "))

if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == 'b':
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))
elif choice == 'c':
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice == 'd':
    print(num_1, "/", num_2, "=", divide(num_1, num_2))
else:
    print("This is an invalid input")
