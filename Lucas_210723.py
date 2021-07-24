print("question 2")
lig=[]
for a in range(2):
    dc=input("user give me a number: ")
    print(dc)
    lig.append(int(dc))
print("question 3")
lgs=lig[0]+lig[1]
print(str(lig[0])+" + "+str(lig[1])+" = "+str(lgs))
print("question 4")
dili=[]
for suls in range(3):
    sia=input("user write a name of some people: ")
    ais=input("user write the age from this people: ")
    print(sia)
    print(ais)
    bip={sia:ais}
    dili.append(bip)
print("question 5")
for supes in dili:
    print(supes)
print("question 6")
nfu=input("What is your name? ")
byu=input("What year were you born? ")
uam=input("Did you have your birthday already? ")
print(nfu)
print(byu)
print(uam)
for poq in range(1):
    if uam.lower() == "yes":
        aup=2021-int(byu)
    elif uam.lower() == "no":
        aup=2020-int(byu)
print("Hi "+nfu+"! you are "+str(aup)+" years old.")


