import random

coin = random.randint (1, 2)

tries = 0
heads = 0
tails = 0

while tries != 100:

if coin == 1:
    { print ("Heads ")
    heads += 1
    tries += 1
    coin = random.randint(1, 2)

    elif coin == 2:
        print ("Tails ")
    tails += 1
    tries += 1
    coin = random.randint(1, 2)
    else:
    print ("WTF")

    }
    print ("Heads = ", heads)
    print ("Tails = ", tails)
else:
    pass