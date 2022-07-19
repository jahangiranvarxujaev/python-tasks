animals = {"cow": "brown"}

animals["dog"] = "black"
cities = {
         "England": {
                    "Counrty": "Manchester",
                    "Population": "15000",
                    "Fact": "Football town",
                    },
         "France": {
                  "Counrty": "Paris",
                  "Population": "35000",
                  "Fact": "Touristic town",
                   },
         "Uzbekistan": {
                      "Counrty": "Tashkent",
                      "Population": "45000",
                      "Fact": "Town without internet",
                       },
         }


numbers = [1, 2, 3]
classes = ["one", "two", "three"]

class_numbers = dict(zip(numbers, classes))
class_numbers[1] = "hello"
print(class_numbers)

print(class_numbers.get(10, "sd"))


for city, info in cities.items():
    print("City -", city)
    for key, value in info.items():
        print(key + " " + value)
