# Asegúrate de que exista un archivo __init__.py en las carpetas 'controllers', 'models' y 'views'
# para que Python las reconozca como paquetes. Ejecuta siempre desde la carpeta raíz: python app.py
from controllers.controlador import iniciar_app


def main():
    try:
        print("Iniciando Sistema de Parqueadero")
        iniciar_app()
    except (KeyboardInterrupt, EOFError):
        print("\nGracias por usar el parqueadero")
        print("Adiós")


if __name__ == "__main__":
    main()
