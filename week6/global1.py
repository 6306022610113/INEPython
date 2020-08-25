#This program simulates 10 tosses of a cion.
import random

HEADS = 1
TAILS = 2
TOSSES = 10
h = 0
t = 0
def main():
    global h
    global t
    for toss in range(TOSSES):
        #Simulate the coin toss.
        if random.randint(HEADS, TAILS) == HEADS:
            print("HEADS")
            h = h + 1
        else:
            print("TAILS")
            t = t + 1
        
    
    print("\nHEADS = ",h)
    print("TAILS = ",t)

#Call the main function.
main()