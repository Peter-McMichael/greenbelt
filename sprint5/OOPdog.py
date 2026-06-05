class Dog:
    def __init__(
            self,
            name = "dog",
            breed = "NA",
            size = 1,
            fur_type = "N/A",
            fur_color = "N/A",
            mood = "N/A",
            has_owner = False,
            ):
        self.name = name
        self.breed = breed
        self.size = size
        self.fur_type = fur_type
        self.fur_color = fur_color
        self.mood = mood
        self.has_owner = has_owner

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, new_size):
        if type(new_size) != int:
            raise ValueError("Dog size must be an integer.")
        if new_size < 1 or new_size > 5:
            raise ValueError("Dog size must be between 1 and 5.")
        self._size = new_size

    @property
    def fur_type(self):
        return self._fur_type
    @fur_type.setter
    def fur_type(self, new_fur_type):
        fur_types = ["soft", "medium", "rough"]
        if new_fur_type not in fur_types:
            raise ValueError("Not a valid fur type.")
        else:
            self._fur_type = new_fur_type


    @property 
    def fur_color(self):
        return self._fur_color
    
    @fur_color.setter
    def fur_color(self, new_fur_color):
        fur_colors = ["gold", "white", "tan"]
        if new_fur_color not in fur_colors:
            raise ValueError("Not a valid fur color.")
        self._fur_color = new_fur_color

    @property
    def mood(self):
        return self._mood
    
    @mood.setter
    def mood(self, new_mood):
        moods = ["hungry", "happy", "calm", "satiated"]
        if new_mood not in moods:
            raise ValueError("Not a valid mood")
        self._mood = new_mood

    def describeDog(self):
        print(f"Dog name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"size: {self.size}")
        print(f"fur type: {self.fur_type}")
        print(f"fur color: {self.fur_color}")
        print(f"mood: {self.mood}")
        print(f"has owner?: {self.has_owner}")

class Car:
    def __init__(self, brand = "Tesla", model = "X", color = "white", year = 2020, license = "XXXXXXXX", owner = "Me", fuel_type = "electric"):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.license = license
        self.owner = owner
        self.fuel_type = fuel_type
    def describeCar(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"year: {self.year}")
        print(f"License: {self.license}")
        print(f"Owner: {self.owner}")
        print(f"Fuel type: {self.fuel_type}")
