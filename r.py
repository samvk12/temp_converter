numbers = [10, 25, 7, 50, 32]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)
