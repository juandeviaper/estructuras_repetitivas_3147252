#DICCIONARIOS
#Son colecciones de datos
#Cada elemento en un diccionario se puede dividir en dos partes:
# # 1. Clave: el nombre del elemento o propiedad
# ## 2. Valor: El valor del diccionario
#Ejemplo de diccionario
#Para caracterizar 

pais = {
    "nombre":"Colombia",
    "capital":"Bogotá",
    "idioma":"Español",
    "poblacion": 51   ,
    "superficie" : 1141748,
    "moneda":"peso comlombiano",
    "gentilicio" : "colombiano",
    "ciudades" :[
        "Bogotá",
        "Medellin",
        "Barranquilla",
        "Cali",
        "Cartagena"]
}

#acceder a propiedades:
print ("Capital de Colombia:" , pais["capital"])
print ("Y se habla:" , pais["idioma"])
print ("Su capital es:" , pais["capital"])
print ("Su gentilicio es:", pais["gentilicio"])
print ("Habitantes:" , pais["poblacion"])
print ("Sus principales ciudades son:")
for ciudad in pais["ciudades"]:
    print(ciudad)