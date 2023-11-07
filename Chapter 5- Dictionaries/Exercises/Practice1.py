# Dictionary about myself
myself = {
    "name": "Seth Hamilton",
    "age": 30,
    "location": "New Orleans, USA",
    "occupation": "Chef",
    "hobbies": ["Cooking", "Racing", "Investigating"],
    "email": "sethhamilton@gmail.com",
    "social_media": {
        "instagram": "sethhamilton123"
    }
}

print("Name:", myself["name"])
print("Age:", myself["age"])
print("Location:", myself["location"])
print("Occupation:", myself["occupation"])
print("Hobbies:", ", ".join(myself["hobbies"]))
print("Email:", myself["email"])
print("Social Media:")
for platform, handle in myself["social_media"].items():
    print(f"{platform}: {handle}")
