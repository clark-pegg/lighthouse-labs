def conditionalSum(values, condition):
  sum = 0

  for value in values:
    if(condition == "even" and value % 2 == 0):
      sum += value
    elif(condition == "odd" and value % 2 == 1):
      sum += value

  return sum

print(conditionalSum([1, 2, 3, 4, 5], "even"))
print(conditionalSum([1, 2, 3, 4, 5], "odd"))
print(conditionalSum([13, 88, 12, 44, 99], "even"))
print(conditionalSum([], "odd"))