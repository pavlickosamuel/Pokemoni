import json
#budu dva typy jedno-typový a dvoj-typový

attack = {}
fr = open("effectiveness.json", "r")
data = json.load(fr)

helper = {"super effective": 2, "normal effective": 1, "not very effective": 0.5, "no effect": 0}

for strenght in data:
    for attacker in data[strenght]:
        if attacker not in attack.keys():
            attack[attacker] = {}
        for defender in data[strenght][attacker]:
            attack[attacker][defender] = helper[strenght]

print(attack)






