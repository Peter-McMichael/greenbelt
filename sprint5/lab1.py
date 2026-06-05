
verified_skills = ["dodge", "speed", "strength", "parry", "intelligence", "magic", "regeneration", "accuracy", "dexterity", "cunning", "swift", "percission", "luck", "stealthy"] 

class VideoGameCharacter:
    def __init__ (self, name = "Player", level = 1, health = 100, skills = ["speed", "strength"], item_capacity = 10, position = (0, 0, 0)):
        self.name = name
        self.level = level
        self.health = health
        self.skills = skills
        self.item_capacity = item_capacity
        self.position = position

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) > 20 or len(new_name) < 1:
                raise ValueError("Name must be between 1 and 20 characters.")
        if type(new_name) != str:
            raise ValueError("Name must be a string.")
        self._name = new_name
        
    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, new_level):
        if type(new_level) != int:
            raise ValueError("The level must be an integer.")
        if new_level < 1:
            raise ValueError("The level must be greater than zero.")
        self._level = new_level
        
    @property 
    def health(self):
        return self._health
    @health.setter
    def health(self, new_health):
        if type(new_health) != int:
            raise ValueError("Health must be an integer.")
        if new_health < 0 or new_health > 100:
            raise ValueError("Health must be between 0 and 100.")
        self._health = new_health
    @property
    def skills(self):
        return self._skills
    @skills.setter
    def skills(self, new_skills):
        if type(new_skills) != list:
            raise ValueError("Skills must be a list.")
        if len(new_skills) > 5:
            raise ValueError("Max Skills cap reached.")
        for i in new_skills:
            if i not in verified_skills:
                raise ValueError("This is not a valid skill.")
            else:
                continue
        self._skills = new_skills.copy()

    @property 
    def item_capacity(self):
        return self._item_capacity
    @item_capacity.setter
    def item_capacity(self, new_item_capacity):
        if type(new_item_capacity) != int:
            raise ValueError("Item capacity must be an integer.")
        if new_item_capacity < 1 or new_item_capacity > 20:
            raise ValueError("Item capacity must be between 1 and 20.")
        self._item_capacity = new_item_capacity

    @property
    def position(self):
        return self._position
    @position.setter
    def position(self, new_position):
        if type(new_position) != tuple and type(new_position) != list:    
            raise ValueError("Position must be a tuple or list.")
        if len(new_position) != 3:
            raise ValueError("Position must have three coordinates.")
        x = new_position[0]
        y = new_position[1]
        z = new_position[2]
        if type(x) != int or type(y) != int or type(z) != int:
            raise ValueError("All three coordinates must be integers.")
        self._position = (x, y, z)
        
    def describeCharacter(self):
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Skills: {self.skills}")
        print(f"Item Capacity: {self.item_capacity}")
        print(f"Position: {self.position}")


steve = VideoGameCharacter("Steve", 67, 67, ["luck", "regeneration", "cunning"], 5, (67, 67, 67))
steve.health=10
steve.position = (10, 5)
steve.describeCharacter()

            



            
            
        
        
            

