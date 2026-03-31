numbers = [5, 10, 15, 20, 25]

try:
    num = int(input("Select a number: "))

    if num not in numbers:
        raise ValueError("Number not in the list")

    print("You selected:", num)

except ValueError:
    print("The number you selected is not in the array.")
    print("Please choose a valid number from:", numbers)
