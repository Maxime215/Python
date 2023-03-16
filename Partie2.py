import json

class User:
    def __init__(self, prenom, age, genre):
        self.prenom = prenom
        self.age = age
        self.genre = genre

    def ConvertJson(self):
        return json.dumps(self.__dict__)

# création d'une instance de la classe user
user = User("Jean", 30, "masculin")

# Converti l'instance de la classe en objet JSON
jsonUser = user.ConvertJson()

# Affiche l'objet JSON dans le terminal
print(jsonUser)