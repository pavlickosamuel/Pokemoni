import json
#budu dva typy jedno-typový a dvoj-typový

attackfield = {}
fr = open("effectiveness.json", "r")
data = json.load(fr)

helper = {"super effective": 2, "normal effective": 1, "not very effective": 0.5, "no effect": 0}

for strenght in data:
    for attacker in data[strenght]:
        if attacker not in attackfield.keys():
            attackfield[attacker] = {}
        for defender in data[strenght][attacker]:
            attackfield[attacker][defender] = helper[strenght]

#print(attackfield)
#print(attackfield["Fire"]["Psychic"])

def attack(P1:int, P2:int, army:str) -> str:
    temp = army.split(",")
    print(temp)
    army1 = temp[:P1]
    army2 = temp[P1:]
    print(army1,army2)

print(attack(2,6,"Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug"))
    
