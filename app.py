# Asegúrate de que exista un archivo __init__.py en las carpetas 'controllers' y 'views' para que Python las reconozca como paquetes.
from controllers.controlador import iniciar_app

def main(iniciar_app=iniciar_app):
    try:
        print("Iniciando Sistemas de Parqueadero")
        iniciar_app()
    except KeyboardInterrupt:
        print("Gracias por usar el parqueadero")
        print("Adiós")
        
if __name__ == "__main__":
    main()