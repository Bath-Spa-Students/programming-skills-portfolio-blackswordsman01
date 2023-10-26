#Double decision structure
Lotterynumber = float(input("Enter lotterynumber :"))
prize = 0
if Lotterynumber > 30 :
    prize = "mercedes"
else:
    prize = 0
print("Your Prize : "+str(prize ) )

#Nested Decision structure
classmarks = int(input("Enter your classmarks :"))
externals = int(input("Enter your externals: "))
if classmarks > 70:
    if externals >=6:
        print("You're accepted into the academy")
    else:
        print("Your classmarks is not sufficient")
else:
    print("Your externals is not sufficient")

#elif statements
classpoints = float(input ("Enter your classpoints"))
if classpoints >= 100:
    print ("Your class is D")
elif classpoints >= 300:
    print ("Your class is C")
elif classpoints >= 500:
    print ("Your class is B")
elif classpoints >= 700:
    print ("Your class is A")
else :
    print ("You are expelled")
    