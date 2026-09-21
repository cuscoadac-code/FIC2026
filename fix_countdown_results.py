import re

# 1. FIX RESULTADOS.HTML
# Let's ensure the JS in resultados.html is fully robust and wrapped in DOMContentLoaded
with open("resultados.html", "r", encoding="utf-8") as f:
    res_content = f.read()

# I will replace the JS block in resultados.html with a safe, isolated block.
# We will use regex to find the script block containing `const participants =` and replace it.
import json

# Re-read participants if we need to, but it's already there. 
# Let's just fix the logic by ensuring no global scope conflicts.
safe_js = """
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            try {
                const tbody = document.getElementById('tableBody');
                const searchInput = document.getElementById('searchInput');
                const btnGen = document.getElementById('btn-gen');
                const btnCat = document.getElementById('btn-cat');
                const catFilters = document.getElementById('cat-filters');
                const categorySelect = document.getElementById('categorySelect');
                const noResults = document.getElementById('noResults');
                const resultsTable = document.getElementById('resultsTable');

                let currentMode = 'general';

                function getMedal(pos) {
                    if (pos === 1) return '🥇';
                    if (pos === 2) return '🥈';
                    if (pos === 3) return '🥉';
                    return pos;
                }

                function renderTable(data) {
                    tbody.innerHTML = '';
                    
                    if(data.length === 0) {
                        noResults.classList.remove('hidden');
                        resultsTable.classList.add('hidden');
                        return;
                    }
                    
                    noResults.classList.add('hidden');
                    resultsTable.classList.remove('hidden');

                    data.forEach((p, index) => {
                        const bgClass = index % 2 === 0 ? 'bg-white' : 'bg-gray-100';
                        const tr = document.createElement('tr');
                        tr.className = bgClass + ' border-b border-gray-300 table-row-hover text-center';
                        
                        tr.innerHTML = `
                            <td class="p-2 border-r border-gray-300 font-bold text-lg">${getMedal(p.pos_gral)}</td>
                            <td class="p-2 border-r border-gray-300">${p.pos_genero}</td>
                            <td class="p-2 border-r border-gray-300">${p.pos_cat}</td>
                            <td class="p-2 border-r border-gray-300 font-bold text-gray-900">${p.dorsal}</td>
                            <td class="p-2 border-r border-gray-300 text-left font-bold">${p.nombre}</td>
                            <td class="p-2 border-r border-gray-300 text-xs">${p.categoria}</td>
                            <td class="p-2 border-r border-gray-300">${p.genero}</td>
                            <td class="p-2 border-r border-gray-300">${p.pais}</td>
                            <td class="p-2 border-r border-gray-300 font-mono">${p.etapa1}</td>
                            <td class="p-2 border-r border-gray-300 font-mono">${p.etapa2}</td>
                            <td class="p-2 border-r border-gray-300 font-mono font-bold bg-gray-200">${p.total}</td>
                            <td class="p-2 border-r border-gray-300 font-mono text-xs text-gray-500">${p.diff_primero}</td>
                            <td class="p-2 font-mono text-xs text-gray-500">${p.diff_anterior}</td>
                        `;
                        tbody.appendChild(tr);
                    });
                }

                function filterData() {
                    const search = searchInput.value.toLowerCase();
                    const cat = categorySelect.value;
                    
                    let filtered = participants.filter(p => {
                        const matchSearch = p.nombre.toLowerCase().includes(search) || 
                                            p.dorsal.toString().includes(search) || 
                                            p.pais.toLowerCase().includes(search);
                                            
                        if (currentMode === 'categoria' && cat !== 'all') {
                            return matchSearch && p.categoria === cat;
                        }
                        return matchSearch;
                    });

                    renderTable(filtered);
                }

                searchInput.addEventListener('input', filterData);
                categorySelect.addEventListener('change', filterData);

                btnGen.addEventListener('click', () => {
                    currentMode = 'general';
                    btnGen.classList.add('active');
                    btnCat.classList.remove('active');
                    catFilters.style.display = 'none';
                    categorySelect.value = 'all';
                    filterData();
                });

                btnCat.addEventListener('click', () => {
                    currentMode = 'categoria';
                    btnCat.classList.add('active');
                    btnGen.classList.remove('active');
                    catFilters.style.display = 'flex';
                    filterData();
                });

                renderTable(participants);
            } catch(e) {
                console.error("Error loading results:", e);
            }
        });
    </script>
"""

