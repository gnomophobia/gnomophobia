#!/usr/bin/python
f0 = open("template.txt", "r")
template = f0.read()
f0.close
f1 = open("test.txt", "r")
while True:                            # Keep reading forever
  l = f1.readline()   # Try to read next line
  if len(l) == 0:              # If there are no more lines
    break                          #     leave the loop

# Now process the line we've just read
  print(l)

f1.close()


