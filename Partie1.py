import random

class Citation:
    def __init__(self):
        self.Citation = [
            "constructeur",
            "modele",
            "motorisation",
            "cylindrée"
        ]
       
    def show(self):
        citation = random.choice(list(self.Citation))
        print(citation)

citation = Citation()
citation = citation.show()
print ('ici')