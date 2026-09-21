import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Title and hero
content = content.replace('Ciclovía del Maíz 2025', 'Ciclovía del Maíz 2026')
content = content.replace('15-17 de Agosto, 2025', '20-22 de Noviembre, 2026')

# Schedule
content = content.replace('Día 1: Viernes 15 de Agosto', 'Día 1: Viernes 20 de Noviembre')
content = content.replace('Día 2: Sábado 16 de Agosto', 'Día 2: Sábado 21 de Noviembre')
content = content.replace('Día 3: Domingo 17 de Agosto', 'Día 3: Domingo 22 de Noviembre')

# Timeline
content = content.replace('15 de julio, 2025', '15 de octubre, 2026')
content = content.replace('14 de agosto, 2025', '19 de noviembre, 2026')
content = content.replace('15-17 de agosto, 2025', '20-22 de noviembre, 2026')

# Footer & Script
content = content.replace('&copy; 2025 Ciclovía del Maíz', '&copy; 2026 Ciclovía del Maíz')
content = content.replace("new Date('August 15, 2025 08:00:00')", "new Date('November 20, 2026 08:00:00')")
content = content.replace("['2020', '2021', '2022', '2023', '2024', '2025']", "['2021', '2022', '2023', '2024', '2025', '2026']")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Dates updated.")
