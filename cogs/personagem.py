class Character:
    def __init__(self, name, character_class, level=1):
        self.name = name
        self.character_class = character_class
        self.level = level
        self.profile = {'name': name, 'class': character_class, 'level': level}

    def level_up(self):
        self.level += 1
        self.profile['level'] = self.level

    def display_profile(self):
        return f"Name: {self.profile['name']}, Class: {self.profile['class']}, Level: {self.profile['level']}" 


# Example commands
if __name__ == '__main__':
    character1 = Character('Arthur', 'Knight')
    print(character1.display_profile()) 
    character1.level_up()
    print(character1.display_profile())