def is_armstrong(
    num,
):  # Creating a function to check if the number is an armstrong number or not
    cubes = []  # Creating an empty list to store the cubes of digits of the number

    for (
        item
    ) in (
        num
    ):  # Using for loop to get the digits in the number and cubing them and appending them to list named 'cubes'
        item = int(item) ** 3
        cubes.append(item)

    sum_of_cubes = sum(
        cubes
    )  # Using sum function to add all the numbers in 'cubes' list that contains the cubes of digits of the original number

    if (
        sum_of_cubes == original_number
    ):  # Checking if sum of cubes of the digits of the original number is equal to original number, if it is then its an armstrong number else not
        print(f"{original_number} is an armstrong number.\n")
    else:
        print(f"{original_number} is not an armstrong number.\n")

    cubes = []  # Resetting the list 'cubes' for storing cubes of digits of next input


while True:
    num = str(abs(int(float(input("Enter A Number: \t")))))  # Taking Input
    original_number = int(num)

    is_armstrong(num)  # Running the function
