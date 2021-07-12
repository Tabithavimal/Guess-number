title="Number Guessing Game"
print(title)

input=int(input("Guess a number between 1 to 8"))
print(input)

if(input>5):
    print("Your guess was too low:Guess a number higher than 3")

elif(input<8):
    print("Congratulations YOU WIN")

count=9
while(count>=0):
    print(count)
    count=count+1