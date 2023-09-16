

# 1) **Multiplos de 3 y 5**: Genera una lista de los múltiplos de 3 y 5 en el rango del 1 al 50 usando comprensión de listas.
#[expression for element in iterable]

multiplos_3_5 = [numero for numero in range (0,50) if numero % 3 == 0 and numero % 5 == 0]
print(multiplos_3_5)

#FELICIDADES Y SIN AYUDA, de a poco se puede :), ust practice a lot

#2 Palabras más largas: Dada la lista de palabras: ["Carmona","Carrusel","carro","Caro","Piel","Cafe","Miguel","Barro","Piso"], crea una nueva lista que contenga las palabras con más de 5 letras utilizando comprensión de listas.

palabras= ["Carmona","Carrusel","carro","Caro","Piel","Cafe","Miguel","Barro","Piso"]
palabras_largas =[palabra for palabra in palabras if len(palabra)>5]
print(palabras_largas)

#olvidaste poner el print pero tuvo piola :3

# 3. **Números primos**: Crea una lista de los números primos hasta 1001 usando comprensión de listas.


def es_primo(numero)->bool:
    if numero <= 1:
        return False
    else:
        for i in range(2, int(numero**0.5)+1):
            if numero % i == 0:
                return False
            else:
                return True


numeros_primos=[numero for numero in range(2,1001) if es_primo(numero)]
print(numeros_primos)


# 4. Crea una lista que contenga la la división de los numeros de 1 al 41 con los numeros del 120 a 160

division_pro=[(numero1 / numero2) for numero1 in range(1,41) for numero2 in range (120,160) ]

print(division_pro)

