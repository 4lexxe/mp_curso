def leer_electrodomesticos():
    try:
        archivo=open("electrodomesticos.txt","r",encoding= "UTF-8")
        lineas=archivo.readlines()
        archivo.close()
    except FileNotFoundError:
        archivo=open("electrodomesticos.txt", "w", encoding="utf-8")    
        archivo.write("E001;2026-03-10;Heladera;Samsung;Maria Lopez;entregado;350000\n")
        archivo.write("E002;2026-03-11;Lavarropas;LG;Carlos Perez;pendiente;420000\n")
        archivo.write("E003;2026-03-12;Microondas;BGH;Ana Gomez;entregado;150000\n")
        archivo.write("E004;2026-03-13;Televisor;Sony;Juan Diaz;cancelado;600000\n")
        archivo.write("E005;2026-03-14;Aspiradora;Philips;administrador;entregado;120000\n")
        archivo.close()
        archivo=open("electrodomesticos.txt","r",encoding="utf-8")
        lineas=archivo.readlines()
        archivo.close()
    return lineas    
def proceso_de_datos():
    listas=leer_electrodomesticos()
    lista_procesada=[]

    for lista in listas:
        datos=lista.strip().split(";")
        lista_procesada.append(datos)
    return lista_procesada
def listar_electrodomesticos():
    datos=proceso_de_datos()
    año_mes=input("electrodomesticos vendidos en un año que año quiere saber ingrese en este formato YYYY-MM:")
    for dato in datos:
        fecha=dato[1]
        usuario=dato[4]
        if fecha.startswith(año_mes)and usuario!="administrador"and dato[5].lower()=="entregado".lower():
            print(f"producto:{dato[2]} cliente:{dato[4]} estado:{dato[5]}")   
            
def productos_vendidos_en_total():
    datos=proceso_de_datos()
    cont=0
    marca=input("ingrese la marca para saber cuantoss productos de esa marca fueros vendidos")
    for dato in datos:
        if dato[3].lower()==marca.lower():
            cont+=1
    print(f"los productos vendidos por la marca:{marca} es de: {cont}") 
def electrodomesticos_no_ENTREGADOS():
    datos=proceso_de_datos()
    for dato in datos:
        if dato[5].lower()!="entregado".lower():
            print(f"electrodomesticos no entregados Codigo:{dato[0]} producto:{dato[2]} cliente:{dato[4]} estado:{dato[5]}")
def top_3_clientes():
    datos=proceso_de_datos()
    clientes=[]     
    for dato in datos:
        usuario=dato[4] 
        clientes.append(usuario)
    clientes_finales=[]
    for cliente in clientes:
        if cliente not in clientes_finales:
            cantidad=clientes.count(cliente) 
            clientes_finales.append([cliente,cantidad])
    for i in range(len(clientes_finales)):
        for j in range(0, len(clientes_finales)- i - 1):
            if clientes_finales[j]<clientes_finales[j+1]:
                clientes_finales[j],clientes_finales[j+1]=clientes_finales[j+1],clientes_finales[j]
    print("top de tres clientes")            
    for elemento in clientes_finales[:3]:
        print(f"cliente:{elemento[0]} cantidad de compras:{elemento[1]}")
    
def informe_por_marca():
    listas= proceso_de_datos()
    lista_marca=[]
        
    for linea in listas:
        marca=linea[3]
        if marca not in lista_marca:
                lista_marca.append(marca)
    for marca in lista_marca:
        with open(f"informe_{marca}.txt","w",encoding="utf-8"):
                total_de_productos_vendidos=0
                total_entregados=0
                total_pendientes=0
                total_cancelados=0
                producto_mas_vendido=""
                recaudación_total_de_la_marca=0
                marca_mayor=0
            
    for lista in listas:
                if lista[5].lower()!="cancelado".lower():
                    total_de_productos_vendidos+=1
                if lista[5].lower()=="entregado".lower() :
                    total_entregados+=1
                if lista[5].lower()=="pendiente".lower(): 
                    total_pendientes+=1
                if lista[5].lower()=="cancelado".lower():
                    total_cancelados+=1
    for l in lista_marca:
                cantidad=lista_marca.count(l)
                if cantidad>marca_mayor:
                    marca_mayor=cantidad
                    producto_mas_vendido=l
    for lista in listas:
                monto_venta= int(lista[6])
                recaudación_total_de_la_marca+= int(monto_venta)
    with open(f"informe_{marca}.txt","w",encoding="utf-8") as archivo:
            archivo.write(f"marca:{marca}\n")
            archivo.write(f"Total de productos vendidos:{total_de_productos_vendidos}")
            archivo.write(f"Total entregados:{total_entregados}")
            archivo.write(f"Total pendientes:{total_pendientes}")
            archivo.write(f"Total cancelados:{total_cancelados}")
            archivo.write(f"Producto más vendido:{producto_mas_vendido}") 
            archivo.write(f"Recaudación total de la marca:{recaudación_total_de_la_marca}") 
def validar_codigo(codigo):
    listas= proceso_de_datos()
    for lista in listas:
        if codigo==lista[0]:
            return True
    return False

def validar_estado(estado):
    listas= proceso_de_datos()
    
    for lista in listas:
        if estado[5]!="entregado" and estado[5]!="pendiente" and estado[5]!="cancelado":
            return False
    return True
     
def modificacion_del_producto():
    listas= proceso_de_datos()
    codigo=input("ingrese el codigo del produto:")
    estado=input("ingrese el estado del prioducto")
    pos=validar_codigo(codigo)
    if validar_estado(estado) and validar_estado(estado):
        for lista in listas:
            if lista[0]==codigo:
               lista[5]= estado.lower()
        archivo= open("informe_{marca}.txt","w",encoding="utf-8")          
        for lista in listas:
          archivo.write(lista[0] + "," +lista[1] + "," +str(lista[2]) + "," +lista[3] + "," +str(lista[4]) + "," +lista[5] + "\n"  )

        archivo.close()

print("Producto modificado correctamente")   
            
#principal   
leer_electrodomesticos()
proceso_de_datos()
listar_electrodomesticos()  
productos_vendidos_en_total()    
electrodomesticos_no_ENTREGADOS()                  
top_3_clientes()
informe_por_marca()
modificacion_del_producto()