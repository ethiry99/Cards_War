queen_of_hearts = {
    'suit':'hearts',
    'rank': 'queen'
}
deck=[]
ranks = [
    {"name":"predator",
'power': 9001,
'succumbs_to': "ceos"
},
"kings", "queens", "presidents", "ceos", "aliens"] #len(x)
suits = ["black", "brown", "double-breasted"]
for suit in suits:
    for rank in ranks:
        deck.append({
            'suit':suit,
            'rank':rank
        })
print(deck)
print('sanity check length:',len(suits)* len(ranks)== len(deck))
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