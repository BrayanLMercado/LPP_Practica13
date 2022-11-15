'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 13: Diccionarios Anidados
Archivo De Funciones
Fecha: 17 De Noviembre De 2022
'''

def main():
    Alum={
        'E1':{'Nombre':'Brayan','Edad':20,'Apellido':'Mercado','Telefono':'6651201847','Promedio':87,'Matrícula':'1280838'},
        'E2':{'Nombre':'Joseph','Edad':23,'Apellido':'Loya','Telefono':'6641201949','Promedio':89,'Matrícula':'1270838'},
        'E3':{'Nombre':'Ramón','Edad':23,'Apellido':'López','Telefono':'6461201949','Promedio':81,'Matrícula':'1279848'},
        'E4':{'Nombre':'Dayana','Edad':19,'Apellido':'Vargas','Telefono':'6861201744','Promedio':93,'Matrícula':'1270899'},
        'E5':{'Nombre':'Brian','Edad':21,'Apellido':'Valle','Telefono':'6641231849','Promedio':80,'Matrícula':'1290738'},
        'E6':{'Nombre':'Andrés','Edad':23,'Apellido':'Toledo','Telefono':'6861601749','Promedio':99,'Matrícula':'1260438'},
        'E7':{'Nombre':'Christian','Edad':25,'Apellido':'Carmona','Telefono':'6651201949','Promedio':78,'Matrícula':'1299938'},
        'E8':{'Nombre':'Diego','Edad':25,'Apellido':'Carmona','Telefono':'6641201949','Promedio':100,'Matrícula':'1299937'},
        'E9':{'Nombre':'Christian','Edad':29,'Apellido':'Vargas','Telefono':'6661221249','Promedio':68,'Matrícula':'1290938'},
        'E10':{'Nombre':'Arturo','Edad':23,'Apellido':'Pineda','Telefono':'6631281949','Promedio':77,'Matrícula':'1240632'}
    }
    try:
        Nombre=str(input("Nombre Del Alumno A Buscar: "))
        Clave=str(input("Clave A Utilizar (Nombre,Edad,Apellido,Telefono,Promedio,Matrícula): "))
        Clave=Clave.title()
        generarInfo(Nombre,Clave,**Alum)
    except Exception as E:
        print(E)

def buscarFlag(nombre,clave,**Alum):
    for dic1, Estudiante, in Alum.items():
        if nombre in Estudiante['Nombre']:
            flag=True
            break
        else:
            flag=False
    return flag

def buscar(nombre,**Alum):
    for dic1, Estudiante, in Alum.items():
        if nombre in Estudiante['Nombre']:
            print('Datos Del Alumno Buscado')
            print("Nombre:",Estudiante["Nombre"],"\nApellido:", Estudiante["Apellido"],"\nMatrícula",Estudiante['Matrícula'])
            print("Edad",Estudiante['Edad'],"\nTelefono:",Estudiante["Telefono"],"\nPromedio:", Estudiante["Promedio"],'\n')

def caliMin(**Alum):
    try:
        prom=[]
        for dic1, Estudiante, in Alum.items():
            prom.append(Estudiante['Promedio'])
        print('El Promedio Más Bajo Es:',min(prom))
    except Exception:
        print("La Clave No Es Válida")

def edadMayor(**Alum):
    try:
        age=[]
        for dic1, Estudiante, in Alum.items():
            age.append(Estudiante['Edad'])
        print('La Edad Mayor Es:',max(age),'Años')
    except Exception:
        print("La Clave No Es Válida")

def edadProm(**Alum):
    try:
        age=[]
        for dic1, Estudiante, in Alum.items():
            age.append(Estudiante['Edad'])
        prom=sum(age)/len(age)
        print('El Promedio De Las Edades Es:',round(prom,2),'Años')
    except Exception:
        print("La Clave No Es Válida")

def printClaveGeneral(clave,**Alum):
    try:
        i=1
        print('\nClave Solicitada:',clave)
        for dic1, Estudiante, in Alum.items():
            print('Alumno',i,':',Estudiante[clave])
            i+=1
    except Exception:
        print("\nLa Clave No Existe")


def generarInfo(nombre,clave,**Alum):
    flag=buscarFlag(nombre,clave,**Alum)
    if flag!=False:
        buscar(nombre,**Alum)
    else:
        print("El Alumno No Se Encuentra Registrado")
    caliMin(**Alum)
    edadMayor(**Alum)
    edadProm(**Alum)
    printClaveGeneral(clave,**Alum)