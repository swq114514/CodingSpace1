from petsystem_v2 import *
# this is a joke
# if you hate it, then remove this file
# :D

DoLoveHandler0 = Dog("_DoLoveHandler0",0,0) # not required if you don't need to use do_love function
DoLoveHandler1 = Dog("_DoLoveHandler1",0,1) # not required if you don't need to use do_love function
DoLoveHandler0.health, DoLoveHandler0.hunger = 114514,1919810 # not required if you don't need to use do_love function
DoLoveHandler1.health, DoLoveHandler1.hunger = 114514,1919810 # not required if you don't need to use do_love function
PetKillHandler = Dog("_PetKillHandler",0,0)
Dog1 = Dog("Dog1",5,0)
Dog2 = Dog("Dog2",4,1)
Dog1.health = 114514
Dog2.health = 1919810
PetKillHandler.health = 1145141919810

Gift = Shit
Dog1.eat(Gift)
Gift = Shit
Dog2.eat(Gift)
Dog3 = DoLoveHandler0.do_love(male="Dog2",female="Dog1",baby_name="Dog3") # petsystem v2 only
Dog3.bark()

Dogs = [None]*10
for i in range(10): Dogs[i] = DoLoveHandler0.do_love(male="Dog2",female="Dog1",baby_name=f"DogA{i}")
    
MoreDogs = [None]*1000
for i in range(1000): MoreDogs[i] = DoLoveHandler0.do_love(male="Dog2",female="Dog1",baby_name=f"DogB{i}")

EvenMoreDogs1 = [None]*10000
for i in range(10000): EvenMoreDogs1[i] = DoLoveHandler0.do_love(male="Dog2",female="Dog2",baby_name=f"DogC{i}") # bug: single dog (even male) can make babies

Dog1.health = 1145141919810
Dog2.health = 1145141919810
Dog1.hunger = 1145141919810
Dog2.hunger = 1145141919810

EvenMoreDogs2 = [None]*10000
for i in range(10000): EvenMoreDogs2[i] = DoLoveHandler0.do_love(male="Dog3",female="Dog1",baby_name=f"DogD{i}") # bug: make babies between Dog3 and its mother (even baby is normal, no attribute set)

for Victim in EvenMoreDogs1: PetKillHandler.eat(Victim)
for Victim in EvenMoreDogs2: PetKillHandler.eat(Victim)
for Victim in MoreDogs: PetKillHandler.eat(Victim)
for Victim in Dogs: PetKillHandler.eat(Victim)
PetKillHandler.eat(Dog3)
PetKillHandler.eat(Dog2)
PetKillHandler.eat(Dog1)
PetKillHandler.eat(DoLoveHandler0)
PetKillHandler.eat(DoLoveHandler1)
PetKillHandler.kill()
# All pet has died
