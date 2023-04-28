# Files and File Writing

# Open a file
myFile = open('scores.txt', 'w')
# w --> write
# r --> read
# r+ --> read and write
# a --> append
# Show attributes and properties of that file
print(' name ' + myFile.name
)
print('mode ' + myFile.mode)
# Write to a file
myFile.write('GBJ : 100 \nKHD: 99\nBBB: 89')
myFile.close()

# Read the file
myFile = open('scores.txt', 'r')
print('reading...' + myFile.read(10))