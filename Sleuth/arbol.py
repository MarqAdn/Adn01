def dibujar_arbol(a, b):
    for i in range(1, a+1):
        espacio = " "*(a-i)
        arbol = "*"*(i*2-1)
        print(espacio + arbol, "\\")
        
    espacio = " "*(a-1)
    tronco = "|*|"
    for i in range(b-1):
        print(espacio + tronco)

altura_triangulo = 5
altura_tronco = 3

dibujar_arbol(altura_triangulo, altura_tronco)