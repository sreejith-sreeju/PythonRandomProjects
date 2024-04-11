print("hello","welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit('exit from this')

print("Okay! let's play :)")
score = 0

answer = input('Whats does cpu stands for? ')
if answer.lower() == 'central processing unit':
    print('CORRECT!')
    score += 1
else:
    print("incorrect!")

answer = input('what is ups? ')
if answer.lower() == 'universal power supply':
    print('CORRECT!')
    score += 1
else:
    print("incorrect!")

answer = input('Whats is a bus? ')
if answer.lower() == 'vehicle':
    print('CORRECT!')
    score += 1
else:
    print("incorrect")

answer = input('what is ksrtc stands for? ')
if answer.lower() == 'transportation service':
    print('CORRECT!')
    score += 1
else:
    print("incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) +"%.")


