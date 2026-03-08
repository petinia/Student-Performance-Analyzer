import json
import os
from models.student import Student

class DataManager:
    def __init__(self):
        self.students = []
        # Chemin vers ton fichier JSON dans le dossier data
        self.file_path = "data/student.json"
        
        # 1. On crée le dossier s'il n'existe pas
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        
        # 2. On charge les données dès l'ouverture
        self.load_from_json()

    def load_from_json(self):
        """Récupère les étudiants stockés dans le fichier JSON au démarrage"""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    # On transforme les dictionnaires JSON en objets Student
                    self.students = [Student(s['name'], s['maths'], s['anglais'], s['informatique']) for s in data]
            except (json.JSONDecodeError, Exception):
                self.students = []

    def save_to_json(self):
        """Enregistre la liste actuelle des étudiants dans le fichier JSON"""
        data_to_save = []
        for s in self.students:
            data_to_save.append({
                "name": s.name,
                "maths": s.maths,
                "anglais": s.anglais,
                "informatique": s.informatique
            })
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, indent=4, ensure_ascii=False)

    def add_student(self, name, maths, anglais, info):
        new_student = Student(name, float(maths), float(anglais), float(info))
        self.students.append(new_student)
        self.save_to_json() # Sauvegarde automatique sur le disque
        return new_student

    def remove_student(self, index):
        """Suppression avec mise à jour du fichier"""
        if 0 <= index < len(self.students):
            self.students.pop(index)
            self.save_to_json() # Sauvegarde automatique

    def update_student(self, index, name, maths, anglais, info):
        """Modification avec mise à jour du fichier"""
        if 0 <= index < len(self.students):
            s = self.students[index]
            s.name = name
            s.maths = float(maths)
            s.anglais = float(anglais)
            s.informatique = float(info)
            self.save_to_json() # Sauvegarde automatique

    def get_students(self):
        return self.students

    # --- ANALYSES ---
    def class_average(self):
        if not self.students: return 0
        return sum(s.calculate_average() for s in self.students) / len(self.students)

    def get_extremes(self):
        if not self.students: return {}
        avgs = [s.calculate_average() for s in self.students]
        max_avg, min_avg = max(avgs), min(avgs)
        return {
            "best": [s.name for s in self.students if s.calculate_average() == max_avg],
            "worst": [s.name for s in self.students if s.calculate_average() == min_avg],
            "max_val": max_avg, "min_val": min_avg
        }

    def get_subject_analysis(self):
        if not self.students: return {}
        subjects = ["maths", "anglais", "informatique"]
        results = {}
        for sub in subjects:
            notes = [getattr(s, sub) for s in self.students]
            m, v = max(notes), min(notes)
            results[sub] = {
                "top": [s.name for s in self.students if getattr(s, sub) == m],
                "low": [s.name for s in self.students if getattr(s, sub) == v],
                "m": m, "v": v
            }
        return results