import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_cards = """          <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              <!-- Paquete Biker -->
              <div class="bg-gray-50 rounded-2xl shadow-lg overflow-hidden border border-gray-200 flex flex-col">
                  <div class="p-6 text-center bg-gray-100 border-b border-gray-200">
                      <h3 class="text-xl font-bold text-gray-800 mb-2">PAQUETE BIKER</h3>
                      <div class="text-4xl font-extrabold text-primary mb-2">S/ 90</div>
                  </div>
                  <div class="p-6 flex-1">
                      <ul class="space-y-3 mb-6">
                          <li class="flex items-center"><i class="ri-checkbox-circle-fill text-gray-400 text-lg mr-2"></i><span class="font-bold text-gray-700 text-sm">Inscripción básica</span></li>
                      </ul>
                  </div>
              </div>

              <!-- Paquete Biker + Transporte -->
              <div class="bg-gray-50 rounded-2xl shadow-lg overflow-hidden border border-gray-200 flex flex-col">
                  <div class="p-6 text-center bg-gray-100 border-b border-gray-200">
                      <h3 class="text-xl font-bold text-gray-800 mb-2">BIKER + TRANSPORTE</h3>
                      <div class="text-4xl font-extrabold text-primary mb-2">S/ 140</div>
                  </div>
                  <div class="p-6 flex-1">
                      <ul class="space-y-3 mb-6">
                          <li class="flex items-center"><i class="ri-checkbox-circle-fill text-gray-400 text-lg mr-2"></i><span class="font-bold text-gray-700 text-sm">Inscripción básica</span></li>
                          <li class="flex items-center"><i class="ri-checkbox-circle-fill text-gray-400 text-lg mr-2"></i><span class="font-bold text-gray-700 text-sm">Transporte</span></li>
                      </ul>
                  </div>
              </div>

              <!-- Paquete Biker + Jersey -->
              <div class="bg-gray-50 rounded-2xl shadow-lg overflow-hidden border border-gray-200 flex flex-col relative">
                  <div class="absolute top-0 right-0 bg-primary text-white font-bold px-3 py-1 rounded-bl-lg text-xs uppercase tracking-wider">Popular</div>
                  <div class="p-6 text-center bg-orange-50 border-b border-orange-100">
                      <h3 class="text-xl font-bold text-gray-800 mb-2">BIKER + JERSEY</h3>
                      <div class="text-4xl font-extrabold text-primary mb-2">S/ 150</div>
                  </div>
                  <div class="p-6 flex-1">
                      <ul class="space-y-3 mb-6">
                          <li class="flex items-center"><i class="ri-checkbox-circle-fill text-primary text-lg mr-2"></i><span class="font-bold text-gray-700 text-sm">Inscripción básica</span></li>
                          <li class="flex items-center"><i class="ri-checkbox-circle-fill text-primary text-lg mr-2"></i><span class="font-bold text-gray-700 text-sm">Jersey Oficial</span></li>
                      </ul>
                  </div>
              </div>
              
              <!-- Paquete Biker Full -->
              <div class="bg-gray-900 rounded-2xl shadow-lg overflow-hidden border border-gray-700 flex flex-col relative">
                  <div class="absolute top-0 right-0 bg-yellow-500 text-white font-bold px-3 py-1 rounded-bl-lg text-xs uppercase tracking-wider">PREMIUM</div>
                  <div class="p-6 text-center bg-gray-800 border-b border-gray-700">
                      <h3 class="text-xl font-bold text-white mb-2">PAQUETE BIKER FULL</h3>
                      <div class="text-4xl font-extrabold text-yellow-500 mb-2">S/ 200</div>
                  </div>
                  <div class="p-6 flex-1">
                      <ul class="space-y-3 mb-6">
                          <li class="flex items-center"><i class="ri-checkbox-circle-fill text-yellow-500 text-lg mr-2"></i><span class="font-bold text-gray-300 text-sm">Inscripción básica</span></li>
                          <li class="flex items-center"><i class="ri-checkbox-circle-fill text-yellow-500 text-lg mr-2"></i><span class="font-bold text-gray-300 text-sm">Transporte</span></li>
                          <li class="flex items-center"><i class="ri-checkbox-circle-fill text-yellow-500 text-lg mr-2"></i><span class="font-bold text-gray-300 text-sm">Jersey Oficial</span></li>
                      </ul>
                  </div>
              </div>
          </div>"""

# Find the start and end of the cards grid
pattern_cards = re.compile(r'<div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">.*?</div>\s*</div>\s*</section>', re.DOTALL)
content = pattern_cards.sub(new_cards + '\n      </div>\n  </section>', content)

new_form_radios = """<div class="grid grid-cols-1 md:grid-cols-2 gap-3 mb-6">
                        <label class="flex items-center p-4 border rounded-lg hover:bg-gray-50 cursor-pointer">
                            <input type="radio" name="paquete" id="pack-basico" value="PAQUETE BIKER (S/ 90)" class="custom-checkbox text-primary" required>
                            <div class="ml-3">
                                <span class="block font-bold text-gray-800">PAQUETE BIKER</span>
                                <span class="block text-sm text-gray-500 font-semibold">S/ 90</span>
                            </div>
                        </label>
                        <label class="flex items-center p-4 border rounded-lg hover:bg-gray-50 cursor-pointer">
                            <input type="radio" name="paquete" id="pack-transporte" value="BIKER + TRANSPORTE (S/ 140)" class="custom-checkbox text-primary" required>
                            <div class="ml-3">
                                <span class="block font-bold text-gray-800">BIKER + TRANSPORTE</span>
                                <span class="block text-sm text-gray-500 font-semibold">S/ 140</span>
                            </div>
                        </label>
                        <label class="flex items-center p-4 border rounded-lg hover:bg-orange-50 cursor-pointer border-orange-300 bg-orange-50">
                            <input type="radio" name="paquete" id="pack-jersey" value="BIKER + JERSEY (S/ 150)" class="custom-checkbox text-primary" checked required>
                            <div class="ml-3">
                                <span class="block font-bold text-orange-700">BIKER + JERSEY</span>
                                <span class="block text-sm text-orange-600 font-bold">S/ 150</span>
                            </div>
                        </label>
                        <label class="flex items-center p-4 border rounded-lg hover:bg-gray-800 cursor-pointer border-gray-700 bg-gray-900">
                            <input type="radio" name="paquete" id="pack-full" value="PAQUETE BIKER FULL (S/ 200)" class="custom-checkbox text-primary" required>
                            <div class="ml-3">
                                <span class="block font-bold text-yellow-500">PAQUETE BIKER FULL</span>
                                <span class="block text-sm text-gray-300 font-bold">S/ 200</span>
                            </div>
                        </label>
                    </div>"""

pattern_form = re.compile(r'<div class="grid grid-cols-1 md:grid-cols-2 gap-3 mb-6">\s*<label class="flex items-center.*?</div>\s*</label>\s*</div>', re.DOTALL)
content = pattern_form.sub(new_form_radios, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML structure updated for 4 packages.")
