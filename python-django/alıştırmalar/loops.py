__author__ = 'schwappkopf'


x = 1

print "while loop\n"
while(x<9):
    print " num : %d " % x
    x=x+1

#infite loop
# var = 1
# while var == 1 :  # This constructs an infinite loop
#   num = raw_input("Enter a number  :")
#   print "You entered: ", num

print "for loop\n"

for letter in "Python":
    print "current letter: ",letter

cars= ['bmw','mercedes','ferrari']
for car in cars:
    print "current car: ", car

# uzunluğa göre for loop
for index in range(len(cars)):
    print "current car: ", cars[index]


# == kullanarak
while (True):
    word = str(raw_input("bir kelime girin: "))
    if word == "q":
            break



# for (i=2; i<10 ; i++)
for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print n, 'equals', x, '*', n/x
             break
     else:
         # loop fell through without finding a factor
        print n, 'is a prime number'

#To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
     print 'What is your {0}?  It is {1}.'.format(q, a)