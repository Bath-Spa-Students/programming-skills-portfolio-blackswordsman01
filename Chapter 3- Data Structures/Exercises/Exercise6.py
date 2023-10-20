#Shrinking Guest List

#Inviting the first three
guests = ['Walter White', 'Thomas Shelby', 'Christopher Smith']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"\nSorry, {name} can't make it to dinner.")

#One of them can't make it! Let's invite another one instead.
del(guests[2])
guests.insert(2, 'Dominic Toretto')

#Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

#The table won't arrive on time
print("\nSorry, we can only invite two people to dinner.")
name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

#Inviting the other two
name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)