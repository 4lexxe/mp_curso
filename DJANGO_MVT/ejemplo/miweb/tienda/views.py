from django.shortcuts import render
from django.contrib import messages

# Datos iniciales para la tienda TechNova
PRODUCTOS = [
    {
        "id": 1,
        "nombre": "Laptop Gamer ASUS ROG Zephyrus G16",
        "categoria": "Laptops",
        "descripcion": "Intel Core i9 14900HX, RTX 4080 12GB, 32GB RAM DDR5, 1TB SSD NVMe, Pantalla 240Hz OLED.",
        "precio": 2499999,
        "precio_anterior": 2799999,
        "descuento": "15% OFF",
        "imagen": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&w=600&q=80",
        "badge": "OFERTA DESTACADA",
        "destacado": True,
    },
    {
        "id": 2,
        "nombre": "Placa de Video NVIDIA RTX 4070 Ti Super",
        "categoria": "Componentes",
        "descripcion": "16GB GDDR6X, Ray Tracing de 3ra gen, DLSS 3.5, ideal para 4K Ultra y creación de contenido.",
        "precio": 1150000,
        "precio_anterior": 1290000,
        "descuento": "10% OFF",
        "imagen": "https://images.unsplash.com/photo-1587202377405-836165b1040a?auto=format&fit=crop&w=600&q=80",
        "badge": "MÁS VENDIDO",
        "destacado": True,
    },
    {
        "id": 3,
        "nombre": 'Monitor Gamer Samsung Odyssey OLED 34"',
        "categoria": "Monitores",
        "descripcion": "Curvo 1800R, WQHD 175Hz, 0.03ms tiempo de respuesta, HDR True Black 400, AMD FreeSync Premium Pro.",
        "precio": 1450000,
        "precio_anterior": 1690000,
        "descuento": "14% OFF",
        "imagen": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=600&q=80",
        "badge": "PREMIUM",
        "destacado": True,
    },
    {
        "id": 4,
        "nombre": "Teclado Mecánico Corsair K100 RGB Wireless",
        "categoria": "Periféricos",
        "descripcion": "Switches Cherry MX Ultra Low Profile, chasis de aluminio cepillado, batería de hasta 200h.",
        "precio": 280000,
        "precio_anterior": 330000,
        "descuento": "15% OFF",
        "imagen": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=600&q=80",
        "badge": "PROMO",
        "destacado": True,
    },
    {
        "id": 5,
        "nombre": "Auriculares HyperX Cloud III Wireless",
        "categoria": "Audio",
        "descripcion": "Audio espacial DTS Headphone:X, transductores de 53 mm angulados, hasta 120 horas de batería.",
        "precio": 195000,
        "precio_anterior": 230000,
        "descuento": "15% OFF",
        "imagen": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?auto=format&fit=crop&w=600&q=80",
        "badge": "POPULAR",
        "destacado": True,
    },
    {
        "id": 6,
        "nombre": "Mouse Inalámbrico Logitech G Pro X Superlight 2",
        "categoria": "Periféricos",
        "descripcion": "Sensor Hero 2 32K DPI, switches híbridos Lightforce, ultraliviano 60 gramos, color negro mate.",
        "precio": 165000,
        "precio_anterior": 190000,
        "descuento": "13% OFF",
        "imagen": "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?auto=format&fit=crop&w=600&q=80",
        "badge": "NUEVO",
        "destacado": True,
    },
]

EQUIPO = [
    {
        "nombre": "Alex Rivera",
        "cargo": "Fundador & CEO",
        "especialidad": "Estrategia Digital y Arquitectura Web",
        "bio": "Especialista en tecnología y e-commerce con pasión por acercar el mejor hardware a la comunidad gamer y profesional.",
        "imagen": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80",
        "email": "alex.rivera@technova.com",
    },
    {
        "nombre": "Sofía Méndez",
        "cargo": "Directora de Tecnología (CTO)",
        "especialidad": "Infraestructura Cloud y Desarrollo Django",
        "bio": "Ingeniera de software enfocada en rendimiento web, seguridad en transacciones y experiencia de usuario fluida.",
        "imagen": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=400&q=80",
        "email": "sofia.mendez@technova.com",
    },
    {
        "nombre": "Lucas Gómez",
        "cargo": "Especialista en Hardware & Soporte",
        "especialidad": "Armado de PCs Gamer y Benchmarks",
        "bio": "Técnico apasionado por la refrigeración líquida, overclocking y asesoramiento técnico personalizado.",
        "imagen": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80",
        "email": "lucas.gomez@technova.com",
    },
    {
        "nombre": "Valentina Torres",
        "cargo": "Líder de E-commerce y Atención",
        "especialidad": "Logística, Envíos y Experiencia del Cliente",
        "bio": "Comprometida con brindar la mejor atención posventa, envíos en 24 horas y resolución ágil de consultas.",
        "imagen": "https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=400&q=80",
        "email": "valentina.torres@technova.com",
    },
]

