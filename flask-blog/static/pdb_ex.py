import sys
from random import choice
import pdb



random1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
random2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]



while True:
    print("To exit this game type exit")
    pdb.set_trace()
    answer = input("What is {} times {}? ".format(choice(random2), choice(random1)))

    # exit

    if answer == "exit":
        print("Now exiting game!")
        sys.exit()


    # determine if number is correct
    elif answer ==  choice(random2 * choice(random1)):
        print("correct!")

    else:
        print("Wrong!!!")


