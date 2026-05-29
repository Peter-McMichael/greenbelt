from OOPdog import Dog
from OOPdog import Car


# defaultDog = Dog()
# defaultCar = Car()

Griffin = Dog("Griffin", "Golden Retriever", 4, "soft", "gold", "satiated", True)
# try:
#     Griffin.size = 3
#     Griffin.mood = "happy"
# except ValueError as error:
#     print("Error:", error)

print(Griffin.size)
Tofu = Dog("Tofu", "Pomeranian", 1, "soft", "white", "happy", True)
Phillip = Dog("Phillip", "Shiba Inu", 3, "medium", "tan", "calm", True)

# print(Griffin.name)
# print(defaultDog.size)

Griffin.mood = "satiated"

# print(Griffin.mood)

# print(defaultCar)
# print("______________________")
# Griffin.describeDog()
# print("______________________")
# defaultCar.describeCar()
#def __init__(self, brand = "Tesla", model = "X", color = "white", year = 2020, license = "XXXXXXXX", owner = "Me", fuel_type = "electric"):





Ferrari = Car("Ferrari", "F40", "Red", 1987, "F40ZRTUFF", "Elon Musk", "Gas")


# Ferrari.describeCar()