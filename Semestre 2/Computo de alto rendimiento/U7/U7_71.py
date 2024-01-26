# Inicialización
flag = [False, False]  # Dos banderas, una para cada proceso
turn = 0  # Variable de turno

# Proceso 0
flag[0] = True
while flag[1]:
    if turn == 1:
        flag[0] = False
        while turn == 1:
            pass
        flag[0] = True

# Sección crítica del Proceso 0
# ...

turn = 1
flag[0] = False

# Proceso 1
flag[1] = True
while flag[0]:
    if turn == 0:
        flag[1] = False
        while turn == 0:
            pass
        flag[1] = True

# Sección crítica del Proceso 1
# ...

turn = 0
flag[1] = False
