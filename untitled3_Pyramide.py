getal = int(input("Voer in getal: "))

for var in range (int(getal)+1):
    print("*"*var)
for var in range (int(getal)-1,0,-1):
    print("*"* var)

var = getal
totvar = var+1
while var != 0:
    calc = totvar - var
    print("*"* calc)
    var += -1

var = getal
totvar = var
while var != 0:
    print("*"* var)
    var += -1

