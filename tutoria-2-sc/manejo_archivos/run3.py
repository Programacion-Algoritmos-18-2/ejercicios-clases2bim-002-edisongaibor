from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona,OperacionesPersona


m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

# print(lista)

lista = lista[1:]
lista_personas = []
# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])



for d in lista: 
    # print(d)
    p = Persona(d[1], d[2], d[3], d[0], d[4], d[5]) 
    lista_personas.append(p)

operaciones = OperacionesPersona(lista_personas) # Creo el objeto operaciones que recibe lo que tiene OperacionesPersona(lista_personas)
print(operaciones.obtener_promedio_n1()) #Imprime promedio de n1
print(operaciones.obtener_promedio_n2()) #Imprime promedio de n2
print(operaciones.obtener_listado_n1()) #Imprime valores menores a 15 de n1
print(operaciones.obtener_listado_n2())	#Imprime valores menores a 15 de n2
print(operaciones.obtener_listado_personas("R", "J")) #Imprime los nombres y apellidos que tienen las letras en la posicion 0 de R y J





