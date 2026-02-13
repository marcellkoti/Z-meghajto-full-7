#Írjuk ki 5ször hogy "hello world"
#for cv in range(kezdő,záróérték-1,léptetés)
#művelet
for _ in range(5):
    print("Hello World")
#Írja ki az első 10 számot
for i in range(1,11):
    print(i,end='\t')
print(" ")    
#Írjuk ki 50-5 ig
for i in range(50,5,-1):
    print(i,end='\t')
print(" ") 

for i in range(50,5,-5):
    print(i,end='\t')
    print(" ")
gyümölcsök=['alma','körte','dió','cseri','mangó']
for gyümi in gyümölcsök:
    print(gyümi,end='\t')
    print(" ")
#elöltesztelő ciklus
#while feltétel:
#   művelet
#Kérjünk be 50-nél nagyobb számot!
szam=int(input("Kérek egy 50-nél nagyobb számot!"))
while szam<=50 or szam>=100:
    print("Hibás számot adtál meg")
    szam=int(input("Kérek egy 50-nél nagyobb számot"))
print("Hurrá!, Ügyes vagy!!, A szám a(z)",szam)
#Random generátor
import random
for _ in range (10):
    print(random.random()) #0 és 1 között
    print(random.randint(100,201))
