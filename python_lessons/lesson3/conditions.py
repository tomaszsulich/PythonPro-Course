# "\" łamie linię w kodzie
if 23785890988447657890567895698875673920175869023 > 89567908576648372892910185768932 and \
    True:
    print("dziala")

cond0 = 23785890988447657890567895698875673920175869023 > 89567908576648372892910185768932
cond1 = True is not False

if cond0 and cond1:
    print("dziala")


conditions = [True, False, True, False]

# NATRAFIŁ NA FALSE?
for cond in conditions:
    if not cond:
        print("niezdane")
        break
else:
    print("zdane")
    
# TO SAMO, ALE KRÓCEJ
if all(conditions):
    print("zdane")
else:
    print("niezdane")
    
# JEŻELI KTÓRYKOLWIEK TRUE, TO ZDANE
if any(conditions):
    print("zdane")
else:
    print("niezdane")

# JEŻELU KTÓRYKOLWIEK FALSE, TO NIEZDANE
if not any (conditions):
    print("zdane")
else:
    print("niezdane")