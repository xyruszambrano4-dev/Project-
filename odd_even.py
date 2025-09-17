# Odd/Even Number Generator

while True:
    print("Choose an option:")
    print("1. Show Odd Numbers")
    print("2. Show Even Numbers")

    choice = int(input("Enter your choice (1 or 2): "))
    limit = int(input("Enter the limit number: "))

    if choice == 1:
        print(f"Odd numbers from 1 to {limit}:")
        for i in range(1, limit + 1):
            if i % 2 != 0:
                print(i, end=" ")
        print("\n")

    elif choice == 2:
        print(f"Even numbers from 1 to {limit}:")
        for i in range(1, limit + 1):
            if i % 2 == 0:
                print(i, end=" ")
        print("\n")

    else:
        print("Invalid choice! Please select 1 or 2.\n")

    again = input("Do you want to try again? (yes/no): ")
    if again.lower() == "no":
        break
