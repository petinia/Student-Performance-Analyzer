class Student:
    def __init__(self, name, maths, anglais, informatique):
        self.name = name
        self.maths = float(maths)
        self.anglais = float(anglais)
        self.informatique = float(informatique)

    def calculate_average(self):
        return (self.maths + self.anglais + self.informatique) / 3