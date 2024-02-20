import random

# Part 1
num1 = 2
num2 = 3.0

total = num1 + num2

print("The type of 'total' is: " + str(type(total)))

# Part 2
heightInCm = 184
massInKg = 70

heightInM = heightInCm / 100

bmi = massInKg / (heightInM * heightInM)

print("My BMI is: " + str(bmi))

# Part 3
name = "Clark"
surname = "Pegg"

fullname = name + " " + surname

print(surname)
print(surname[0])
print(fullname.replace(" ", ""))
print((surname + " ") * 10)

# Part 3b
greetings = f"Hello my name is {fullname}"
print(greetings)

# Part 4
empty_list = list()
heights = list()

for n in range(5):
  heights.append(random.randint(150, 200))

print(heights)
print(heights[1])

heights2 = heights[-3::]

print(heights2)

all_list = heights + heights2

print(all_list)
print("The type of 'all_list' is: " + str(type(all_list)))

# Part 5
empty_tuple = tuple()

try:
  empty_tuple[0] = "hello"
except Exception as error:
  print(error)

dict = dict()

height_dict = {"Clark": 184}
height_dict["Willow"] = 60 # she is a dog

print(height_dict)
print(height_dict["Clark"])

print(height_dict.keys())
print(height_dict.values())
