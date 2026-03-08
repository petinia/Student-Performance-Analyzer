class Analysis:

    @staticmethod
    def calculate_average(student):
        return (
            student.maths +
            student.anglais +
            student.informatique
        ) / 3


    @staticmethod
    def get_mention(average):
        if average >= 16:
            return "Très Bien"
        elif average >= 14:
            return "Bien"
        elif average >= 12:
            return "Assez Bien"
        elif average >= 10:
            return "Passable"
        else:
            return "Ajourné"


    # ----------------------------
    # Analyse globale
    # ----------------------------

    @staticmethod
    def best_student(students):
        if not students:
            return None
        return max(students, key=lambda s: Analysis.calculate_average(s))


    @staticmethod
    def worst_student(students):
        if not students:
            return None
        return min(students, key=lambda s: Analysis.calculate_average(s))


    # ----------------------------
    # Analyse par matière
    # ----------------------------

    @staticmethod
    def best_math(students):
        if not students:
            return None
        return max(students, key=lambda s: s.maths)


    @staticmethod
    def worst_math(students):
        if not students:
            return None
        return min(students, key=lambda s: s.maths)


    @staticmethod
    def best_english(students):
        if not students:
            return None
        return max(students, key=lambda s: s.anglais)


    @staticmethod
    def worst_english(students):
        if not students:
            return None
        return min(students, key=lambda s: s.anglais)


    @staticmethod
    def best_computer(students):
        if not students:
            return None
        return max(students, key=lambda s: s.informatique)


    @staticmethod
    def worst_computer(students):
        if not students:
            return None
        return min(students, key=lambda s: s.informatique)


    # ----------------------------
    # Moyennes par matière
    # ----------------------------

    @staticmethod
    def average_math(students):
        if not students:
            return 0

        total = 0
        for student in students:
            total += student.maths

        return total / len(students)


    @staticmethod
    def average_english(students):
        if not students:
            return 0

        total = 0
        for student in students:
            total += student.anglais

        return total / len(students)


    @staticmethod
    def average_computer(students):
        if not students:
            return 0

        total = 0
        for student in students:
            total += student.informatique

        return total / len(students)