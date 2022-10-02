names = ['Kelly', 'Jessa', 'Emma']
# outer loop
for name in names:
    # inner while loop
    count = 0
    while count < 5:
        print(name, end=' ')
        # increment counter
        count = count + 1
    print()

i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if(i%j): break
        j = j + 1
    if (j > i/j) : 
        print (' is prime')
    i = i + 1

print ("Good bye!")