import random
tries = 0
sample_space = {'Heads', 'Tails'}
print(sample_space)
while tries < 1:
    tries += 1
    coin = random.randint(1, 2)
    if coin == 1:
        print('Heads')
    if coin == 2:
        print ('Tails')
total = tries

C:\Users\user\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/user/PycharmProjects/pythonProject/assignment2.1.py
{'Tails', 'Heads'}
Heads

C:\Users\user\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/user/PycharmProjects/pythonProject/assignment2.1.py
{'Heads', 'Tails'}
Heads

Process finished with exit code 0
