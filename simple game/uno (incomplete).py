import random as rd

# from 0 to 9 are normal cards, 10 represents skip, 11 => reverse, 12 => +2, 13 => +4, 14=> wild
deck = {
    'r': [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,'s','s','r','r','+2','+2'],
    'g': [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,'s','s','r','r','+2','+2'],
    'b': [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,'s','s','r','r','+2','+2'],
    'y': [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,'s','s','r','r','+2','+2'],
    'w': ['wild','wild','+4','+4','+4','+4']
}

# this take function gives a card to a player from deck
# x represents the category in which user gets the card
# 0 represents player gets a card from red color
# 1 => green,  2 => blue,  3 => yellow
# 4 represents player gets a wild card, i.e., normal wild card or +4
def take(p):
    global deck
    no_card_avail = len(deck['r']) + len(deck['g']) + len(deck['b']) + len(deck['y']) + len(deck['w'])
    prob_getting_card = [len(deck['r']), len(deck['g']), len(deck['b']), len(deck['y']), len(deck['w'])]
    for i in range(5):
        prob_getting_card[i] = prob_getting_card[i]/no_card_avail*100
    print(prob_getting_card)
    list = ['r','g','b','y','w']
    x = 0
    while(x == 0):
        x = rd.choices(list,weights=prob_getting_card,k=1)
        # x = rd.choices(list,weights=[23,23,23,23,8],k=1)
        x = x[0]
        if len(deck[x]) == 0: 
            list.remove(x)
            x = 0
    
    if(x == 'r'):
        m = rd.choice(deck[x])    # here we choose a card from deck currently presents at that category
        deck[x].remove(m)         # then remove that card from the deck
        p[x].append(m)            # also append that card into player's list
    
    elif(x == 'g'):
        m = rd.choice(deck[x])
        deck[x].remove(m)
        p[x].append(m)
    
    elif(x == 'b'):
        m = rd.choice(deck[x])
        deck[x].remove(m)
        p[x].append(m)

    elif(x == 'y'):
        m = rd.choice(deck[x])
        deck[x].remove(m)
        p[x].append(m)

    else:
        m = rd.choice(deck[x])
        deck[x].remove(m)
        p[x].append(m)
    

def show_dict(d):
    for x in d:
        print(f'{x}: {d[x]}')
    print("\n\n")


no_player = int(input("\nEnter no of opponents(1-3): ")) + 1

while(no_player>7 or no_player<2):
    print("No of opponent must be in between 1 and 3")
    no_player = int(input("\nEnter no of opponents(1-3): ")) + 1

# this is the position of user in the player's list
pos_user = rd.randrange(0,no_player)

# this is the dictionary of player's cards at this time
dict_players = dict()

# each player can hold red, green, blue, yellow or wild card
for i in range(no_player):
    if i == pos_user:
        dict_players['U'] = {'r': [], 'g': [], 'b': [], 'y': [], 'w': []}
    else:
        dict_players[i] = {'r': [], 'g': [], 'b': [], 'y': [], 'w': []}


show_dict(deck)
show_dict(dict_players)

for i in range(7):
    for player in dict_players:
        take(dict_players[player])


show_dict(dict_players)
show_dict(deck)


while(True):
    x = int(input("\nEnter: "))
    if x == 0:
        break
    take(dict_players['U'])
    show_dict(dict_players)