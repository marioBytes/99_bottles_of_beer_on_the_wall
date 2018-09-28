bottles = 99 # Create a counter for the loop

# Create a loop that iterates through each verse of the song
# that counts from 99 to 1
for bottle in range(bottles, -1, -1):
    if bottle > 2: # If the number is greater than 2 make the verse plural
        print(bottle, "bottles of beer on the wall.", bottle, "bottles of beer. Take one down, pass it around,", bottle - 1, "bottles of beer on the wall.")
    elif bottle == 2: # If the number is equal to 2 make the latter half of the verse singular
        print(bottle, "bottles of beer on the wall.", bottle, "bottles of bear. Take one down, pass it around,", bottle - 1, "bottle of beer on the wall")
    elif bottle == 1: # If the number is equal to 1 make the verse singular.
       print(bottle, "bottle of beer on the wall", bottle, "bottle of beer. Take one down, pass it down pass it around. No more bottles of beer on the wall.") 
    else: # If the number is 0 then do nothing
        pass
    bottle -= 1 # Subtract one from the bottle counter each iteration
