a=int(input("Kérek egy számot"))
b=int(input("Kérek egy másik számot"))
#egyirányú elágazás
    #Amikor a felhasználó 10-nél nagyobb számot ad meg,
    #abből vegyünk le 5-öt
if a>10:
    a=a-5 # a-=5

#kétirányú elágazás
    #A MÁSODIK SZÁM PÁROS-E AVAGY PÁRATLAN?
if b%2==0:
    print("páros")
else:
    print("páratlan")
#többirányű elágazás különböző feltétel alapján
    #A megadott két szám egyenlő, vagy melyika nagyobb?
if a==b:
    print("A két szám egyenlő")
elif a>b:
    print("Nagyobb",a)
else:
    print("Nagyobb",b)
#többirányú elágazás változó értéke alapján
jegy=(input("Hányast kaptál??"))
match jegy:
    case '1': print("elégtelen")
    case '2': print("elégséges")
    case '3': print("közepes")
    case '4': print("jó")
    case '5': print("jeles")
    case _:print("Ilyen jegy magyar honba nem létezik!") 
