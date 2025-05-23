import random  #Importa un modulo para elegir caracteres aleatorios
import string  #Contiene conjuntos de caracteres como letras y numeros
import pyperclip  #Permite copiar la contraseña directamente al portapapeles

def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))  #Crea una lista de caracteres aleatorios y los une en una sola cadena
    return contraseña

#ascii_leters incluye mayusculas + minusculas
#digits incluye 0-9
#punctuation incluye simbolos como !@#$%^&*()


def main():
    print("Generador de Contraseñas Fuertes \n")

    #Este print muestra un titulo bonito al ejecutar el programa

    while True:  #while true es para repetir la operación hasta que se introduzca algo válido según premisas
        try:  #try/except detecta si escribe texto en vez de numero (error)
            longitud = int(input("Introduce la longitud de la contraseña (mínimo 8): "))  #si el numero es menor que 8 se vuelve a pedir
            if longitud < 8:
                print("La longitud mínima es 8. Intenta de nuevo.")
                continue
            break  #cuando todo esté bien, se rompe el ciclo con un break
        except ValueError:
            print("Por favor, introduce un número válido.")

    contraseña = generar_contraseña(longitud)  #llama a la función generar_contraseña con la longitud introducida
    pyperclip.copy(contraseña)  #pyperclip para copiar la contraseña automáticamente
    print(f"\n Tu contraseña segura es:\n{contraseña}")  #muestra por pantalla la contraseña generada
    print("La contraseña se ha copiado al portapapeles.")  #informa que ya está copiada y lista para pegar

if __name__ == "__main__":  #esta parte se asegura de que main() se ejecute solo si corres este archivo directamente, no se se importa desde otro
    main()