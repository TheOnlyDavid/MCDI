import sys
import re

# Función para dividir una línea en palabras y emitir pares (palabra, 1)
def map_function(line):
    words = re.findall(r'\w+', line)  # Encuentra palabras usando expresiones regulares
    for word in words:
        print(f"{word.lower()}\t1")  # Emitir palabra y 1

# Procesar líneas de entrada
for line in sys.stdin:
    map_function(line)
