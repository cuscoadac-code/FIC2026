import json
import random

# List of sample names, countries, categories
first_names_m = ["Carlos", "Juan", "Diego", "Roberto", "Luis", "Jorge", "Miguel", "Fernando", "Alejandro", "Andrés"]
first_names_f = ["María", "Ana", "Lucía", "Sofía", "Camila", "Valeria", "Mariana", "Daniela", "Gabriela", "Paula"]
last_names = ["Ramírez", "Silva", "Vásquez", "Gómez", "López", "Torres", "Pérez", "García", "Martínez", "Rodríguez", "Fernández", "González"]
countries = ["PERU", "COLOMBIA", "CHILE", "ECUADOR", "ARGENTINA", "BRASIL", "BOLIVIA", "EEUU", "ESPAÑA", "MEXICO"]

categories = [
    {"name": "Elite Masculino", "gender": "M"},
    {"name": "Elite Femenino", "gender": "F"},
    {"name": "Master A (30-39)", "gender": "M"},
    {"name": "Master B (40-49)", "gender": "M"},
    {"name": "Master C (50+)", "gender": "M"},
    {"name": "Damas A", "gender": "F"},
    {"name": "E-Bike", "gender": "M"}
]

def seconds_to_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

participants = []

# Generate 100 participants
for i in range(1, 101):
    cat = random.choice(categories)
    gender = cat["gender"]
    
    if gender == "M":
        name = f"{random.choice(first_names_m)} {random.choice(last_names)} {random.choice(last_names)}"
    else:
        name = f"{random.choice(first_names_f)} {random.choice(last_names)} {random.choice(last_names)}"
        
    country = random.choice(countries)
    number = 100 + i
    
    # Times in seconds
    base_time_e1 = random.randint(1800, 3600) # 30 mins to 1 hour
    base_time_e2 = random.randint(7200, 14400) # 2 hours to 4 hours
    total = base_time_e1 + base_time_e2
    
    participants.append({
        "id": i,
        "dorsal": number,
        "nombre": name.upper(),
        "categoria": cat["name"],
        "genero": gender,
        "pais": country,
        "etapa1_sec": base_time_e1,
        "etapa2_sec": base_time_e2,
        "total_sec": total,
        "etapa1": seconds_to_time(base_time_e1),
        "etapa2": seconds_to_time(base_time_e2),
        "total": seconds_to_time(total)
    })

# Sort by total time to calculate positions
participants.sort(key=lambda x: x["total_sec"])

# Calculate positions and differences
first_total = participants[0]["total_sec"]
cat_counts = {}
gender_counts = {"M": 0, "F": 0}

for idx, p in enumerate(participants):
    # General pos
    p["pos_gral"] = idx + 1
    
    # Gender pos
    gender_counts[p["genero"]] += 1
    p["pos_genero"] = gender_counts[p["genero"]]
    
    # Category pos
    if p["categoria"] not in cat_counts:
        cat_counts[p["categoria"]] = 0
    cat_counts[p["categoria"]] += 1
    p["pos_cat"] = cat_counts[p["categoria"]]
    
    # Differences
    if idx == 0:
        p["diff_primero"] = "-"
        p["diff_anterior"] = "-"
    else:
        p["diff_primero"] = f"+{seconds_to_time(p['total_sec'] - first_total)}"
        p["diff_anterior"] = f"+{seconds_to_time(p['total_sec'] - participants[idx-1]['total_sec'])}"

participants_json = json.dumps(participants)

