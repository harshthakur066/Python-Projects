import string
import random
import sys


N = int(input("Enter size of string --> "))

counter = int(input("How many password combinations do you need! --> "))

choice = input("Obsfucate the passcode? [Y/n] ")

savef = input("Do you want to save the file? [Y/n]")

if choice == 'n':
    obs = False
else:
    obs = True


def run(N):

    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits + string.ascii_lowercase + string.punctuation, k=N))
    if obs:
        res = res.replace('a', '4').replace('e', '3').replace('i', '!').replace(
            'l', '1').replace('t', '7').replace('s', '$').replace('o', '0')
    else:
        pass
    return res


def output():
    if savef == 'n':
        print("The generated random string : " + str(run(N)))
    else:
        sys.stdout = open('pw.txt', 'wt')
        with open('pw.txt', mode='r+') as file:
            file.write('The generated random string :')
            for i in range(counter):
                file.write('\n' + str(run(N)))


try:
    for i in range(counter):
        output()
except:
    print('Something went wrong')

finally:
    print('Done')
