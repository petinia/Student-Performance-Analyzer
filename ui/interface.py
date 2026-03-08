import tkinter as tk
from tkinter import ttk, messagebox

class App:
    def __init__(self, root, data_manager):
        self.root = root
        self.data_manager = data_manager
        self.root.title("Student Performance Analyzer")
        self.root.geometry("1100x850")
        
        # --- ON NE TOUCHE PAS AU DESIGN ---
        self.bg_color = "#0f172a"
        self.card_color = "#1e293b"
        self.accent_color = "#3b82f6"
        self.root.configure(bg=self.bg_color)

        # TITRE CENTRÉ
        tk.Label(self.root, text="Student Performance Analyzer", font=("Helvetica", 32, "bold"), 
                 bg=self.bg_color, fg="white", pady=40).pack()

        # STYLE DES ONGLETS
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TNotebook", background=self.bg_color, borderwidth=0)
        style.configure("TNotebook.Tab", background=self.card_color, foreground="white", 
                        padding=[20, 8], font=("Helvetica", 10, "bold"), borderwidth=0)
        style.map("TNotebook.Tab", background=[("selected", self.accent_color)])

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=30, pady=10)

        self.tab_gestion = tk.Frame(self.notebook, bg=self.bg_color)
        self.tab_analyse_etud = tk.Frame(self.notebook, bg=self.bg_color)
        self.tab_analyse_mat = tk.Frame(self.notebook, bg=self.bg_color)

        self.notebook.add(self.tab_gestion, text=" GESTION ")
        self.notebook.add(self.tab_analyse_etud, text=" ANALYSE ÉTUDIANTS ")
        self.notebook.add(self.tab_analyse_mat, text=" ANALYSE MATIÈRES ")

        self.setup_gestion()
        self.setup_analyse_etud()
        self.setup_analyse_mat()

        # --- SEULE MODIFICATION : CHARGEMENT AUTO AU DÉMARRAGE ---
        self.refresh_ui()

    def setup_gestion(self):
        container = tk.Frame(self.tab_gestion, bg=self.bg_color)
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # BLOC SAISIE
        form_card = tk.Frame(container, bg=self.card_color, padx=30, pady=20)
        form_card.pack(side="left", fill="y", padx=10)

        tk.Label(form_card, text="INFORMATIONS ÉTUDIANT", font=("Helvetica", 11, "bold"), 
                 bg=self.card_color, fg=self.accent_color).pack(pady=(0, 15))

        self.entries = {}
        for field in ["Nom", "Maths", "Anglais", "Informatique"]:
            tk.Label(form_card, text=field, bg=self.card_color, fg="white").pack(anchor="w")
            e = tk.Entry(form_card, font=("Helvetica", 12), bg="#334155", fg="white", borderwidth=0, insertbackground="white")
            e.pack(fill="x", pady=(2, 10), ipady=8)
            self.entries[field] = e

        # BOUTONS
        tk.Button(form_card, text="AJOUTER", bg=self.accent_color, fg="white", font=("Helvetica", 10, "bold"), 
                  bd=0, cursor="hand2", command=self.add_student_logic).pack(fill="x", pady=5, ipady=8)

        tk.Button(form_card, text="MODIFIER", bg="#10b981", fg="white", font=("Helvetica", 10, "bold"), 
                  bd=0, cursor="hand2", command=self.edit_student_logic).pack(fill="x", pady=5, ipady=8)

        tk.Button(form_card, text="SUPPRIMER", bg="#ef4444", fg="white", font=("Helvetica", 10, "bold"), 
                  bd=0, cursor="hand2", command=self.delete_student_logic).pack(fill="x", pady=5, ipady=8)

        # BLOC LISTE
        list_card = tk.Frame(container, bg=self.card_color, padx=20, pady=20)
        list_card.pack(side="right", fill="both", expand=True, padx=10)

        self.listbox = tk.Listbox(list_card, bg=self.card_color, fg="white", font=("Helvetica", 11), 
                                  borderwidth=0, highlightthickness=0, selectbackground=self.accent_color)
        self.listbox.pack(fill="both", expand=True)
        self.listbox.bind('<<ListboxSelect>>', self.load_student_to_form)

    def setup_analyse_etud(self):
        self.lbl_etud = tk.Label(self.tab_analyse_etud, text="En attente de données...", bg=self.bg_color, fg="white", font=("Helvetica", 14), pady=100)
        self.lbl_etud.pack(fill="x")

    def setup_analyse_mat(self):
        self.lbl_mat = tk.Label(self.tab_analyse_mat, text="En attente de données...", bg=self.bg_color, fg="white", font=("Courier New", 12), pady=100)
        self.lbl_mat.pack(fill="x")

    def load_student_to_form(self, event):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            student = self.data_manager.get_students()[index]
            self.entries["Nom"].delete(0, tk.END); self.entries["Nom"].insert(0, student.name)
            self.entries["Maths"].delete(0, tk.END); self.entries["Maths"].insert(0, student.maths)
            self.entries["Anglais"].delete(0, tk.END); self.entries["Anglais"].insert(0, student.anglais)
            self.entries["Informatique"].delete(0, tk.END); self.entries["Informatique"].insert(0, student.informatique)

    def add_student_logic(self):
        try:
            self.data_manager.add_student(self.entries["Nom"].get(), self.entries["Maths"].get(), self.entries["Anglais"].get(), self.entries["Informatique"].get())
            self.refresh_ui()
            # On vide les champs après l'ajout
            for entry in self.entries.values(): entry.delete(0, tk.END)
        except: messagebox.showerror("Erreur", "Vérifiez vos notes")

    def edit_student_logic(self):
        selected = self.listbox.curselection()
        if selected:
            try:
                self.data_manager.update_student(selected[0], self.entries["Nom"].get(), self.entries["Maths"].get(), self.entries["Anglais"].get(), self.entries["Informatique"].get())
                self.refresh_ui()
                for entry in self.entries.values(): entry.delete(0, tk.END)
            except: messagebox.showerror("Erreur", "Modification impossible")

    def delete_student_logic(self):
        selected = self.listbox.curselection()
        if selected:
            self.data_manager.remove_student(selected[0])
            self.refresh_ui()
            for entry in self.entries.values(): entry.delete(0, tk.END)

    def refresh_ui(self):
        """Met à jour la liste et les statistiques sans vider les champs de saisie forcément"""
        # On rafraîchit la Listbox
        self.listbox.delete(0, tk.END)
        for s in self.data_manager.get_students():
            self.listbox.insert(tk.END, f"  {s.name.upper()}  -  Moyenne: {s.calculate_average():.2f}")
        # On rafraîchit les stats
        self.update_stats()

    def update_stats(self):
        ext = self.data_manager.get_extremes()
        if ext and self.data_manager.get_students():
            self.lbl_etud.config(text=f"MOYENNE CLASSE : {self.data_manager.class_average():.2f}\n\nTOP : {', '.join(ext['best'])}\nBAS : {', '.join(ext['worst'])}")
            
            mats = self.data_manager.get_subject_analysis()
            if mats:
                res = ""
                for k, v in mats.items(): 
                    res += f"{k.upper()} : Top {v['m']} ({', '.join(v['top'])}) / Bas {v['v']} ({', '.join(v['low'])})\n\n"
                self.lbl_mat.config(text=res)
        else:
            self.lbl_etud.config(text="En attente de données...")
            self.lbl_mat.config(text="En attente de données...")