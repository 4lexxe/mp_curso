def leer_prestemo():
    try:
        archivo=open("prestamos.txt","r",encoding= "UTF-8")
        lineas=archivo.readlines()
        archivo.close()
    except FileNotFoundError:
        archivo=open("prestamos.txt", "w", encoding="utf-8")    
        archivo.write("2025-09-01;Rayuela;Julio Cortázar;Ana Gutierrez;devuelto\n")
        archivo.write("2025-09-02;Cien años de soledad;Gabriel García Marquez;administrador;pendiente\n")
        archivo.write("2025-09-03;Rayuela;Julio Cortázar;Marco Lopez;retrasado\n")
        archivo.write("2025-09-03;El Extranjero;Albert Camus;Carlos Gómez;retrasado\n")
        archivo.close()
        archivo=open("prestamos.txt","r",encoding="utf-8")
        lineas=archivo.readlines()
        archivo.close()
    return lineas    
def proceso_de_datos():
    listas=leer_prestemo()
    lista_procesada=[]

    for lista in listas:
        datos=lista.strip().split(";")
        lista_procesada.append(datos)
    return lista_procesada

def listar_por_fecha():
    
    datos=proceso_de_datos()
    anio=input("ingrese el año que fue prestado el libro")
    mes=input("ingrese la fecha en elque fue prestado el libro")
    for dato in datos:
        fecha=dato[0]
        usuario=dato[3]
        if fecha.startswith(anio+"-"+mes) and usuario!="administrador":
            print(f"libro:{dato[1]}")
            print(f"autor:{dato[2]}")
            print(f"usuario:{usuario}")
            print(f"estado:{dato[4]}")
def solicitud_de_libro_por_autor():
    datos=proceso_de_datos()  
    cont=0
    autor=input("ingrese el nombre del autor").lower()
    for dato in datos:
        if dato[2].lower()==autor.lower():
            cont+=1
    print(f"este autor:{autor} fue solicitado{cont}")
    
def listar_libro_no_devueltos():
    datos=proceso_de_datos()
    print("libros no devueltos")
    for dato in datos:
        if dato[4].lower()!="devuelto".lower():
            print(f"usuario:{dato[3]}, libros no devueltos:{dato[4]}")
def usuarios_solicitados():
    datos=proceso_de_datos()
    usuarios=[]
    for dato in datos:
        usuario=dato[3]
        usuarios.append(usuario)
    lista_final=[]
    for usuario in usuarios:
        if usuario not in lista_final:
            cantidad=usuarios.count(usuario)
            lista_final.append([usuario,cantidad])
    lista_final.sort(key=lambda x:[1])       
    for elemento in lista_final[:3]:
        print(elemento[0],":", elemento[1])

def punto_obligatorio():
    lista=proceso_de_datos()
    lista_autor=[]
    for linea in lista:
        autor= linea[2]
        if autor not in lista_autor:
            lista_autor.append(autor)
    for autor in lista_autor:
        with open(f"informe_{autor}.txt","w",encoding="utf-8"):
            libros_solicitados=0
            libros_devueltos=0
            libros_pendientes=0    
            libros_retrasados=0
        for registro in lista:
            if registro[2]==autor:
                libros_solicitados+=1
                if "devuelto".lower()==linea[4].lower():
                    libros_devueltos+=1
                if "pendiente".lower()==linea[4].lower():
                    libros_pendientes+=1
                if "retrasado".lower()==linea[4].lower(): 
                    libros_retrasados+=1   
        libro_mas_solicitado=""
        libro_mayor=0
        for autor in lista_autor:
            cantidad=lista_autor.count(autor)
            if cantidad>libro_mayor:
                libro_mas_solicitado=cantidad
    with open(f"informe_{autor}.txt","w",encoding="utf-8") as archivo:
        archivo.write(f"autor:{autor}\n")
        archivo.write(f"total de libros solicitados:{libros_solicitados}")
        archivo.write(f"total de libros devueltos:{libros_devueltos}")
        archivo.write(f"total de libros peendientes:{libros_pendientes}")
        archivo.write(f"total de libros retrasados:{libros_retrasados}") 
        archivo.write(f"libro mas solicitado:{libro_mas_solicitado}")  
                 
    print(f"autor:{autor[2]}")               
    print(f"Total de libros solicitados:{libros_solicitados}")
    print(f"Total de libros devueltos:{libros_devueltos}")
    print(f"Total de libros pendientes:{libros_pendientes}") 
    print(f"Total de libros retrasados:{libros_retrasados}") 
    print(f"Libro más solicitado:{libro_mas_solicitado}")
#principal
leer_prestemo() 
proceso_de_datos()
listar_por_fecha()
solicitud_de_libro_por_autor() 
listar_libro_no_devueltos()
usuarios_solicitados()
punto_obligatorio()