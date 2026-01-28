from auth import iniciar_sesion
from cafeteria import tomar_pedido, imprimir_ticket, entregar_pedido

def main():
    print(" CAFETERÍA DMITRIEV ".center(50,'*'))
    print("\nBienvenido al sistema de autoservicio.")

    # Configuración inicial
    credenciales = {"usuario": "josy", "contrasena": "josy"} 
    menu = {"cafe": 6, "sandwich": 10, "cheesecake": 8, "expreso": 4, "te": 8}
    lista_productos = list(menu.keys())

    if iniciar_sesion(credenciales, 3): 
        print("\n" + " INICIANDO PEDIDO ".center(50,'*'))
        carrito = tomar_pedido(menu, lista_productos)

        if carrito:
            imprimir_ticket(carrito, menu)
            entregar_pedido(carrito)
    else:
        print("\nAcceso denegado. Límite de intentos alcanzado.")

if __name__ == "__main__":
    main() 