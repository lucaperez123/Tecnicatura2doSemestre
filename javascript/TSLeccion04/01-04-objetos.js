let x =10 // variables de tipo prmitiva
console.log(x.leght); 

//objeto
let persona = {
    nombre: 'Juan',
    apellido: 'Perez',
    email: 'juanperezgmal.com',
    edad: 28,
    nombreCompleto: function(){ // metodo o funcion en javascript
        return this.nombre + ' ' + this.apellido;
    }
}

console.log(persona.nombre);
console.log(persona.edad);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.nombreCompleto());



