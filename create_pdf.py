from fpdf import FPDF
import datetime

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 16)
        self.cell(0, 10, "REGLAMENTO Y BASES - CICLOVIA DEL MAIZ 2026", border=False, align="C")
        self.ln(15)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Pagina {self.page_no()} - Ayni Sport S.A.C. | RUC: 20612898503", align="C")

pdf = PDF()
pdf.add_page()
pdf.set_font("helvetica", size=11)

texto = """1. ORGANIZACION Y RESPONSABILIDAD
El evento 'Ciclovia del Maiz 2026' es organizado exclusivamente por Ayni Sport S.A.C., con RUC 20612898503, con domicilio legal en Mz. a Lote 21 Urb. Mariscal Gamarra I Etapa, Cusco, Peru. La organizacion se reserva el derecho de modificar el presente reglamento para garantizar la seguridad y el correcto desarrollo del evento.

2. CATEGORIAS Y PARTICIPACION
Las categorias oficiales estan abiertas para deportistas a partir de los 12 anos (con Autorizacion de Padres obligatoria para menores de edad en las categorias Precadete y Cadete) y sin limite de edad superior en las categorias Master. Todo participante debe portar su Documento de Identidad original durante el recojo del kit.

3. TRATAMIENTO DE DATOS PERSONALES (Ley N 29733)
De conformidad con el D.S. N 016-2024-JUS, la base de datos de los competidores inscritos se encuentra registrada ante la Autoridad Nacional de Proteccion de Datos Personales (ANPD). Los datos de salud sensibles (historial, alergias) seran utilizados de manera restrictiva y exclusiva para la prevencion de riesgos y atencion de emergencias durante la competencia.

4. POLITICAS DE REEMBOLSO Y CANCELACION (INDECOPI)
Bajo el Codigo de Proteccion y Defensa del Consumidor, si el evento es suspendido o modificado sustancialmente por causas atribuibles a la organizacion, el participante podra solicitar la devolucion integra del monto pagado. Ayni Sport S.A.C. cuenta con un plazo maximo legal de 15 dias calendario para efectuar la devolucion tras la solicitud formal del cliente al correo aynisporteam@gmail.com.

5. PENALIDAD POR 'NO SHOW'
El participante que no asista al recojo de su kit o no se presente a la partida oficial en la fecha y hora indicadas sin previo aviso sustentado, perdera el total de su inscripcion, siendo los montos abonados retenidos como penalidad y compensacion de gastos operativos.

6. DESCARGO DE RESPONSABILIDAD Y ASUNCION DE RIESGOS
El ciclismo de montana (XCM) en la ruta Pisac-Ollantaytambo es un deporte de aventura sujeto al riesgo fisico inherente (caidas, esfuerzo fisico extremo en altitud). 
Con la inscripcion, el participante declara voluntariamente que:
a) Participa asumiendo total responsabilidad sobre su condicion fisica y aptitud deportiva.
b) Entiende que la organizacion no se hace responsable por perdidas materiales ni lesiones derivadas del riesgo normal de la competencia, a pesar del cumplimiento legal de Ayni Sport S.A.C. de contar con guias, rescate paramedico y un plan de contingencia operativo.
c) Exime de cualquier reclamacion civil a Ayni Sport S.A.C. por contingencias inherentes a su propia destreza o negligencia tecnica.

7. COMPORTAMIENTO Y SANCIONES
La organizacion sancionara con la descalificacion inmediata a quien agreda verbal o fisicamente a otro participante o staff, o a quien arroje basura (envolturas, botellas) a lo largo del Valle Sagrado.

Para ejercer sus Derechos ARCO o interponer una queja, ingrese a nuestro Libro de Reclamaciones Virtual en la web oficial: ficperu.online.
"""

pdf.multi_cell(0, 6, texto)

pdf.output("reglamento-fic2026.pdf")
print("PDF generado con exito.")
