def line(A, B, X1, X2):
    A = float(input())
    B = float(input())
    X1 = float(input())
    X2 = float(input())
    print(f"El coeficiente A de su ecuacion de la recta es: {A}")
    print(f"El coeficiente B de su ecuacion de la recta es: {B}")
    print(f"El coeficiente X1 de su ecuacion de la recta es: {X1}")
    print(f"El coeficiente X2 de su ecuacion de la recta es: {X2}\n")

    print(f"Para la siguiente ecuacion:\n\tY = {A}X + {B}")
    
    Y_3 = A * X1 + B
    Y_4 = A * X2 + B
    
    print(f"\nDados los siguientes puntos:")
    print(f"\tP1 ({X1}, {Y_3})")
    print(f"\tP2 ({X2}, {Y_4})")
    distancia = ((X2 - X1)**2 + (Y_4 - Y_3)**2)**(1/2)
    print(f"\nLa distancia entre los dos puntos sobre la recta es: {distancia}")
