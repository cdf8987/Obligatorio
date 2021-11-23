import pickle
from os.path import exists
from os import system
from datetime import date

#creo estructura de datos.
banco = {"alumnos":[],"carrera":[]}

una_carrera1 = {"codigo":123,"nombre":"carrera 1","materias":[]}
una_carrera2 = {"codigo":456,"nombre":"carrera 2","materias":[]}
una_carrera3 = {"codigo":789,"nombre":"carrera 3","materias":[]}

una_materia1 = {"codigo":123,"nombre":"materia 1 de carrera 1","carrera":una_carrera1,"estanterias":[]}
una_materia2 = {"codigo":456,"nombre":"materia 2 de carrera 1","carrera":una_carrera2,"estanterias":[]}
una_materia3 = {"codigo":789,"nombre":"materia 1 de carrera 2","carrera":una_carrera3,"estanterias":[]}

una_estanteria1 = {"codigo":123,"nombre":"Estantería 1 de materia 1 de carrera 1","materia":una_materia1,"material":[]}
una_estanteria2 = {"codigo":456,"nombre":"Estantería 2 de materia 2 de carrera 2","materia":una_materia2,"material":[]}
una_estanteria3 = {"codigo":789,"nombre":"Estantería 1 de materia 3 de carrera 3","materia":una_materia3,"material":[]}

una_materia1.get("estanterias").append(una_estanteria1)
una_materia2.get("estanterias").append(una_estanteria2)
una_materia3.get("estanterias").append(una_estanteria3)

una_carrera1.get("materias").append(una_materia1)
una_carrera2.get("materias").append(una_materia2)
una_carrera3.get("materias").append(una_materia3)

banco.get("carrera").append(una_carrera1)
banco.get("carrera").append(una_carrera2)
banco.get("carrera").append(una_carrera3)


#definicion de funciones.
def menu():
    print("1-Registrar alumno")
    print("2-Registrar material")
    print("3-Material por materia")
    print("4-Ver material")
    print("5-Cantidad de material por carrera")
    print("6-Calificación del material")
    print("7-Material por alumno")
    print("8-Alumnos con más materiales")
    print("9-Salir")

def abrir_archivo():
    
    global banco
    if exists("archivo_banco"):
        archivo = open("archivo_banco","rb")
        banco = pickle.load(archivo)
        archivo.close()

def grabar_archivo():
    archivo = open("archivo_banco","wb")
    pickle.dump(banco,archivo)
    archivo.close()

def convertir_fecha(la_fecha):
    lista_fecha = la_fecha.split("/")
    tipo_fecha = date(int(lista_fecha[2]),int(lista_fecha[1]),int(lista_fecha[0]))
    return tipo_fecha

def mostrar_carrera():
    for una_carrera in banco.get("carrera"):
        print("Código:",una_carrera.get("codigo"),"Nombre:",una_carrera.get("nombre"))

def mostrar_secciones(una_carrera):
    for una_materia in una_carrera.get("materias"):
        print("Código:",una_materia.get("codigo"),"Nombre:",una_materia.get("nombre"))

def mostrar_estanterias(una_materia):
    for una_estanteria in una_materia.get("estanterias"):
        print("Código:",una_estanteria.get("codigo"),"Nombre:",una_estanteria.get("nombre"))

def buscar_alumno(cedula):
    encontre_alumno = False
    pos              = 0
    lista_alumno   = banco.get("alumnos")
    while not encontre_alumno and pos < len(lista_alumno):
        alumno = lista_alumno[pos]
        pos = pos + 1
        if alumno.get("cedula") ==  cedula:
            encontre_alumno = True 
    if encontre_alumno:
        return alumno
    else:
        return None

#buscar el material en todo el banco de materiales.
def buscar_material_en_banco(codigo):
    encontre_material = False
    pos              = 0
    lista_carrera   = banco.get("salas")
    #buscar las carreras hasta encontrar el material.
    while not encontre_material and pos < len(lista_carrera):
        una_sala = lista_carrera[pos]
        pos = pos + 1
        pos2 = 0
        lista_materia = una_carrera1.get ("materias")
        #buscar las materias de la carrera hasta encontrar el material.
        while not encontre_material and pos2 < len(lista_materia):
            una_materia = lista_materia[pos2]
            pos2 = pos2 + 1
            pos3 = 0
            lista_estanterias = una_materia.get("estanterias")
            #buscar las estanterias de las materias hasta encontrar el material.
            while not encontre_material and pos3 < len(lista_estanterias):
                una_estanteria = lista_estanterias[pos3]
                pos3 = pos3 + 1
                pos4 = 0
                lista_material = una_estanteria.get("material")
                #buscar los materiales de la estanteria hasta encontrar material.
                while not encontre_material and pos4 < len(lista_material):
                    un_material = lista_material[pos4]
                    pos4 = pos4 + 1
                    if un_material.get("codigo") == codigo:
                        encontre_material = True
    if encontre_material:
        return un_material
    else:
        return None

