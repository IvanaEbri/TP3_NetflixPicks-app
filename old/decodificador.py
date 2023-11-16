# Diccionario que mapea códigos de dos letras a nombres completos de países
paises = {
    "AR": "Argentina",
    "AU": "Australia",
    "BR": "Brasil",
    "CA": "Canadá",
    "CL": "Chile",
    "CN": "China",
    "CO": "Colombia",
    "DE": "Alemania",
    "EG": "Egipto",
    "ES": "España",
    "FR": "Francia",
    "GB": "Reino Unido",
    "GR": "Grecia",
    "IN": "India",
    "IT": "Italia",
    "JP": "Japón",
    "KR": "Corea del Sur",
    "MX": "México",
    "NG": "Nigeria",
    "NL": "Países Bajos",
    "PE": "Perú",
    "PT": "Portugal",
    "RU": "Rusia",
    "SA": "Arabia Saudita",
    "SE": "Suecia",
    "TH": "Tailandia",
    "TR": "Turquía",
    "US": "Estados Unidos",
    "ZA": "Sudáfrica",
    "BD": "Bangladesh",
    "NG": "Nigeria",
    "PK": "Pakistán",
    "IR": "Irán",
    "IQ": "Iraq",
    "ID": "Indonesia",
    "VN": "Vietnam",
    "PH": "Filipinas",
    "EG": "Egipto",
    "DZ": "Argelia"
}

# Función para obtener el nombre completo del país
def obtener_nombre_pais(codigo):
    return paises.get(codigo, "Desconocido")

# Ejemplo de uso
codigo_pais = "AR"
nombre_completo = obtener_nombre_pais(codigo_pais)



