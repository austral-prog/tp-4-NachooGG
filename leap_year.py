def leap_year():
    anio = int(input())
    if (anio // 400) or (anio % 4 == 0) :
        print(f"El año {anio} es bisiesto")
    else : 
        print(f"El año {anio} no es bisiesto"))
