# Part 1
def greeting(name):
  print(f"""Hello {name},
Lovely weather today!
Hope it stays so good.""")

names = ["Clark", "Willow", "Wasabi"]

for name in names:
  greeting(name)

# Part 2
def hello(first, last):
  print(f"Hello {first} {last}")

hello("Clark", "Pegg")

# Part 3
def add(num1, num2):
  print(f"{num1} + {num2} = {num1+num2}")

add(2, 3)

# Part 4
def add_no_print(num1, num2):
  return num1 + num2

num1 = 4
num2 = 5

print(f"{num1} + {num2} = {add_no_print(num1, num2)}")

# Part 5
def add_list(numbers):
  sum = 0

  for number in numbers:
    sum += number

  return sum

num_list = [0,2,3,4,5,6]

print(add_list(num_list))

# Part 6
def reverse_string(string):
  return string[::-1]

my_string = "Hello there!"

print(reverse_string(my_string))

# Part 7
def check_range(number, range):
  if(number >= range[0] and number <= range[1]):
    return True
  return False

print(check_range(4, (1, 6)))
print(check_range(0, (1, 6)))
