first_number = int(input("Type your first number: "))
second_number = int(input("Type your second number: "))
print(f"Press 1 to see the even numbers from {first_number} to {second_number}.\n"
      f"Press 2 to see the odd numbers from {first_number} to {second_number}.\n"
      f"Press 3 to see the squares of the numbers from {first_number} to {second_number}.\n"
      f"Press 4 to finish.")
choice = int(input("Type your choice here: "))
while choice != 4:
    if choice == 1:  # Even numbers
        for i in range(first_number, second_number + 1):
            if i % 2 == 0:
                print(i, end=" ")
    elif choice == 2:  # Odd numbers
        for i in range(first_number, second_number + 1):
            if i % 2 == 1:
                print(i, end=" ")
    elif choice == 3:  # Squares of numbers
        for i in range(first_number, second_number + 1):
            print(i ** 2, end=" ")
    else:
        print("Invalid choice")
    print()
    print(f"Press 1 to see the even numbers from {first_number} to {second_number}.\n"
          f"Press 2 to see the odd numbers from {first_number} to {second_number}.\n"
          f"Press 3 to see the squares of the numbers from {first_number} to {second_number}.\n"
          f"Press 4 to finish.")
    choice = int(input("Type your choice here: "))
print("Your finished! Good job!")
