def calculate_average(numbers):
    if not numbers:  # Handle empty list
        return 0
    return sum(numbers) / len(numbers)

#Example usage
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#Example with ZeroDivisionError handled
my_numbers_2 = []
average_2 = calculate_average(my_numbers_2) 
print(f"The average is: {average_2}") 