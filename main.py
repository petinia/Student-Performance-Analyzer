import tkinter as tk
from ui.interface import App
from services.data_manager import DataManager

def main():
    # 1. Création de la fenêtre principale (le 'root')
    root = tk.Tk()
    
    # 2. Initialisation du gestionnaire de données
    data_manager = DataManager()
    
    # 3. Lancement de l'application en lui passant les arguments manquants
    app = App(root, data_manager)
    
    # 4. Boucle infinie pour maintenir la fenêtre ouverte
    root.mainloop()

if __name__ == "__main__":
    main()