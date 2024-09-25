class Persona #Creamos una clase


    def__init__(self,nombre,apellido,edad): #se lo llama metodo init dunder
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido

persona1 = Persona("Luca", "Perez", 21) #Constructor
print(persona1.nombre)) #<class 'type'>
print(persona1.apellido) #<class 'type'>
print(persona1.edad) #<class 'type'>

persona2 = Persona("Fiorella", "Gonzalez", 22)
print(f"el objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} {persona2.edad}")

persona1.nombre = "Juan" #Modificamos el atributo nombre
persona1.apellido = "Gomez" #Modificamos el atributo apellido
persona1.edad = 30 #Modificamos el atributo edad
print(f"el objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} {persona1.edad}")