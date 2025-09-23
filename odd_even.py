while True:
    choice = input("Do you want odd or even? ").lower()
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))

    total = 0
    for num in range(start, end + 1):
        if choice == "odd" and num % 2 != 0:
            print(num)
            total += num
        elif choice == "even" and num % 2 == 0:
            print(num)
            total += num

    print("Total of num:", total)

    again = input("\nDo you want to try again? (yes/no): ").lower()
    if again == "no":
        break
