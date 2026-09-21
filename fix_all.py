import re

# ==========================================
# 1. FIX RESULTADOS.HTML
# ==========================================
with open("resultados.html", "r", encoding="utf-8") as f:
    res_content = f.read()

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

# Find the start of the <script> block with participants array
start_script = res_content.find("<script>\n        const participants = [")
end_script = res_content.find("</script>", start_script)

if start_script != -1 and end_script != -1:
    old_script_block = res_content[start_script:end_script+9]
    # We want to extract just the array to put it in a safe script block
    arr_start = old_script_block.find("const participants = [")
    arr_end = old_script_block.find("];", arr_start)
    if arr_start != -1 and arr_end != -1:
        participants_arr = old_script_block[arr_start:arr_end+2]
        new_block = f"<script>\n        {participants_arr}\n    </script>\n{safe_js}"
        res_content = res_content.replace(old_script_block, new_block)

with open("resultados.html", "w", encoding="utf-8") as f:
    f.write(res_content)

# ==========================================
# 2. UPDATE INDEX.HTML (COUNTDOWN & WA)
# ==========================================
with open("index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

# --- ADD COUNTDOWN ---
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

# Only add if it's not already there
if 'id="cd-days"' not in idx_content:
    idx_content = re.sub(r'(<a href="#inscripcion"[^>]*>.*?Inscríbete ahora\s*</a>)', r'\1\n' + countdown_html, idx_content, flags=re.IGNORECASE)

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


# --- REPLACE CHATBOT WITH WHATSAPP FLOATING BUTTON ---
wa_button = """
<!-- WhatsApp Floating Button -->
<a href="https://wa.me/51993022225?text=Hola,%20deseo%20m%C3%A1s%20informaci%C3%B3n%20sobre%20la%20Ciclov%C3%ADa%20del%20Ma%C3%ADz" target="_blank" class="fixed bottom-6 right-6 w-14 h-14 bg-green-500 rounded-full shadow-2xl flex items-center justify-center text-white hover:bg-green-600 hover:scale-110 transition-all z-50 cursor-pointer">
    <i class="ri-whatsapp-line text-3xl"></i>
</a>
"""

# We need to remove the existing chat Window and toggle button
chatbot_pattern = r'<!-- Floating Chat Button -->.*?<div id="chatWindow".*?</div>\s*</div>\s*</div>\s*</div>'
idx_content = re.sub(chatbot_pattern, wa_button, idx_content, flags=re.DOTALL)

# And remove the JS logic for the chatbot
chatbot_js_pattern = r'// Chatbot Logic.*?}\);'
idx_content = re.sub(chatbot_js_pattern, '', idx_content, flags=re.DOTALL)


with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx_content)

print("All tasks applied successfully.")
