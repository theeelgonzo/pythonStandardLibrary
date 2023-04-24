# Least to Greatest
pointsInAGame = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(pointsInAGame)
print(sortedGame)
# Alphabetically
children = ['sue', 'jerry', 'linda']
print(sorted(children))

# Key Parameters
print(sorted("My favorite child is Linda".split(), key=str.upper))
print(sorted(pointsInAGame, reverse=True))

leaderBoard = {231: 'CKL', 123: 'ABC', 432: 'JKC'}
print(sorted(leaderBoard, reverse=True))

students = [('Alice', 'B', 12), ('Eliza', 'A', 16), ('Tae', 'C', 15)]
print(sorted(students, key=lambda student:student[1]))
