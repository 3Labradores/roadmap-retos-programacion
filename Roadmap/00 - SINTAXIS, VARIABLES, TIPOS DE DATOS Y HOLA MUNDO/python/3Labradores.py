# https://github.com/3Labradores/roadmap-retos-programacion/new/main/Roadmap/00%20-%20SINTAXIS%2C%20VARIABLES%2C%20TIPOS%20DE%20DATOS%20Y%20HOLA%20MUNDO/python

""" modod alternativo de escribir comentarios, pero igual puede considerarse una string que python ignora

"""

# Manera mas comun de comentar en python es usando el simbolo de gato

variable_string = "Variable de tipo string"
variable_booleana = True
variable_int = 2 # Pyhton igual reconoce esta parte solamente como comentario y la parte anterior como mi variable
variable_float = 2.04
variable_compleja = -1 + 2j
variable_lista = ["var", "numero", "lista"]
variable_tupla = ("var", "numer", "list")
variable_rango = range(2,17,3) 
variable_set = {1,3,5,8,90,4,5,8}
variable_dictionario = {"Nombre": "Sara","Edad": 27,  "Documento": 1003882}
variavle_frozen = frozenset([1, 2, 3])

print(variable_booleana, variable_compleja, variable_dictionario, variable_float, variable_int, variable_lista, variable_rango, variable_set, variable_string, variable_tupla)
