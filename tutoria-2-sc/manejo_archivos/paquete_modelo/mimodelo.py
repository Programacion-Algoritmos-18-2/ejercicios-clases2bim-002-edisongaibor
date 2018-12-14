"""
    creación de clases
"""
class Persona(object): #Creo Clase Persona
    """
    """
    
    def __init__(self, n, ape, ed, cod,n1,n2): #Constructor (recibo distintos parametros)
        """
        """
        self.nombre = n
        self.edad = int(ed)  #pongo int porque python me recibe por defecto cadenas y debo convertir a entero.
        self.codigo = int(cod)
        self.apellido = ape
        self.nota1 = int(n1)
        self.nota2 = int(n2)

    #Creacion de metodos set y get (agregar y obtener)
    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_edad(self, n):
        """
        """
        self.edad = int(n)

    def obtener_edad(self):
        """
        """
        return self.edad
    
    def agregar_codigo(self, n):
        """
        """
        self.codigo = int(n)

    def obtener_codigo(self):
        """
        """
        return self.codigo
    
    def obtener_apellido(self):
        """
        """
        return self.apellido

    def agregar_nota1(self):
        """
        """
        self.nota1 = int(n1)

    def obtener_nota1(self):
        """
        """
        return self.nota1

    def agregar_nota2(self):
        """
        """
        self.nota2 = int(n2)

    def obtener_nota2(self):
        """
        """
        return self.nota2



#Metodo toString de Python  
    def __str__(self):
        """
        """
        return "%s - %s - %d - %d -%d -%d" % (self.nombre, self.apellido,\
                self.edad, self.codigo, self.nota1, self.nota2 )

#Clase Operaciones Persona
class OperacionesPersona(object):
    """
    """
    
    def __init__(self, listado):
        """
        """
        self.listado_personas = listado
    
    def obtener_promedio_n1(self):
        """
        """
        suma = 0 #Inicializa suma en 0 

        for n in self.listado_personas: 
            suma = suma + n.obtener_nota1() #Crea un acumulador (suma) que permite almacenar nota1
        promedio = suma / len(self.listado_personas) #saca promedio de nota1 , por medio de suma dividido para el tamanio de la lista listado personas

        return promedio # Retorna el resultado de promedio de nota1

    def obtener_promedio_n2(self): 
        """
        """
        suma = 0 #Inicializa suma en 0

        for n in self.listado_personas:
            suma = suma + n.obtener_nota2() #Crea un acumulador -suma- que permite almacenar nota2
        promedio = suma / len(self.listado_personas) #saca promedio de nota2 , por medio de suma dividido para el tamanio de la lista listado personas

        return promedio # Retorna el resultado de promedio de nota2

    def obtener_listado_n1(self):
        """
        """
        print("Notas n1 menores a quince:\n") 
        cadena = "" # Se inicializa cadena en vacia (Formateo)
        for n in self.listado_personas:
            if(n.obtener_nota1() < 15): #Restringe mediante un if si la nota (nota1) es menor a 15
                cadena = "%s-%d-%s\n" % (cadena, n.obtener_nota1(), n.obtener_nombre()) # Imprime la cadena (vacia), la nota 1 que es menor a 15 y el nombre de la persona que tiene esa nota
        return cadena   #Retorna la cadena con nota menor a 15 y el nombre
    
    def obtener_listado_n2(self):
        """
        """
        print("Notas n2 menores a quince:\n")
        cadena = "" # Se inicializa cadena en vacia (Formateo)
        for n in self.listado_personas:
            if(n.obtener_nota2() < 15): #Restringe mediante un if si la nota (nota1) es menor a 15
                cadena = "%s-%d-%s\n" % (cadena, n.obtener_nota2(), n.obtener_nombre()) # Imprime la cadena (vacia), la nota 1 que es menor a 15 y el nombre de la persona que tiene esa nota
        return cadena #Retorna la cadena con nota menor a 15 y el nombre
    
   
    def obtener_listado_personas(self, l1, l2): # Creo metodo que recibe 2 parametros l1 y l2
        """
        """
        print("Nombres de personas que comienzan con la letra R y J:\n")
        cadena = "" # Se inicializa cadena en vacia (Formateo)

        for n in self.listado_personas:
            if( l1 == n.obtener_nombre()[0] or l2 == n.obtener_nombre()[0]): #Restingo mediante un if si la letra 1 (R) es igual a la letra de los nombres en la posicion 0, de la misma manera con la letra 2 (J)
                cadena = "%s-%s-%s\n" % (cadena, n.obtener_nombre(), n.obtener_apellido()) # Llena la cadena con los nombres que tienen las letras que envia desde el run
        return cadena #Retorna la cadena con los nombres y apellidos 


    def __str__(self): #Metodo toString
        """
        """
        cadena = "" #Inicializo cadena en vacio
        for n in self.listado_personas:
            cadena = "%s-%s-%s \n" % (cadena, n.obtener_nombre(), n.obtener_apellido())   
        return cadena #Retorna la cadena con nombres y apellidos
