
def iniciar_sesion(credenciales, maximo_intentos): 
    intentos = 0 #Inicializo el contador de intentos fallidos.

    while intentos < maximo_intentos: #Inicia un bucle while que se repite mientras el número de intentos sea menor a 3.
        
        usuario_ingresado = input("Usuario: ")
        contrasena_ingresada = input(f"Ingresa tu contraseña (intento {intentos+1} de {maximo_intentos}): ")
        #pide y muestra el numero de intentos

        if usuario_ingresado == credenciales["usuario"] and contrasena_ingresada == credenciales["contrasena"]:
            print("\n" + "✨ Acceso permitido, ¡Bienvenido! ✨ ".center(50,' '))
            return True
            
        intentos += 1
        if intentos < maximo_intentos: #Verifica si aún quedan intentos disponibles.
            print("Usuario o contraseña incorrecta. Intenta nuevamente.")
            
    return False
