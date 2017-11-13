import locale

# get local encoding
defaultEncoding = locale.getpreferredencoding()

# open file to read from it
file = open('words.txt', encoding=defaultEncoding)

print('Files\' name is %s. Files\' encoding is %s. Files\' open mode is %s.' \
  % (file.name, file.encoding, file.mode))

# reading data from a text file
#print(file.read())

# move to a specific byte position in file
# file.seek(10)
# file.read(10)

# # tell will give current file position
# print(file.tell())

# at position 10 read 10 characters
#print(file.read(10))

# close file
file.close()
print(file.closed)

# automatically close file
# with open('words.txt', encoding=defaultEncoding) as autoCloseFile:
#   words = autoCloseFile.read()
#   print(words)
# print(autoCloseFile.closed)

# stream object is an iterator, a for loop can be used to read a file line-by-line
lineNum = 0
with open('words.txt', encoding=defaultEncoding) as liner:
  for line in liner:
    lineNum += 1
    print('{:>4} {}'.format(lineNum, line.rstrip()))

# writing to file
# mode='w' append to end of file
with open('writer.txt', mode='w', encoding=defaultEncoding) as writer:
  writer.write('yo!')
# mode='a' append to end of file
with open('writer.txt', mode='a', encoding=defaultEncoding) as writer:
  writer.write('yo2!')

# open binary files use mode='rb' in open() function

# compressed files
import gzip

with gzip.open('somethin.zip', mode='wb') as zipFile:
  zipFile.write('some stuff being written to a compressed file'.encode('utf-8'))
