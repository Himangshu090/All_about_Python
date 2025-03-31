from random import shuffle
"""list = [1,2,3,4,5,6,7,8,9]

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result= shuffle_list(list)
print(result)"""


my_list = ['','O','']

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

shuffle_list(my_list)

def player_guess():

    guess = ""
    while guess not in ['0','1','2']:
        guess = input("Enter a index among 0,1,2 :")
        return int(guess)
    
def check_guess(my_list,guess):
    if(my_list[guess] == 'O'):
        print("Correct guess")
        print(my_list)
    else:
        print("Wrong answer better luck next time")    
        print(my_list)

#Initalization

my_list = ['','','O']

#shuffling the list
shuffling = shuffle_list(my_list)

#users guess
guess = player_guess()

#check guess

check_guess(shuffling,guess)
    


