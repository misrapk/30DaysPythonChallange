## COIN SWITCH APPLICATION
import random

print("WELCOME TO COIN TOSS GAME!")

n = int(input("How many times would you like to Toss the Coin? "))

choice = input("Do you want to see each toss?(y/n)")

head = 0
tails = 0

for toss in range(n):
    coin = random.randint(0,1)   #0 - head 1 - Tail
    
    if coin == 0:
        head += 1
        if choice == 'y':
            print("HEAD")
    else:
        tails +=1
        if choice == 'y':
            print("TAILS")
            
            
    if head==tails:
        print(f"At {toss +1} flips. The number of head and tails are equal: {head} each")
        
    
#percentage
headPercentage = round((head/n)*100, 2)
tailsPercentage = round((tails/n)*100, 2)

print(f"Summary of Tosses after {n} flips!\n")
print(f"Side\t Count\t Percentage")

print(f"Heads\t {head}/{n}\t {headPercentage}%")
print(f"Tails\t {tails}/{n}\t {tailsPercentage}%")