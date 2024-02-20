def instructorWithLongestName(instructors):
  longestName = (0, 0)

  for instructor in instructors:
    if(len(instructor["name"]) > longestName[0]):
      longestName = (len(instructor["name"]), instructor)

  return longestName[1]


print(instructorWithLongestName([
  {"name": "Samuel", "course": "iOS"},
  {"name": "Jeremiah", "course": "Data"},
  {"name": "Ophilia", "course": "Web"},
  {"name": "Donald", "course": "Web"}
]))

print(instructorWithLongestName([
  {"name": "Matthew", "course": "Data"},
  {"name": "David", "course": "iOS"},
  {"name": "Domascus", "course": "Web"}
]))