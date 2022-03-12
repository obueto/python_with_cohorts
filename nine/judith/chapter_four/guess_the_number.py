import random


def guess_number():
    number = random.randrange(1, 1000)
    guess = None
    guess_count = 0

    while guess != number:
        guess_count += 1

        guess = int(input('Guess A Number Between 1 and 1000'))
        if guess < number:
            print('Too low. Try again')
        elif guess > number:
            print('Too high. Try again')
        else:
            print("Congratulations")
    if guess_count <= 10:
        print('Either you know the secret or you got lucky!')
    elif guess_count > 10:
        print('You should be able to do better')


guess_number()
