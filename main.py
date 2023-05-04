import random
card=[1,2,3,4,5,6,7,8,9,10,"K","Q","J","A"]

player_deck=[]
croupier_deck=[]





def get_card():
    for x in range(2):
        a = random.choice(card)
        b = random.choice(card)
        player_deck.append(a)
        croupier_deck.append(b)
def count_player():
    global  isplayerhavea,playernum
    isplayerhavea = False

    playernum=0

    for x in player_deck:
        a=x
        if (a=="A"):
            isplayerhavea=True

    if isplayerhavea==False:
        for x in player_deck:
            if x=="K" or x== "Q" or x=="J":
                playernum=playernum+10
            elif x=="A":
                playernum=playernum+1
            else:
                playernum=playernum+x
    return playernum

def count_croupier():
    global iscroupierhavea,courpiernum
    iscroupierhavea = False
    courpiernum = 0

    for x in croupier_deck:
        a=x
        if (a=="A"):
            iscroupierhavea=True

    if iscroupierhavea==False:
        for x in croupier_deck:
            if x=="K" or x== "Q" or x=="J":
                courpiernum=courpiernum+10
            elif x=="A":
                courpiernum=courpiernum+1
            else:
                courpiernum=courpiernum+x
    return courpiernum



def hit_cards(self):
    # if count_player()>21:
    #     print("You are busted out game over")
    #     choice="N"
    #     return

    a=random.choice(card)
    self.append(a)
    if self=="croupier_deck":
        print("asdkujbasıdba")

    #print(count_player())

    print(self)
    #count_player()




get_card()
count_player()


playnum=count_player()
count_croupier()


croupier_deck=["A",5]

print(f"Your Deck: {player_deck}")
# print(f"Courpier Deck: [{croupier_deck[0]}, *]")
print(f"corupier {croupier_deck}")

choice="N";

if count_player() != 21:
    choice=input("Dou you want to hit a card? (Y/N)" )



while choice=="Y"or choice=="y":
    hit_cards(player_deck)

    if count_player()>21:
        print("You are busted out game over")
        quit()
    elif count_player() == 21:
        break
    choice = input("Dou you want to hit a card? (Y/N)")

while count_croupier() >= 17:
    hit_cards(croupier_deck)
    if count_croupier()>21:
        print("You Won")
        quit()

if count_player()>count_croupier():
    print(croupier_deck)
    print("Conguraltions you won")
    quit()
elif count_croupier()>count_player():
    print(f"Courpier deck is {croupier_deck}")
    print("You lost")
    quit()
elif count_croupier()==count_player():
    print(f"Courpier deck is {croupier_deck}")
    print("Draw return chips")
    quit()