print('Beräknar differensen av jämna/udda tal ....')

# Initialize the sum to zero
sum_of_odds = 0
sum_of_even = 0

# Create a list of odd numbers from 1 to 999
odd_numbers = list(range(1, 1000, 2))
even_numbers = list(range(0, 1000, 2))

# Iterate over the list and add each number to the sum
for num in odd_numbers:
    sum_of_odds += num

# Iterate over the list and add each number to the sum
for num in even_numbers:
    sum_of_even += num    

# Print the sum
print(sum_of_odds)
print(sum_of_even)
print(f"differensen =  {sum_of_odds - sum_of_even}")
