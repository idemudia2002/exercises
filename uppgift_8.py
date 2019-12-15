def contains(list, city):
    return city in list

cities = ["Stockholm", "Tokyo", "New York", "Berlin"]

write = input("type a city ")

print(contains(cities, write))