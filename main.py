from random import randint

def find_num():
    tries = 0
    comp_num = randint(1,10)
    
    while tries < 6:
        num = int(input("Gues the number from 1 to 50: "))
        
        tries += 1 
        
        if num > comp_num:
            print("The number is high")
        elif num < comp_num:
            print("The number is low")
        else:
            print({
                "massage": "Congrats! You guessed the number!",
                "tries": {tries},
                "number": {num}                
            })
            break


# 10STICKS
def sticks(st):
    turn = 1
    s=st
    
    while s > 0:
        n = 0
        while n > 3 or n < 1:
            n = int(input("enter the number from (1,2,3): "))

        print(st)        
        s -= n
        
        print(f"Player{turn}: {s}")
        
        if turn == 1:
            turn = 2
        else:
            turn = 1

    print(f"Player{turn} is lose")
    

# find_num()
sticks(10)