# HTML TEMPLATE
html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultados - Ciclovía del Maíz 2026</title>
    <script src="https://cdn.tailwindcss.com/3.4.16"></script>
    <script>
        tailwind.config={{
            theme:{{
                extend:{{
                    colors:{{
                        primary:'#FF7A00', // Naranja estilo Machu Picchu Epic
                        secondary:'#4A4A4A'
                    }}
                }}
            }}
        }}
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/remixicon@4.5.0/fonts/remixicon.css" rel="stylesheet">
    <style>
        body {{ font-family: 'Open Sans', sans-serif; background-image: url('https://images.unsplash.com/photo-1544181093-c712c9a1d131?q=80&w=1920&auto=format&fit=crop'); background-attachment: fixed; background-size: cover; }}
        .glass-panel {{ background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); }}
        .table-row-hover:hover {{ background-color: #f3f4f6; }}
        
        /* Custom scrollbar for table */
        .table-container::-webkit-scrollbar {{ height: 8px; }}
        .table-container::-webkit-scrollbar-track {{ background: #f1f1f1; }}
        .table-container::-webkit-scrollbar-thumb {{ background: #888; border-radius: 4px; }}
        .table-container::-webkit-scrollbar-thumb:hover {{ background: #555; }}
        
        .medal {{ font-size: 1.5rem; }}
        .btn-filter {{ padding: 0.5rem 1.5rem; border-radius: 9999px; font-weight: bold; border: 2px solid #FF7A00; transition: all 0.2s; background: white; color: #FF7A00; }}
        .btn-filter.active {{ background: #FF7A00; color: white; }}
    </style>
</head>
<body class="flex flex-col min-h-screen">

    <!-- Navbar -->
    <header class="bg-gray-900 text-white shadow-md sticky top-0 z-50">
        <nav class="container mx-auto px-6 py-4 flex justify-between items-center">
            <h1 class="text-2xl font-bold text-primary"><a href="index.html">FIC 2026</a></h1>
            <div class="hidden md:flex space-x-8 text-sm font-bold">
                <a href="index.html" class="hover:text-primary transition-colors">Volver al Inicio</a>
            </div>
        </nav>
    </header>

    <!-- Main Content -->
    <main class="flex-grow container mx-auto px-2 py-8">
        
        <div class="glass-panel rounded-xl shadow-2xl overflow-hidden border-t-4 border-primary">
            
            <!-- Filters Header -->
            <div class="p-6 border-b border-gray-200">
                
                <!-- Buscador -->
                <div class="max-w-md mx-auto mb-6 relative">
                    <i class="ri-search-line absolute left-4 top-3 text-gray-400 text-xl"></i>
                    <input type="text" id="searchInput" placeholder="Buscar por Nombre, Dorsal o País..." class="w-full pl-12 pr-4 py-3 rounded-full border-2 border-gray-200 focus:outline-none focus:border-primary shadow-sm text-gray-700 font-bold">
                </div>

                <!-- Botones de Filtro -->
                <div class="flex flex-wrap justify-center gap-3 mb-4">
                    <button class="btn-filter active" id="btn-gen">Generales</button>
                    <button class="btn-filter" id="btn-cat">Categorías</button>
                </div>
                
                <div class="flex flex-wrap justify-center gap-3" id="cat-filters" style="display: none;">
                    <select id="categorySelect" class="btn-filter bg-white text-primary border-primary font-bold appearance-none px-6">
                        <option value="all">Todas las Categorías</option>
                        <option value="Elite Masculino">Elite Masculino</option>
                        <option value="Elite Femenino">Elite Femenino</option>
                        <option value="Master A (30-39)">Master A (30-39)</option>
                        <option value="Master B (40-49)">Master B (40-49)</option>
                        <option value="Master C (50+)">Master C (50+)</option>
                        <option value="Damas A">Damas A</option>
                        <option value="E-Bike">E-Bike</option>
                    </select>
                </div>
            </div>

            <!-- Tabla -->
            <div class="table-container overflow-x-auto p-4">
                <table class="w-full text-sm text-left border-collapse min-w-[1200px]" id="resultsTable">
                    <thead>
                        <tr class="bg-gray-600 text-white text-xs uppercase tracking-wider text-center">
                            <th colspan="13" class="p-2 border border-gray-500 text-sm">Resultados de la carrera 2 Días - FIC 2026</th>
                        </tr>
                        <tr class="bg-gray-500 text-white text-xs uppercase tracking-wider text-center">
                            <th class="p-3 border-r border-gray-400">Pos.<br>Gral.</th>
                            <th class="p-3 border-r border-gray-400">Pos.<br>Género</th>
                            <th class="p-3 border-r border-gray-400">Pos.<br>Cat.</th>
                            <th class="p-3 border-r border-gray-400">N°</th>
                            <th class="p-3 border-r border-gray-400 text-left min-w-[200px]">Nombre</th>
                            <th class="p-3 border-r border-gray-400">Categoría</th>
                            <th class="p-3 border-r border-gray-400">Género</th>
                            <th class="p-3 border-r border-gray-400">País</th>
                            <th class="p-3 border-r border-gray-400">Prólogo</th>
                            <th class="p-3 border-r border-gray-400">Maratón</th>
                            <th class="p-3 border-r border-gray-400 bg-gray-600 font-bold text-sm">Total</th>
                            <th class="p-3 border-r border-gray-400">Diff.<br>Primero</th>
                            <th class="p-3">Diff.<br>Anterior</th>
                        </tr>
                    </thead>
                    <tbody class="text-gray-800 font-semibold" id="tableBody">
                        <!-- Generado por JS -->
                    </tbody>
                </table>
                <div id="noResults" class="hidden text-center py-10 text-gray-500 font-bold text-lg">
                    No se encontraron participantes.
                </div>
            </div>
            
        </div>
    </main>

    <!-- JS Logic -->
    <script>
        const participants = {participants_json};
        
        const tbody = document.getElementById('tableBody');
        const searchInput = document.getElementById('searchInput');
        const btnGen = document.getElementById('btn-gen');
        const btnCat = document.getElementById('btn-cat');
        const catFilters = document.getElementById('cat-filters');
        const categorySelect = document.getElementById('categorySelect');
        const noResults = document.getElementById('noResults');
        const resultsTable = document.getElementById('resultsTable');

        let currentMode = 'general'; // 'general' or 'categoria'

        function getMedal(pos) {{
            if (pos === 1) return '🥇';
            if (pos === 2) return '🥈';
            if (pos === 3) return '🥉';
            return pos;
        }}

        function renderTable(data) {{
            tbody.innerHTML = '';
            
            if(data.length === 0) {{
                noResults.classList.remove('hidden');
                resultsTable.classList.add('hidden');
                return;
            }}
            
            noResults.classList.add('hidden');
            resultsTable.classList.remove('hidden');

            data.forEach((p, index) => {{
                // Alternate row colors
                const bgClass = index % 2 === 0 ? 'bg-white' : 'bg-gray-100';
                
                const tr = document.createElement('tr');
                tr.className = `${{bgClass}} border-b border-gray-300 table-row-hover text-center`;
                
                tr.innerHTML = `
                    <td class="p-2 border-r border-gray-300 font-bold text-lg">${{getMedal(p.pos_gral)}}</td>
                    <td class="p-2 border-r border-gray-300">${{p.pos_genero}}</td>
                    <td class="p-2 border-r border-gray-300">${{p.pos_cat}}</td>
                    <td class="p-2 border-r border-gray-300 font-bold text-gray-900">${{p.dorsal}}</td>
                    <td class="p-2 border-r border-gray-300 text-left font-bold">${{p.nombre}}</td>
                    <td class="p-2 border-r border-gray-300 text-xs">${{p.categoria}}</td>
                    <td class="p-2 border-r border-gray-300">${{p.genero}}</td>
                    <td class="p-2 border-r border-gray-300">${{p.pais}}</td>
                    <td class="p-2 border-r border-gray-300 font-mono">${{p.etapa1}}</td>
                    <td class="p-2 border-r border-gray-300 font-mono">${{p.etapa2}}</td>
                    <td class="p-2 border-r border-gray-300 font-mono font-bold bg-gray-200">${{p.total}}</td>
                    <td class="p-2 border-r border-gray-300 font-mono text-xs text-gray-500">${{p.diff_primero}}</td>
                    <td class="p-2 font-mono text-xs text-gray-500">${{p.diff_anterior}}</td>
                `;
                tbody.appendChild(tr);
            }});
        }}

        function filterData() {{
            const search = searchInput.value.toLowerCase();
            const cat = categorySelect.value;
            
            let filtered = participants.filter(p => {{
                const matchSearch = p.nombre.toLowerCase().includes(search) || 
                                    p.dorsal.toString().includes(search) || 
                                    p.pais.toLowerCase().includes(search);
                                    
                if (currentMode === 'categoria' && cat !== 'all') {{
                    return matchSearch && p.categoria === cat;
                }}
                return matchSearch;
            }});

            renderTable(filtered);
        }}

        // Event Listeners
        searchInput.addEventListener('input', filterData);
        categorySelect.addEventListener('change', filterData);

        btnGen.addEventListener('click', () => {{
            currentMode = 'general';
            btnGen.classList.add('active');
            btnCat.classList.remove('active');
            catFilters.style.display = 'none';
            categorySelect.value = 'all';
            filterData();
        }});

        btnCat.addEventListener('click', () => {{
            currentMode = 'categoria';
            btnCat.classList.add('active');
            btnGen.classList.remove('active');
            catFilters.style.display = 'flex';
            filterData();
        }});

        // Initial render
        renderTable(participants);
    </script>
</body>
</html>
"""

with open("resultados.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("resultados.html generado con 100 participantes simulados.")
