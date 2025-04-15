# Write a program to generate a list of 10 random integers in the range 1-xxx where xxx is the last 3 -digits of your registration number.
import random
numbers = [random.randint(0,999) for _ in range (10)]
print(numbers)

# Define a function to find how many integers from the above list are prime numbers.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
c = 0
for i in numbers:
    if is_prime(i):
        c+=1
print("No of prime numbers: ",c)

new_li = numbers.copy()

# Define a function to convert the list into the nearest square matrix by appending 0s if required.
def to_square_matrix(li, size=4):
    total_elements = size * size
    while len(li) < total_elements:
        li.append(0)
    matrix = [li[i:i+size] for i in range(0, total_elements, size)]
    return matrix

matrix = to_square_matrix(numbers, size=4)
print("square matrix:")
for row in matrix:
    print(row) 

# Function to plot a pie chart of even and odd numbers in the list
import matplotlib.pyplot as plt

even_count = sum(1 for x in numbers if x % 2 == 0)
odd_count = len(numbers) - even_count
labels = ['Even', 'Odd']
sizes = [even_count, odd_count]
colors = ['blue', 'orange']
explode = (0.1, 0)  
plt.figure(figsize=(6, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Even vs Odd Numbers')
plt.show()

# Function to plot a bar chart of prime numbers vs non-prime numbers in the list
prime_count = sum(1 for x in numbers if is_prime(x))
non_prime_count = len(numbers) - prime_count
categories = ['Prime', 'Non-Prime']
counts = [prime_count, non_prime_count]
colors = ['green', 'red']
plt.figure(figsize=(6, 4))
plt.bar(categories, counts, color=colors)
plt.title('Prime vs Non-Prime Numbers')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

# Sort the list with odd numbers first in ascending order followed by even numbers in ascending order
sorted_li = sorted(numbers, key=lambda x: (x % 2 == 0, x))
print("Sorted List (Odd first, Even next):", sorted_li)