INFO_TIENDA = {
    "nombre": "TechNova",
    "slogan": "Tu tienda de tecnología y hardware de alto rendimiento",
    "direccion": "Av. Corrientes 1420, Buenos Aires, Argentina",
    "telefono": "+54 11 5234-8900",
    "whatsapp": "+54 9 11 9876-5432",
    "email": "contacto@technova.com",
    "horarios": "Lunes a Viernes de 09:00 a 19:00 hs | Sábados de 10:00 a 14:00 hs",
    "descripcion_corta": "Somos el e-commerce referente en tecnología, computadoras, componentes y periféricos de última generación.",
}


def index(request):
    """Página principal del sitio (index.html)"""
    context = {
        "tienda": INFO_TIENDA,
        "productos_destacados": PRODUCTOS,
        "promociones": [
            {
                "titulo": "Semana Gamer TechNova",
                "subtitulo": "Hasta 25% OFF en placas de video y periféricos seleccionados",
                "badge": "PROMO LIMITADA",
            },
            {
                "titulo": "Envíos Gratis a Todo el País",
                "subtitulo": "En compras superiores a $150.000 con entrega prioritaria",
                "badge": "ENVÍO GRATIS",
            },
            {
                "titulo": "6 Cuotas Sin Interés",
                "subtitulo": "Con todas las tarjetas bancarias participantes",
                "badge": "FINANCIACIÓN",
            },
        ],
    }
    return render(request, "index.html", context)


def acercade(request):
    """Página institucional (acercade.html)"""
    context = {
        "tienda": INFO_TIENDA,
        "equipo": EQUIPO,
        "mision": "Proveer soluciones tecnológicas de vanguardia, acercando hardware y periféricos de la máxima calidad a entusiastas, creadores de contenido y profesionales de toda la región con asesoramiento experto.",
        "vision": "Convertirnos en la plataforma de comercio electrónico en tecnología más confiable y elegida de Latinoamérica, destacada por la excelencia en servicio, innovación y transparencia.",
        "historia": (
            "TechNova nació en 2021 a partir del entusiasmo de un grupo de apasionados por la computación y "
            "el desarrollo de software. Comenzamos como un pequeño proyecto de ensamble de computadoras "
            "personalizadas y, gracias a la confianza de nuestra comunidad gamer y profesional, hoy nos "
            "consolidamos como una tienda en línea moderna, con catálogo en constante expansión, convenios "
            "directos con fabricantes líderes (NVIDIA, ASUS, Corsair, Logitech) y miles de pedidos entregados "
            "con éxito en todo el país."
        ),
        # Video de YouTube sobre comercio electrónico y tecnología
        "video_youtube_id": "y881t8ilMyc",  # E-commerce y tecnología del futuro
    }
    return render(request, "acercade.html", context)


def contacto(request):
    """Página de contacto (contacto.html)"""
    mensaje_enviado = False
    nombre_contacto = ""

    if request.method == "POST":
        nombre_contacto = request.POST.get("nombre", "").strip()
        email_contacto = request.POST.get("email", "").strip()
        asunto_contacto = request.POST.get("asunto", "Consulta general").strip()
        mensaje_contacto = request.POST.get("mensaje", "").strip()

        if nombre_contacto and email_contacto and mensaje_contacto:
            messages.success(
                request,
                f"¡Muchas gracias {nombre_contacto}! Tu mensaje ha sido recibido con éxito. "
                f"Te responderemos a la brevedad al correo {email_contacto}.",
            )
            mensaje_enviado = True
        else:
            messages.error(
                request,
                "Por favor, completa todos los campos requeridos (Nombre, Email y Mensaje).",
            )

    context = {
        "tienda": INFO_TIENDA,
        "mensaje_enviado": mensaje_enviado,
        "nombre_contacto": nombre_contacto,
    }
    return render(request, "contacto.html", context)


def productos(request):
    """Página de catálogo de productos (productos.html) - Complemento Sprint 1/2"""
    context = {
        "tienda": INFO_TIENDA,
        "productos": PRODUCTOS,
        "categorias": ["Laptops", "Componentes", "Monitores", "Periféricos", "Audio"],
    }
    return render(request, "productos.html", context)
