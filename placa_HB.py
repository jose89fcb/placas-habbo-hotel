import requests

# URL que contiene el archivo de texto
url = "https://www.habbo.es/gamedata/external_flash_texts/d36bb4a27a4b904aaf85b11d61a718e1e3624b5f"

# Solicitar al usuario que ingrese el código de la placa
codigo_placa = input("Ingrese el código de la placa (por ejemplo, HW1): ")

# Realizar una solicitud GET para obtener el contenido del archivo de texto
respuesta = requests.get(url)

# Comprobar si la solicitud fue exitosa
if respuesta.status_code == 200:
    # Obtener el contenido del archivo de texto
    contenido_texto = respuesta.text

    # Buscar el nombre y la descripción de la placa correspondiente
    inicio_nombre_placa = contenido_texto.find(f"badge_name_{codigo_placa}")
    inicio_desc_placa = contenido_texto.find(f"badge_desc_{codigo_placa}")

    if inicio_nombre_placa != -1 and inicio_desc_placa != -1:
        inicio_nombre_placa += len(f"badge_name_{codigo_placa}=")
        inicio_desc_placa += len(f"badge_desc_{codigo_placa}=")

        fin_nombre_placa = contenido_texto.find("\n", inicio_nombre_placa)
        fin_desc_placa = contenido_texto.find("\n", inicio_desc_placa)

        nombre_placa = contenido_texto[inicio_nombre_placa:fin_nombre_placa].strip()
        desc_placa = contenido_texto[inicio_desc_placa:fin_desc_placa].strip()

        # Imprimir los resultados
        print(f"Nombre de la placa {codigo_placa}: {nombre_placa}")
        print(f"Descripción de la placa {codigo_placa}: {desc_placa}")
    else:
        print(f"No se encontró información para la placa {codigo_placa}")
else:
    print("Error al obtener la información de la URL")
