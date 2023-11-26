# It works like switch case or map list in java. Preserve data in key : value

country = {1: "USA",2: "UK", 3: "France"}

for key, value in country.items():
    print(key, value)

print(country[2])
print(country.get(3))
print(country.keys())
print(country.values())
print(country.items())

country[1] = "The USA"

print(country.items())