"""
Your module description
"""

# Bienvenida al juego de Adivina el Número
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# Importar el módulo random para generar un número aleatorio
import random

# Generar un número aleatorio entre 1 y 10
number = random.randint(1,10)

# Inicializar la variable para rastrear si el usuario adivinó correctamente
isGuessRight = False

# Bucle while para permitir al usuario adivinar el número
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ") # Solicitar al usuario un número
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess)) # Mensaje de victoria
        isGuessRight = True # Cambiar la bandera a Verdadero para salir del bucle
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess)) # Mensaje de intento fallido
