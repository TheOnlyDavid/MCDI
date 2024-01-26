# Inicialización
flag = [False, False]  # Dos banderas, una para cada proceso
turn = 0  # Variable de turno

# Proceso 0
flag[0] = True
turn = 1
while flag[1] and turn == 1:
    pass

# Sección crítica del Proceso 0
# ...

flag[0] = False

# Proceso 1
flag[1] = True
turn = 0
while flag[0] and turn == 0:
    pass

# Sección crítica del Proceso 1
# ...

flag[1] = False
