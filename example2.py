# design a function that can enable a user to compare three elements and printthe largest one 
def find_largest(a,b,c):
    if a > b and a > c:
        return a 
    elif b > a and b > c:
        return b
    else:
        return c
    

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
    
largest = find_largest(num1, num2, num3)
print(f"The largest number is: {largest}")  

