# Part 1
heights = [1.82,1.75,1.68,1.76,1.5]

for height in heights:
  print(height)

for height in heights:
  if(height > 1.75):
    print(height)

for height in heights:
  print(height)

  if(height == 1.68):
    break

for height in heights:
  if(height != 1.68):
    print(height)

# Part 2
i = 0
while(i < 4):
  print(i)
  i+=1

i = 0
while(i < 15):
  if(i % 2 == 0):
    print(i)
  i+=1

i = 6
while(i < 15):
  print(i)
  i+=1

# Part 3
actors = [
    "Nathan Fillion",
    "Gina Torres",
    "Alan Tudyk",
    "Morena Baccarin",
    "Adam Baldwin",
    "Jewel Staite",
    "Sean Maher",
    "Summer Glau",
    "Ron Glass"
]

roles = [
    "Captain Malcolm Reynolds",
    "Zoe Washburn",
    "Hoban Washburn",
    "Inara Serra",
    "Jayne Cobb",
    "Kaylee Frye",
    "Dr. Simon Tam",
    "River Tam",
    "Derrial Book"
]

for n in range(len(actors)):
  print(actors[n] + " as " + roles[n])
  