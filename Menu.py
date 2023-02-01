salir=False
while not salir:
    print("MENU")
    print("1) Crear lista")
    print("2) Añadir elemento")
    print("3) Eliminar elemento")
    print("4) Modificar elemento")
    print("5) Mostrar datos")
    print("6) Mostar datos de forma inversa")
    print("7) Limpiar lista")
    print("8) Borrar lista")
    print("9) Salir del MENU")
    op=input("\n Elige una de la opciones: ")
                
        
    if(op=='1'):
        print("Crear lista")
        if 'lista' in locals():
            print("Sea creado la lista")
        else:
            lista=[]
            print("lista creada")

    elif(op=='2'):
        print("Añadir elemento")
        if 'lista' in locals():
            ll=input("ingresa elemento")
            lista.append(ll)
            print("Sea ingresado")
        else:
            print("La Lista no existe")
            

    elif(op=='3'):
        print("Eliminar elemento")
        if 'lista' in locals():
            lista[0]=''
            print("Elemento Vacio")
        else:
            print("No puede eliminar un elemento que no existe")

    elif(op=='4'):
        print("Modificar elemento")
        if 'lista' in locals():
            lista[0]=input('el sustituto')
            print("Sea Modificado el elemento")
        else:
            print("La lista no exist")

    elif(op=='5'):
        print("Mostrar datos")
        if 'lista' in locals():
            print(lista)
        else:
            print("La lista no existe")

    elif(op=='6'):
        print("Mostar datos de forma inversa")
        if 'lista' in locals():
            for x in reversed(lista):
                print(x)
        else:
            print("La lista no existe")

    elif(op=='7'):
        print("Limpiar lista")
        if 'lista' in locals():
            del(lista)
            lista=[]
            print("Lista Vacia")
        else:
            print("No puedes vaciar una lista que no existe")

    elif(op=='8'):
        print("Borrar lista")
        if 'lista' in locals():
            del(lista)
            print("Sea Borrardo la lista")
        else:
            print("No puedes borrar una lista que no existe")

    elif(op=='9'):
        salir=True
    else:
        print("Esta opcion no existe eliga de nuevo")
