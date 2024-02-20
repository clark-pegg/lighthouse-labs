def sumLargestNumbers(numbers):
  largest = 0
  secondLargest = 0

  for number in numbers:
    if(number > largest):
      secondLargest = largest
      largest = number
      
  return largest + secondLargest

print(sumLargestNumbers([1, 10]))
print(sumLargestNumbers([1, 2, 3]))
print(sumLargestNumbers([10, 4, 34, 6, 92, 2]))