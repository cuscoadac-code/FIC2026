from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Bases Tecnicas y Organizacion', 0, 1, 'C')
        self.set_font('Arial', '', 11)
        self.cell(0, 10, 'Reglamento oficial y detalles de la competencia FIC 2026.', 0, 1, 'C')
        self.ln(10)

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size = 11)

text = """
1. Responsables
Ayni Sport SAC.

Municipalidades auspiciadoras:
- Municipalidad de Pisac
- Municipalidad de Taray
- Municipalidad de Qoya
- Municipalidad de Lamay
- Municipalidad de Calca
- Municipalidad de Huayllabamba
- Municipalidad de Yucay
- Municipalidad de Urubamba
- Municipalidad de Ollantaytambo

2. Participantes
- Uso de casco obligatorio.
- Exclusivamente bicicletas montaneras con llantas mayores a 2.1mm de ancho. (SE VAN A MEDIR EL ANCHO DE LAS LLANTAS)
- Para competir deben cumplir con la inscripcion y las reglas del evento.
- La participacion es de responsabilidad individual salvo menores de edad quienes dependen de sus padres o apoderados.
- Los competidores deben firmar el documento de compromiso de NO RIESGO. Ya que es un deporte de aventura y que participan por voluntad propia.
- Cualquier competidor que incumpla las bases seran descalificados.
- Todos los competidores, directivos, representantes y demas personas que intervengan en este evento lo hacen por su PROPIA CUENTA Y RIESGO.

3. Inscripciones
Las fechas de inscripciones es desde el 01 de octubre hasta jueves 19 noviembre a media noche.

Medios de inscripcion:
1. Virtual: Via Yape al n CEL +51 993022225 (adjuntar captura de pantalla del deposito) y datos: Nombre completo - Categoria - Fecha nac. - DNI - Nacionalidad. Tanto en el formulario virtual y fisico.
2. Presencial: Calle Chiwampata 543 San Blas Esquina con Alabado, AGENCIA LUNA LLENA.

- El registro es personal. En caso de ser menor de edad, con autorizacion del padre o apoderado.
- La edad minima para este nivel es de 12 anos.
- Firma de carta de compromiso de Riesgo y declaracion jurada.
- Identificacion en la competencia es su numero bien legible.
- El derecho de participacion es intransferible. No hay reembolso.
- La identificacion externa del competidor sera su numero correctamente ubicado en su bicicleta.

4. De la Competencia
- La competencia se rige bajo las bases.
- Los competidores deben estar media hora antes en la linea de partida.
- Primero partiran las categorias de mayor a menor experiencia.
- Partida: 8:00 am desde San Salvador con direccion a Huayllabamba.
- La categoria NOVEL sera bien revisada (solo competidores sin experiencia).

5. Penalizaciones
- Comportamiento Antideportivo.
- Realizar cortes en la carrera.
- Ingresar en otra categoria.
- Falta de numeracion / equipamiento.
- Uso de caminos no autorizados.
- Desobediencia a instrucciones.

6. Categorias
(La edad es en base al ano de nacimiento mas no del dia de cumpleanos)

- Pre cadetes (12 a 14)
- Cadetes (15 a 17)
- Elite (18 a 29)
- Master A (30 - 39)
- Master B (40 - 49)
- Master C (50 a mayor)
- Enduro
- Damas Elite
- Damas Master
- Noveles / Turismo
- Damas Noveles (> 5)

7. Programa del Evento
- 06:00 hrs: Bienvenida, saludo y entrega de box lunch a los competidores.
- 07:00 - 08:00 hrs: Calentamiento para competidores.
- 09:00 hrs: Control de numeros para la competencia.
- 10:00 hrs: Partida oficial desde Pisac.
- 11:00 - 12:30 hrs: Llegada de los primeros lugares y del peloton a Urubamba.
- 14:00 hrs: Premiacion de categorias.
"""

for line in text.split('\n'):
    pdf.multi_cell(0, 7, txt = line)

pdf.output("bases_tecnicas.pdf")
