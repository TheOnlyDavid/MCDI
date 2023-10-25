import sys

word_counts = {}

# Función para reducir y contar las palabras
def reduce_function(word, counts):
    if word in word_counts:
        word_counts[word] += int(counts[0])
    else:
        word_counts[word] = int(counts[0])

# Procesar la entrada
for line in sys.stdin:
    word, count = line.strip().split('\t')
    reduce_function(word, [count])

# Imprimir el resultado
for word, count in word_counts.items():
    print(f"{word}\t{count}")
