num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

if num1 > num2:
    print("num1 is greater than num2")
elif num1 < num2:
    print("num1 is less than num2")
else:
    print("num1 is equal to num2")
















def compare():
    my_list = [1, 2, 3]
    my_tuple = (1, 2, 3)

    print("List is mutable:", isinstance(my_list, list))
    print("Tuple is immutable:", isinstance(my_tuple, tuple))

    # Modify list
    my_list[0] = 10

    print("Modified list:", my_list)

    # Tuple cannot be modified (will cause error if attempted)
