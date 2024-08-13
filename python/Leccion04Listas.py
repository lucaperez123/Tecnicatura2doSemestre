#Lista = Ariel , Liliana, Luca,Osvaldo

nombres = ['Luca' , 'Fiorella','Mariano', 'Bianca']
print(nombres)
#print(nombres[0]) #Mostrando Elemento que queramos
#print(nombres[1])
#print(nombres[3]) 
#print(nombres[-1]) # mostramos el ultimo numero
#print(nombres[-2]) # Mostramos el penultimo

#Recuperar un rango de la lista

print(nombres[0:2]) # Solo muestra el indice 0, 1 pero no el indice 2
# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) #Indices a mostrar 0, 1, 2

#desde el indice indicado hasta el final
print(nombres[1: ])

#Modificamos un valor 
nombres[3] = 'Gustavo'
nombres[0] = 'Lucas'
print(nombres)

#Iterar una lista

for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

