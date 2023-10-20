#Changing Guest List

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