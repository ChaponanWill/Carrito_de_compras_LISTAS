#Autor: @ChaponanWill
import time
time.sleep(0.3)

lista_productos=[]
#Función: Lista de productos
def lista():
    return("""
        🖖BIENVENIDO A "SUPERTODO"🖖
        1. Ver lista.
        2. Agregar un producto a la lista.
        3. Agregar varios productos a mi lista.
        4. Eliminar productos de la lista.
        5. Detalle de carrito
        6. Salir.
        """)
    time.sleep(1)
#Función: Modificar listas de productos
def productos(eleccion):
    #VER LISTA
    if eleccion=="1":
        if lista_productos==[]:
            return "❌No tienes productos en la lista❌"
        else:
            return f"☑️Tu lista de productos es \n {lista_productos}"
    #AGREGANDO UN SOLO PRODUCTO
    elif eleccion=="2":
        i=len(lista_productos)
        agregar_elemento=input(f"➡️Introduce el '0' (solo número cero) para salir de esta opción ... \nIntroduce el nombre del {i+1}° producto: ")
        if agregar_elemento=="0":
            return "No se agrego producto❌"
        if agregar_elemento in lista_productos:
            confirmar=input("Ya tienes agregado este producto. ¿Deseas volver a agregarlo?(si/no): ").lower()
            if confirmar=="si":
                lista_productos.append(agregar_elemento)
                print("Agregando producto ...")
                time.sleep(1)
                return f"""
                ☑️ {agregar_elemento} ... Producto agregado exitosamente
                """
            else:
                return "Elemento No agregado ❌❌"
        else:     
            lista_productos.append(agregar_elemento)
            print("Agregando producto ...")
            time.sleep(1)
            return f"""
            ☑️ {agregar_elemento} ... Producto agregado exitosamente
            """
    #AGREGANDO VARIOS ELEMENTOS
    elif eleccion=="3":
        i=len(lista_productos)
        while True:
            i+=1
            agregar_elemento=input(f"➡️Introduce el '0' (solo número cero) para salir de esta opción ... \nIntroduce el nombre del {i}° producto: ")
            if agregar_elemento=="0":
                return("Saliendo de agregar productos❌")
                break
            if agregar_elemento in lista_productos:
                confirmar=input("Ya tienes agregado este producto. ¿Deseas volver a agregarlo?(si/no): ").lower()
                if confirmar=="si":
                    lista_productos.append(agregar_elemento)
                    print("Agregando producto ...")
                    time.sleep(1)
                    print(f"""
                    ☑️ {agregar_elemento} ... Producto agregado exitosamente
                    """)
                else:
                    print("Elemento No agregado ❌❌")
            else:     
                lista_productos.append(agregar_elemento)
                print("Agregando producto ...")
                time.sleep(1)
                print(f"""
                ☑️ {agregar_elemento} ... Producto agregado exitosamente
                """)
    #ELIMINAR PRODUCTOS:
    elif eleccion=="4":
        while True:
            if lista_productos==[]:
                return "❌No tienes productos en la lista❌"
                break;
            else:
                print(f"☑️Tu lista de productos es: \n {lista_productos}")
                eliminar=input("➡️Introduce el '0' (solo número cero) para salir de esta opción ... \n INTRODUCE EL PRODUCTO A ELIMINAR: ")
                time.sleep(0.4)
                if eliminar=="0":
                    return "Saliendooo...."
                    break;
                if eliminar in lista_productos:
                    while True:
                        confirmar=input(f"Seguro que quieres eliminar {eliminar} de tu lista de productos(si/no): ").lower()
                        time.sleep(0.4)
                        if confirmar=="si":
                            lista_productos.remove(eliminar)
                            print(f"☑️{eliminar} ha sido correctamente eliminado ... ")
                            print("------------------------------------------------------")
                            break;  
                        elif confirmar=="no":
                            print("NO SE ELIMINO PRODUCTO")
                            break;
                        else:
                            print("---Confirmar---")
                        time.sleep(0.4)
                else:
                    print("--------------------------")
                    print("Producto inválido 🙅‍♂️")
                    print("--------------------------")

    #DETALLE DE CARRITO
    elif eleccion=="5":
        if lista_productos==[]:
                return "❌No tienes productos en el carrito❌"
        else:
            print("\tPRODUCTOS DEL CARRITO DE COMPRAS:")
            for i in lista_productos:
                print(f"\t✅ {i}")
            return "   🛒EXCELENTE CARRITO...🛍️"

    #OPCIÓN INVÁLIDA
    else:
        return "👁️OPCIÓN INVÁLIDA👁️"



#PROGRAMA
while True:
    time.sleep(0.5)
    print(lista())
    print("--------------------------------------------------------------------------")
    ingreso_eleccion=input("🏪Ingresa la opción que deseas realizar(Un número): ")
    time.sleep(1)
    #saliendo del programa
    if ingreso_eleccion=="6":
        print("Saliendo del programa ....")
        time.sleep(0.5)
        break;
    print(productos(ingreso_eleccion))
    print("--------------------------------------------------------------------------")