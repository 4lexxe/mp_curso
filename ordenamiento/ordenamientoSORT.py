notas = [8, 4, 10, 7, 5]
#menor a mayor
ordenadas = sorted(notas)
print(ordenadas)

#mayor a menor
ordenadas = sorted(notas, reverse=True)
print(ordenadas)

#mayor a menor
notas.sort(reverse=True)
print(notas)


personas = [
    ["Pedro", 6],
    ["Juan", 8],
    ["Lucia", 9],
    ["Ana", 10]
    ]

personas = sorted(personas, key=lambda persona: persona[1])
print(personas)


#mayor a menor
personas = sorted(personas, key=lambda persona: persona[1], reverse=True)
print(personas)



#.sort()

personas.sort(key=lambda persona:persona[1], reverse=True)
print(personas)



#mostrar los primeros 3 personas con mayor notas


#[  INICIO : HASTA  : PASOS ]
#INICIO = COMIENZA y se incluye el numero, por defecto es 0
#HASTA = TERMINA PERO NO INCLUYE AL NUMERO
#PASOS = CADA CUANTO PASOS
#[:3]   INICIO 0 y un final que termina en 3


