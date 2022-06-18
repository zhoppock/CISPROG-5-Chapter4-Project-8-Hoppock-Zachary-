import os

def copyfile():
  fileName = input("What is the first file called? ")
  fileCopy = input("What is the copy file called? ")

  if os.path.exists(fileName):
    print("\n" + fileName + ": File exists.")
  else:
    print("\nFilename", fileName, "has been created.")

  f = open(fileName, 'w')
  content = input("What is in the first file? ")
  f.write(content)
  f.close()

  print("Content has been published in", fileName + ".")

  if os.path.exists(fileCopy):
    print("\n" + fileCopy + ": File exists.")
  else:
    print("\nFilename", fileCopy, "has been created.")

  c = open(fileCopy, 'w')
  f = open(fileName, 'r')

  text = f.read()
  c.write(text)
  c.close()

  print("Contents of", fileName, "have been copied to", fileCopy + ".")