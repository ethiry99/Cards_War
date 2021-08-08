
from random import seed
from random import randint

deck=[]
ranks = ["deuce", "three", "four", "five", "six","seven","eight","nine","ten","jack","queen","king","ace"] 
suits = ["hearts", "diamonds", "spades","clubs"]
random = []
for suit in suits:
    for rank in ranks:
        deck.append({
            'suit':suit,
            'rank':rank
            'random':randint(0,1000000)
        })
print(deck)
print('sanity check length:',len(suits)* len(ranks)== len(deck))
print(len(deck))
free=True
def shuffle (unshuffled):
    temp= list(unshuffled)
    bound=True
    #for each card : giving
    print('free is free inside:' ,free)
    return temp
shuffled=shuffle(deck)
#compare shuffled to dek
print('free is free outside:' ,free)
try:    
    print(bound)
except NameError as e:
    print('bound is still bound',e)
print(returned)