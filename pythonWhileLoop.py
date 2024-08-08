# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.

i=1
while i<10:
    print(i,end=" ")
    if i==5:
        break
    i+=1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
else:
   print("condition not match to run while")