#busco la materia en todo el banco de materiales.
def buscar_materia_en_banco(codigo):
    encontre_materia = False
    pos              = 0
    lista_carrera   = banco.get("carrera")
    #busco las carreras hasta encontrar la materia.
    while not encontre_materia and pos < len(lista_carrera):
        una_carrera = lista_carrera[pos]
        pos = pos + 1
        pos2 = 0
        lista_materia = una_carrera.get("materias")
        #busco las materias de la carrera hasta encontrar la materia.
        while not encontre_materia and pos2 < len(lista_materia):
            una_materia = lista_materia[pos2]
            pos2 = pos2 + 1
            if una_materia.get("codigo") == codigo:
                encontre_materia = True
    if encontre_materia:
        return una_materia
    else:
        return None

def buscar_carrera(codigo):
    encontre_carrera = False
    pos              = 0
    lista_carrera   = banco.get("salas")
    while not encontre_carrera and pos < len(lista_carrera):
        una_carrera = lista_carrera[pos]
        pos = pos + 1
        if una_carrera.get("codigo") == codigo:
            encontre_carrera = True
    if encontre_carrera:
        return una_carrera
    else:
        return None

def buscar_materia(una_carrera, codigo):
    encontre_materia = False
    pos              = 0
    lista_materia   = una_carrera.get("materia")
    while not encontre_materia and pos < len(lista_materia):
        una_materia = lista_materia[pos]
        pos = pos + 1
        if una_materia.get("codigo") == codigo:
            encontre_materia = True
    if encontre_materia:
        return una_materia
    else:
        return None

def buscar_estanteria(una_materia, codigo):
    encontre_estanteria = False
    pos              = 0
    lista_estanterias   = una_materia.get("estanterias")
    while not encontre_estanteria and pos < len(lista_estanterias):
        una_estanteria = lista_estanterias[pos]
        pos = pos + 1
        if una_estanteria.get("codigo") == codigo:
            encontre_estanteria = True
    if encontre_estanteria:
        return una_estanteria
    else:
        return None

def sumar_material_alumno(cedula):
    total = 0
    lista_carrera = banco.get("carrera")
    for una_carrera in lista_carrera:
        lista_materia = una_carrera.get("materia")
        for una_materia in lista_materia:
            lista_estanterias = una_materia.get("estanterias")
            for una_estanteria in lista_estanterias:
                lista_material = una_estanteria.get("material")
                for un_material in lista_material:
                    #ver estructura del material, cada material tiene un alumno asociado.
                    alumno = un_material.get("alumno")
                    if cedula == alumno.get("cedula"):
                        #aumento la cantidad de material del alumno.
                        total = total + 1
    return total


#REQUERIMIENTO 1
def registrar_alumno():
    documento = input("Ingresa cédula del alumno: ")
    alumno_buscado = buscar_alumno(documento)
    if alumno_buscado == None:
        numero = input("Ingresa número de alumno: ")
        nombre = input("Ingresa nombre de alumno: ")
        fecha   = input("Ingresa fecha de nacimiento de alumno (dd/mm/aaaa): ")
        fecha_nac = convertir_fecha(fecha)
        alumno = {"cedula":documento,"nombre":nombre,"numero":numero,"fecha_nacimiento":fecha_nac}
        banco.get("alumnos").append(alumno)
        print("El alumno se registro correctamente...")
    else:
        print("El documento ya se encuentra registrado es del alumno",alumno_buscado.get("nombre"))

