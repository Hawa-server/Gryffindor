"""
create a custom function that will check for parity.
to determine if a number is even or odd.
"""
def parity():
    number = 2
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

parity()        
