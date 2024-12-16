def calculate_bill():
    print("\nWelcome to the Pizza Ordering System!")
    print("=========================================")

    size = input("Please choose your pizza size:\n[S] Small ($15)\n[M] Medium ($20)\n[L] Large ($25)\nYour choice (S, M, L): ").upper()
    while size not in ['S', 'M', 'L']:
        print("Invalid choice! Please enter 'S', 'M', or 'L'.")
        size = input("Your choice (S, M, L): ").upper()

    add_pepperoni = input("\nWould you like to add pepperoni? (Y/N): ").upper()
    while add_pepperoni not in ['Y', 'N']:
        print("Invalid choice! Please enter 'Y' for Yes or 'N' for No.")
        add_pepperoni = input("Would you like to add pepperoni? (Y/N): ").upper()

    extra_cheese = input("\nWould you like extra cheese? (Y/N): ").upper()
    while extra_cheese not in ['Y', 'N']:
        print("Invalid choice! Please enter 'Y' for Yes or 'N' for No.")
        extra_cheese = input("Would you like extra cheese? (Y/N): ").upper()

    bill = 0
    if size == "S":
        bill = 15
    elif size == "M":
        bill = 20
    elif size == "L":
        bill = 25

    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 4


    print("\n==================== ORDER SUMMARY ====================")
    print(f"Pizza Size: {size} - ${bill - 2 if add_pepperoni == 'Y' else bill - 4 if extra_cheese == 'Y' else bill}")
    print(f"Add Pepperoni: {'Yes' if add_pepperoni == 'Y' else 'No'} - ${2 if add_pepperoni == 'Y' else 0}")
    print(f"Add Extra Cheese: {'Yes' if extra_cheese == 'Y' else 'No'} - ${4 if extra_cheese == 'Y' else 0}")

    print("\n=======================================================")
    print(f"Your final bill is: ${bill}")
    print("\nThank you for ordering! Enjoy your pizza!")
    print("=======================================================\n")


calculate_bill()