#REQUERIMIENTO 2
def registrar_material():
    documento = input("Ingresa número de documento del alumno que publica el material: ")
    alumno_buscado = buscar_alumno(documento)
    if alumno_buscado != None:
        print("alumno",alumno_buscado.get("nombre"))
        codigo = input("Ingresa código alfanumérico (letras y números) del material: ")
        material_buscado = buscar_material_en_banco(codigo)
        if material_buscado == None:
             #mejoro experiencia de usuario mostrandole los codigos de sala del banco de materiales para que ingrese uno
            #y no tenga que adivinar o acordarse de todos los codigos.
            mostrar_carrera()
            codigo_carrera = int(input("Ingresa código de la carrera donde publicar el material: "))
            carrera_buscada = buscar_carrera(codigo_carrera)
            if carrera_buscada != None:
                print(">>>",carrera_buscada.get("nombre"))
                #mejoro experiencia de usuario mostrandole los codigos de secciones de la carrera para que ingrese uno
                #y no tenga que adivinar o acordarse de todos los codigos.
                mostrar_carrera(carrera_buscada)
                codigo_materia = int(input("Ingresa código de la materia donde publicar el material: "))
                materia_buscada = buscar_materia(carrera_buscada, codigo_materia)
                if materia_buscada != None:
                    print(">>>",materia_buscada.get("nombre"))
                    #mejoro experiencia de usuario mostrandole los codigos de estanterias de la materia para que ingrese uno
                    #y no tenga que adivinar o acordarse de todos los codigos.
                    mostrar_estanterias(materia_buscada)
                    codigo_estanteria = int(input("Ingresa código de estantería donde publicar el material: "))
                    estanteria_buscada = buscar_estanteria(materia_buscada, codigo_estanteria)
                    if estanteria_buscada != None:
                        print(">>>",estanteria_buscada.get("nombre"))
                        titulo = input("Ingresa título del material: ")
                        contenido = input("Ingresa contenido del material: ")
                        calificacion = int(input("Ingresa calificación del material (1-10): "))
                        un_material = {"codigo":codigo,"titulo":titulo,"contenido":contenido,"calificacion":calificacion,"alumno":alumno_buscado,"estanteria":estanteria_buscada}
                        estanteria_buscada.get("material").append(un_material)
                        print("El material se registró correctamente...")
                    else:
                        print("La estantería no existe en",materia_buscada.get("nombre"))
                else:
                    print("La materia no exixte en",carrera_buscada.get("nombre"))
            else:
                print("La carrera no existe en el banco de materiales")
        else:
            print("El material ya se encuentra en plataforma",material_buscado.get("titulo"))
    else:
        print("El alumno con documento",documento,"no se encuentra registrado")

#REQUERIMIENTO 3
def material_por_materia():
    codigo = int(input("Ingresa código de la materia: "))
    materia_buscada = buscar_materia_en_banco(codigo)
    if materia_buscada != None:
        print("Lista de materiales de",materia_buscada.get("nombre"))
        lista_estanterias = materia_buscada.get("estanterias")
        for una_estanteria in lista_estanterias:
            lista_material = una_estanteria.get("material")
            for un_material in lista_material:
                print(un_material.get("codigo"),un_material.get("titulo"))
    else:
        print("La materia con código",codigo,"no está en el banco de materiales")

#REQUERIMIENTO 4
def ver_material():
    codigo = input("Ingresa código del material: ")
    material_buscado = buscar_material_en_banco(codigo)
    if material_buscado != None:
        #accedo a la estanteria del material (ver estructura del material cuando se crea)
        una_estanteria  = material_buscado.get("estanteria")
        #accedo a la materia de la estanteria (ver estructura creada al inicio)
        una_materia     = una_estanteria.get("materia")
        #accedo a la sala de la materia (ver estructura creada al inicio)
        una_sala        = una_materia.get("carrera")
        print("CARRERA =>",una_carrera1.get("nombre"),"MATERIA =>",una_materia.get("nombre"),"ESTANTERÍA =>",una_estanteria.get("nombre"))
        print("CONTENIDO:",material_buscado.get("contenido"))
        print("CALIFICACIÓN:",material_buscado.get("calificacion"))
    else:
        print("El material de código",codigo,"no está en el banco de materiales")

#REQUERIMIENTO 5
def cantidad_material_por_carrera():
    lista_carrera = banco.get("carrera")
    for una_carrera in lista_carrera:
        #inicio total de materiales para cada carrera.
        total_material = 0
        print(una_carrera.get("nombre"))
        lista_materia = una_carrera.get("materia")
        for una_materia in lista_materia:
            lista_estanterias = una_materia.get("estanterias")
            for una_estanteria in lista_estanterias:
                lista_material = una_estanteria.get("material")
                total_material = total_material + len(lista_material)
        print("Total de materiales en la sala",total_material)
        print("--------------------------------------------")

