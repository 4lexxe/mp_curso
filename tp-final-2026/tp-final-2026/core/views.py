"""
Vistas del Sprint 1 - Clínica SaludPlus.

Todas las vistas son Vistas Basadas en Clases (CBV) de tipo TemplateView,
ya que el Sprint 1 trabaja sobre maquetado y navegación estática.
"""
from django.conf import settings
from django.views.generic import TemplateView

CLINICA = settings.CLINICA


class InicioView(TemplateView):
    """Home (/): identidad institucional, hero, CTA y ventajas clave."""
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "clinica": CLINICA,
                "titulo_pagina": "Inicio",
                "ventajas": [
                    {
                        "icono": "bi-clock-fill",
                        "titulo": "Atención de guardia 24/7",
                        "texto": (
                            "Guardia médica operada las 24 horas, los 365 días "
                            "del año, con equipos de urgencias y traumatología "
                            "siempre disponibles."
                        ),
                    },
                    {
                        "icono": "bi-heart-pulse-fill",
                        "titulo": "Tecnología diagnóstica",
                        "texto": (
                            "Laboratorio propio, tomografía, resonancia magnética "
                            "y estudios funcionales con resultados digitales en "
                            "tu historia clínica."
                        ),
                    },
                    {
                        "icono": "bi-calendar2-check-fill",
                        "titulo": "Facilidad de reserva online",
                        "texto": (
                            "Reservá tu turno en pocos clics, elegí profesional y "
                            "recibí la confirmación por correo electrónico sin "
                            "filas ni llamados."
                        ),
                    },
                ],
            }
        )
        return context


class EspecialidadesView(TemplateView):
    """Especialidades Médicas (/especialidades/): catálogo en grilla de cards."""
    template_name = "especialidades.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "clinica": CLINICA,
                "titulo_pagina": "Especialidades Médicas",
                "especialidades": [
                    {
                        "nombre": "Cardiología",
                        "icono": "bi-activity",
                        "resumen": (
                            "Estudios electrocardiográficos, ecocardiograma, "
                            "Holter y prevención de enfermedades cardiovasculares."
                        ),
                        "badges": ["Consulta", "Estudios", "Preventiva"],
                    },
                    {
                        "nombre": "Pediatría",
                        "icono": "bi-emoji-smile",
                        "resumen": (
                            "Controles de crecimiento y desarrollo, vacunación "
                            "esquema completo y neonatología."
                        ),
                        "badges": ["0 a 18 años", "Controles", "Vacunación"],
                    },
                    {
                        "nombre": "Traumatología",
                        "icono": "bi-bandaid",
                        "resumen": (
                            "Diagnóstico y tratamiento de lesiones óseas, "
                            "articulares y musculares, con rehabilitación."
                        ),
                        "badges": ["Consultorio", "Rehabilitación"],
                    },
                    {
                        "nombre": "Odontología",
                        "icono": "bi-eyedropper",
                        "resumen": (
                            "Odontología general, estética, ortodoncia y "
                            "endodoncia para toda la familia."
                        ),
                        "badges": ["General", "Estética", "Ortodoncia"],
                    },
                    {
                        "nombre": "Oftalmología",
                        "icono": "bi-eye-fill",
                        "resumen": (
                            "Agudeza visual, fondo de ojo, tonometría y "
                            "cirugía de cataratas con tecnología láser."
                        ),
                        "badges": ["Consulta", "Cirugía"],
                    },
                    {
                        "nombre": "Clínica Médica",
                        "icono": "bi-stethoscope",
                        "resumen": (
                            "Atención general, chequeos preventivos, "
                            "diagnóstico integral y seguimiento de patologías "
                            "crónicas."
                        ),
                        "badges": ["General", "Chequeo"],
                    },
                    {
                        "nombre": "Ginecología",
                        "icono": "bi-gender-female",
                        "resumen": (
                            "Controles ginecológicos, planificación familiar, "
                            "ecografías y salud integral de la mujer."
                        ),
                        "badges": ["Consulta", "Ecografía"],
                    },
                    {
                        "nombre": "Dermatología",
                        "icono": "bi-droplet-fill",
                        "resumen": (
                            "Diagnóstico de lesiones de piel, control de lunares, "
                            "dermatología estética y alergias."
                        ),
                        "badges": ["Consulta", "Estética"],
                    },
                    {
                        "nombre": "Nutrición",
                        "icono": "bi-apple",
                        "resumen": (
                            "Planes alimentarios personalizados, control de peso "
                            "y acompañamiento en enfermedades metabólicas."
                        ),
                        "badges": ["Plan a medida", "Seguimiento"],
                    },
                ],
            }
        )
        return context


