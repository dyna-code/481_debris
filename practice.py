def main():
    with open('input_file.txt', 'r') as file:
                # Read the content of the file, split it by spaces, and convert each element to an integer
                        numbers = [int(num) for num in file.read().split()]

    

    # Calculate the average by dividing the sum of the numbers by the total count
    average = sum(numbers) / len(numbers)

    # Print the result
    print(f"The average of the given integers is: {average:.2f}")
if __name__ == "__main__":
    main()
