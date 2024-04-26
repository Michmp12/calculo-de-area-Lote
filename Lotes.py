import os

list_urbano = []
list_comercial = []
list_campestre = []
sw = True

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def fnt_limpiar():
    limpiar_pantalla()
    print('Autor: Michell Alejandra Mosquera Pacheco')

def fnt_selector(op):
    global sw
    if op == '1':
        limpiar_pantalla()
        fnt_limpiar()
        tipo_lote = input('---TIPO DE LOTE---\n1. Urbano\n2. Comercial\n3. Campestre\n->')
        limpiar_pantalla()
        fnt_limpiar()
        if tipo_lote == '1':
            import os 
            frente = float(input('Ingrese medida del frente del lote: '))
            fondo = float(input('Ingrese medida del fondo del lote: '))
            area = frente * fondo
            mt2 = 25000 * area
            permiso_const = 0.45 * mt2
            total = mt2 + permiso_const
            lote = f"Area:  {area} /Valor del area: $ {mt2} /Permiso de construcción:  {permiso_const} /Valor total: $ {total}"
            list_urbano.append(lote)
            print('Registro exitoso\n')
            enter = input('Presione <Enter> para continuar...')
            fnt_limpiar()

        elif tipo_lote == '2':
            frente = float(input('Ingrese medida del frente del lote: '))
            fondo = float(input('Ingrese medida del fondo del lote: '))
            area = frente * fondo
            mt2 = 60000 * area
            permiso_const = 0.75 * mt2
            total = mt2 + permiso_const
            lote = f"Area:  {area} /Valor del area: $ {mt2} /Permiso de construcción:  {permiso_const} /Valor total: $ {total}"
            list_comercial.append(lote)
            print('Registro exitoso\n')
            enter = input('Presione <Enter> para continuar...')
            fnt_limpiar()

        elif tipo_lote == '3':
            frente = float(input('Ingrese medida del frente del lote: '))
            fondo = float(input('Ingrese medida del fondo del lote: '))
            area = frente * fondo
            mt2 = 35000 * area
            permiso_const = 0.15 * mt2
            total = mt2 + permiso_const
            lote = f"Area:  {area} /Valor del area: $ {mt2} /Permiso de construcción:  {permiso_const} /Valor total: $ {total}"
            list_campestre.append(lote)
            print('Registro exitoso\n')
            enter = input('Presione <Enter> para continuar...')
            fnt_limpiar()

    if op == '2':
        limpiar_pantalla()
        tipo_lote = input('---TIPO DE LOTE---\n1. Urbano\n2. Comercial\n3. Campestre\n->')

        if tipo_lote == '1':
            limpiar_pantalla()
            print('---LISTA DE LOTES URBANOS---\n' )
            if len(list_urbano) == 0:
                print('No hay lotes registrados\n')
                enter = input('Presione <Enter> para continuar...')
                fnt_limpiar()
            else:
                for lote in list_urbano:
                    print(lote)

        elif tipo_lote == '2':
            limpiar_pantalla()
            print('---LISTA DE LOTES COMERCIALES---\n' )
            if len(list_comercial) == 0:
                print('No hay lotes registrados\n')
                enter = input('Presione <Enter> para continuar...')
                fnt_limpiar()
            else:
                for lote in list_comercial:
                    print(lote)

        elif tipo_lote == '3':
            limpiar_pantalla()
            print('---LISTA DE LOTES CAMPESTRES---\n' )
            if len(list_campestre) == 0:
                print('No hay lotes registrados\n')
                enter = input('Presione <Enter> para continuar...')
                fnt_limpiar()
            else:
                for lote in list_campestre:
                    print(lote)

    if op == '3':
        sw = False

    if op == '4':
        limpiar_pantalla()
        print("---TOTALES ACUMULADOS---\n")
        print(f"Total Lotes Urbanos: {len(list_urbano)}")
        print(f"Total Lotes Comerciales: {len(list_comercial)}")
        print(f"Total Lotes Campestres: {len(list_campestre)}")
        enter = input('\nPresione <Enter> para continuar...')
        fnt_limpiar()

while sw:
    opcion = input('---MENÚ---\n1. Agregar\n2. Mostrar\n3. Salir\n4. Mostrar Totales\n->')
    fnt_selector(opcion)