class ProfesionalesView(TemplateView):
    """Staff Profesional (/profesionales/): directorio en grilla de cards."""
    template_name = "profesionales.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "clinica": CLINICA,
                "titulo_pagina": "Staff Profesional",
                "profesionales": [
                    {
                        "nombre": "Dra. Luciana Fernández",
                        "titulo": "Doctora en Medicina - UBA",
                        "especialidad": "Cardiología",
                        "matricula": "MN 128.456 - MP 45.102",
                        "estado": "Agenda Abierta",
                        "abierto": True,
                        "foto": "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=400&q=80",
                    },
                    {
                        "nombre": "Dr. Martín Ocampo",
                        "titulo": "Doctor en Medicina - UTN",
                        "especialidad": "Traumatología",
                        "matricula": "MN 119.873 - MP 42.880",
                        "estado": "Consultorio Completo",
                        "abierto": False,
                        "foto": "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?auto=format&fit=crop&w=400&q=80",
                    },
                    {
                        "nombre": "Dra. Carla Domínguez",
                        "titulo": "Doctora en Medicina - UBA",
                        "especialidad": "Pediatría",
                        "matricula": "MN 131.220 - MP 46.511",
                        "estado": "Agenda Abierta",
                        "abierto": True,
                        "foto": "https://images.unsplash.com/photo-1594824476967-48c8b964273f?auto=format&fit=crop&w=400&q=80",
                    },
                    {
                        "nombre": "Dr. Sebastián Ríos",
                        "titulo": "Doctor en Medicina - UNR",
                        "especialidad": "Clínica Médica",
                        "matricula": "MN 125.004 - MP 44.739",
                        "estado": "Agenda Abierta",
                        "abierto": True,
                        "foto": "https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=400&q=80",
                    },
                    {
                        "nombre": "Dra. Valentina Peralta",
                        "titulo": "Doctora en Medicina - UBA",
                        "especialidad": "Dermatología",
                        "matricula": "MN 134.567 - MP 47.203",
                        "estado": "Consultorio Completo",
                        "abierto": False,
                        "foto": "https://images.unsplash.com/photo-1651008376811-b90baee60c1f?auto=format&fit=crop&w=400&q=80",
                    },
                    {
                        "nombre": "Dr. Ignacio Ferreyra",
                        "titulo": "Doctor en Medicina - UNC",
                        "especialidad": "Oftalmología",
                        "matricula": "MN 122.918 - MP 43.665",
                        "estado": "Agenda Abierta",
                        "abierto": True,
                        "foto": "https://images.unsplash.com/photo-1537368910025-700350fe46c7?auto=format&fit=crop&w=400&q=80",
                    },
                ],
            }
        )
        return context


class ReservarView(TemplateView):
    """Gestión de Turnos (/reservar/): formulario estático de solicitud."""
    template_name = "reservar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "clinica": CLINICA,
                "titulo_pagina": "Reservar Turno",
                "especialidades": [
                    "Cardiología",
                    "Pediatría",
                    "Traumatología",
                    "Odontología",
                    "Oftalmología",
                    "Clínica Médica",
                    "Ginecología",
                    "Dermatología",
                    "Nutrición",
                ],
                "profesionales": [
                    "Dra. Luciana Fernández (Cardiología)",
                    "Dr. Martín Ocampo (Traumatología)",
                    "Dra. Carla Domínguez (Pediatría)",
                    "Dr. Sebastián Ríos (Clínica Médica)",
                    "Dra. Valentina Peralta (Dermatología)",
                    "Dr. Ignacio Ferreyra (Oftalmología)",
                ],
                "horarios": [
                    "08:00", "08:30", "09:00", "09:30", "10:00", "10:30",
                    "11:00", "11:30", "12:00", "14:00", "14:30", "15:00",
                    "15:30", "16:00", "16:30", "17:00", "17:30", "18:00",
                    "18:30", "19:00",
                ],
            }
        )
        return context


class ContactoView(TemplateView):
    """Contacto e Institucional (/contacto/): consultas + panel lateral."""
    template_name = "contacto.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "clinica": CLINICA,
                "titulo_pagina": "Contacto e Institucional",
            }
        )
        return context
