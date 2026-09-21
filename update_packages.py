import os

files_to_update = ["index.html", "llms.txt"]

for file_path in files_to_update:
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace packages
        content = content.replace("Básico (S/ 300)", "Inscripción General (S/ 80)")
        content = content.replace("Premium (S/ 560)", "Inscripción + Movilidad (S/ 120)")
        content = content.replace("VIP (S/ 940)", "Paquete Completo: Inscripción, Transporte, Hospedaje y Tour (S/ 890)")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Packages updated successfully.")
