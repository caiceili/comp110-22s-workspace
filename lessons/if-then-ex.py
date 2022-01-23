"""Practice with if-then-else  statements"""

choice: int = int(input("Enter a number: "))

# Implement the logic to print
#A < 25
#B >= 25 and <50 
#C > 75
#D >= 50 and <= 75

if choice < 25:
        print("A")
else:        
    if choice < 50:
        print("B")
    else: 
        if choice <= 75
            print("D")
        else:
            print("C")