# Extract the participants array before replacing
part_match = re.search(r'const participants = (\[.*?\]);', res_content, re.DOTALL)
if part_match:
    participants_arr = part_match.group(1)
    # Replace everything from <script>\s*const participants = ... to </script>
    res_content = re.sub(r'<script>\s*const participants = \[.*?</script>', 
                         f"<script>\nconst participants = {participants_arr};\n</script>\n{safe_js}", 
                         res_content, flags=re.DOTALL)

with open("resultados.html", "w", encoding="utf-8") as f:
    f.write(res_content)


# 2. ADD COUNTDOWN TO INDEX.HTML
with open("index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

countdown_html = """
<div class="mt-12 flex flex-wrap gap-4 justify-start md:justify-start">
    <div class="bg-black bg-opacity-40 backdrop-blur-md border border-gray-500 rounded-xl p-4 w-24 text-center shadow-lg">
        <div id="cd-days" class="text-3xl font-bold text-white mb-1">00</div>
        <div class="text-xs text-gray-300 uppercase tracking-wider">Días</div>
    </div>
    <div class="bg-black bg-opacity-40 backdrop-blur-md border border-gray-500 rounded-xl p-4 w-24 text-center shadow-lg">
        <div id="cd-hours" class="text-3xl font-bold text-white mb-1">00</div>
        <div class="text-xs text-gray-300 uppercase tracking-wider">Horas</div>
    </div>
    <div class="bg-black bg-opacity-40 backdrop-blur-md border border-gray-500 rounded-xl p-4 w-24 text-center shadow-lg">
        <div id="cd-minutes" class="text-3xl font-bold text-white mb-1">00</div>
        <div class="text-xs text-gray-300 uppercase tracking-wider">Minutos</div>
    </div>
    <div class="bg-black bg-opacity-40 backdrop-blur-md border border-gray-500 rounded-xl p-4 w-24 text-center shadow-lg">
        <div id="cd-seconds" class="text-3xl font-bold text-white mb-1">00</div>
        <div class="text-xs text-gray-300 uppercase tracking-wider">Segundos</div>
    </div>
</div>
"""

# Find where to inject in the Hero section
# <a href="#inscripcion" class="inline-block bg-primary hover:bg-opacity-90 text-white font-bold py-3 px-8 !rounded-button text-lg shadow-lg transition-all whitespace-nowrap">
# Inscríbete ahora
# </a>

if 'id="cd-days"' not in idx_content:
    idx_content = re.sub(r'(<a href="index\.html#inscripcion"|<!-- Enlace a inscripciones -->|<a href="#inscripcion"|<a href="index\.html#inscripcion")([^>]*>.*?Inscríbete ahora\s*</a>)',
                         r'\1\2\n' + countdown_html, idx_content, flags=re.DOTALL)

# Add Countdown JS Logic at the end
countdown_js = """
<script>
    // Countdown Timer Logic
    document.addEventListener('DOMContentLoaded', () => {
        const countDownDate = new Date("Nov 20, 2026 00:00:00").getTime();

        const x = setInterval(function() {
            const now = new Date().getTime();
            const distance = countDownDate - now;

            if (distance < 0) {
                clearInterval(x);
                return;
            }

            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            const elDays = document.getElementById("cd-days");
            const elHours = document.getElementById("cd-hours");
            const elMins = document.getElementById("cd-minutes");
            const elSecs = document.getElementById("cd-seconds");

            if (elDays) elDays.innerHTML = days.toString().padStart(2, '0');
            if (elHours) elHours.innerHTML = hours.toString().padStart(2, '0');
            if (elMins) elMins.innerHTML = minutes.toString().padStart(2, '0');
            if (elSecs) elSecs.innerHTML = seconds.toString().padStart(2, '0');
        }, 1000);
    });
</script>
"""

if 'cd-days' in countdown_html and 'const countDownDate' not in idx_content:
    idx_content = idx_content.replace('</body>', countdown_js + '\n</body>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx_content)

print("Countdown added and Resultados JS fixed.")