#REQUERIMIENTO 6
def calificación_del_material(): 
    codigo = input("Ingresa codigo del material: ")
    lista_carrera = banco.get("carrera")
    for una_carrera in lista_carrera:
        lista_materia = una_carrera.get("materia")
        for una_materia in lista_materia:
            lista_estanterias = una_materia.get("estanterias")
            for una_estanteria in lista_estanterias:
                lista_material = una_estanteria.get("material")
                for un_material in lista_material:
                    if un_material.get("titulo") >= titulo:
                        #accedo a la estanteria del material (ver estructura del material cuando se crea)
                        una_estanteria  = un_material.get("estanteria")
                        #accedo a la materia de la estanteria (ver estructura creada al inicio)
                        una_materia     = una_estanteria.get("materia")
                        #accedo a la sala de la materia (ver estructura creada al inicio)
                        una_carrera        = una_materia.get("carrera")
                        print("CARRERA =>",una_carrera.get("nombre"),"MATERIA =>",una_materia.get("nombre"),"ESTANTERÍA =>",una_estanteria.get("nombre"))
                        print("CONTENIDO:",un_material.get("contenido"))
                        print("TITULO:",un_material.get("titulo"))
                        print("--------------------------------------------")

#REQUERIMIENTO 7
def material_alumnos():
    alumnos_no_repetidos = []
    lista_carrera = banco.get("carrera")
    for una_carrera in lista_carrera:
        lista_materia = una_carrera.get("material")
        for una_materia in lista_materia:
            lista_estanterias = una_materia.get("estanterias")
            for una_estanteria in lista_estanterias:
                lista_material = una_estanteria.get("materiales")
                for un_material in lista_material:
                    #ver estructura de material cuando se crea. Cada material es de un alumno asociado.
                    alumno = un_material.get("alumno")
                    cedula = alumno.get("cedula")
                    #si el alumno no esta en la lista de cedulas que ya mostre.
                    if cedula not in alumnos_no_repetidos:
                        #lo agrego para no mostrarlo de nuevo.
                        alumnos_no_repetidos.append(cedula)
                        print("El alumno",alumno.get("nombre"),alumno.get("numero"),"ha publicado material")

#REQUERIMIENTO 8
def alumnos_con_mas_materiales():
    lista_alumno = banco.get("alumnos")
    mayor_cantidad = 0
    for un_alumno in lista_alumno:
        total_del_alumno = sumar_material_alumno(un_alumno.get("cedula"))
        if total_del_alumno >= mayor_cantidad:
            #me  quedo con el valor mas grande.
            mayor_cantidad = total_del_alumno
    if mayor_cantidad != 0:
        print("Mayor cantidad de materiales publicados",mayor_cantidad)
        #si hay por lo menos 1 alumno que tiene mas de cero materiales publicado.
        for un_alumno in lista_alumno:
            total_del_alumno = sumar_material_alumno(un_alumno.get("cedula"))
            if total_del_alumno == mayor_cantidad:
                print(">>> El alumno",un_alumno.get("nombre"),un_alumno.get("numero"),"ha publicado esa cantidad")


#al inicio del programa cargo toda la info del banco desde un archivo.
abrir_archivo()
opcion_usuario = 0
while opcion_usuario != 9:
    menu()
    opcion_usuario = int(input("Ingresa numero de opcion: "))
    #segun la opcion ingresada, ejecutamos la funcion correspondiente
    if opcion_usuario < 9 :
        if opcion_usuario == 1 :
            registrar_alumno()
        elif  opcion_usuario == 2 :
            registrar_material()
        elif  opcion_usuario == 3 :
            material_por_materia()
        elif  opcion_usuario == 4 :
            ver_material()             
        elif  opcion_usuario == 5 :
            cantidad_material_por_carrera()
        elif  opcion_usuario == 6 :
            calificación_del_material()
        elif  opcion_usuario == 7 :
            material_alumnos()
        elif  opcion_usuario == 8 :
            alumnos_con_mas_materiales()
    
    else  :
        print("Ingrese una opcion valida")                

    
grabar_archivo()
print("Eso es todo amigos")