# if-else staement about seasons

month = input("Enter a month: ").lower()

if month in ["december", "january", "february"]:
    season = "Winter"
elif month in ["march", "april", "may"]:
    season = "Spring"
elif month in ["june", "july", "august"]:
    season = "Summer"
elif month in ["september", "october", "november"]:
    season = "Fall"
else:
    season = "Invalid month"

print(f"The season for {month} is {season}")
