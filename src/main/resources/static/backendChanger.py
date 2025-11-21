import os
import shutil

# URL vieja y nueva
URL_ANTIGUA = "http://localhost:8080"
URL_NUEVA = "http://mi-backend:5000"

CARPETA_PROYECTO = "."

def reemplazar_url():
    for carpeta, _, archivos in os.walk(CARPETA_PROYECTO):
        for archivo in archivos:
            if archivo.endswith(".dart"):
                ruta_archivo = os.path.join(carpeta, archivo)

                with open(ruta_archivo, "r", encoding="utf-8") as f:
                    contenido = f.read()

                if URL_ANTIGUA in contenido:
                    backup = ruta_archivo + ".backup"
                    shutil.copyfile(ruta_archivo, backup)

                    contenido_nuevo = contenido.replace(URL_ANTIGUA, URL_NUEVA)

                    with open(ruta_archivo, "w", encoding="utf-8") as f:
                        f.write(contenido_nuevo)

                    print(f"✔ Reemplazada URL en: {ruta_archivo}")

if __name__ == "__main__":
    print("Iniciando reemplazo de URLs en archivos .dart…")
    reemplazar_url()
    print("Proceso completado.")
