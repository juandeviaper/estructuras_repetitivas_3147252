# Colección de países
paises = [
    {
        "nombre": "Colombia",
        "capital": "Bogotá",
        "moneda": "peso colombiano",
        "ciudades": 
        [
            {
                "nombre": "Bogotá",
                "poblacion": 8.5,
                "fundacion": 1538,
            },
            {
                "nombre": "Medellín",
                "poblacion": 2.5,
                "fundacion": 1616,
            },
            {
                "nombre": "Barranquilla",
                "poblacion": 1.2,
                "fundacion": 1629,
            },
            {
                "nombre": "Cali",
                "poblacion": 2.5,
                "fundacion": 1536
            },
            {
                "nombre": "Cartagena",
                "poblacion": 1.0,
                "fundacion": 1533
            }
        ]
    },
    {
        "nombre": "Perú",
        "capital": "Lima",
        "moneda": "Sol",
        "ciudades": [
            {
                "nombre": "Lima",
                "poblacion": 9.7,
                "fundacion": 1535,
            },
            {
                "nombre": "Cuzco",
                "poblacion": 0.4,
                "fundacion": 1100,
            }
        ]
    },
    {
        "nombre": "Inglaterra",
        "capital": "Londres",
        "moneda": "Libra esterlina",
        "ciudades": 
        [
            {
                "nombre": "Manchester",
                "poblacion": 0.5,
                "fundacion": 79,
            },
            {
                "nombre": "Bristol",
                "poblacion": 0.5,
                "fundacion": 1155,
            },
            {
                "nombre": "Oxford",
                "poblacion": 0.15,
                "fundacion": 1096,
            }
        ]
    },
    {
        "nombre": "España",
        "capital": "Madrid",
        "moneda": "Euro",
        "ciudades":
        [
            {
                "nombre": "Barcelona",
                "poblacion": 1.6,
                "fundacion": 15,
            },
            {
                "nombre": "Toledo",
                "poblacion": 0.8,
                "fundacion": 192,
            },
            {
                "nombre": "Valencia",
                "poblacion": 0.8,
                "fundacion": 138,
            }
        ]
    }
]

# Iterar cada país
print("---------------------")
print("Recorrido de países")
print("---------------------")
for pais in paises:
    print("Nombre:", pais["nombre"])    
    print("Capital:", pais["capital"])
    print("Moneda:", pais["moneda"])
    print("Ciudades principales de", pais["nombre"])
    for ciudad in pais["ciudades"]:
        print("-- Ciudad:", ciudad["nombre"])
        print("   Población:", ciudad["poblacion"], "millones")
        print("   Fundación:", ciudad["fundacion"])
    print("---------------------")