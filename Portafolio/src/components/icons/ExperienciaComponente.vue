<!--
-->>



<template>
    <div id="wadu-wadu"> 
        <section id="experiencia">
        <div class="card">
            <h3 class="titulo">{{ titulo }}</h3>
            <p class="fecha">{{ fecha }}</p>
            <ul class="listado">
            <li class="item">
                <p>{{ experiencia.parrafo }}</p>
                <div class="icon-container">
              
                </div>
              <p>
                Comence la tecnicatura superior en desarollo de software
              </p>
            </li>
            <li class="item">
              
              <p>
                Estudie y me capacite en c++
            </p>
            </li>
            <li class="item">
             
              <p>
                Comence la tecnicatura universitaria en programacion  en la UTN San Rafael
            </p>
            </li>
            <li class="item">
             
              <p>
                Realice el periodo de selecion de alura latam para una beca
            </p>
            </li>
            <li class="item">
           
              <p>
                Complete el periodo de seleccion y continuo como becado en el periodo de especializacion en BackEnd
            </p>
            </li>
          </ul>
        </div>
        
      </section>
      </div>
    </template>
    
    <style scoped>
    
    
    
    
    .card {
      height: 100%;
      border-radius: 30px;
      background: linear-gradient(135deg, rgb(141, 137, 137) 0%, rgb(0, 0, 0) 100%);
      transition: all 0.5s ease-in-out;
      transform-style: preserve-3d;
      box-shadow: rgba(7, 161, 35, 0) 40px 50px 25px -40px, rgba(246, 246, 246, 0.2) 0px 25px 25px -5px;
      
    }
    .titulo{
        color: rgb(31, 22, 41);
        font-size: 2rem;
        font-weight: bold;
        margin-left: 2rem;
    }
    
    .fecha{
        color: rgb(209, 73, 27);
        font-size: 1.2rem;
        margin-left: 2rem;
        font-weight: bold;
    }
    
    
    .listado{
        color: rgb(245, 244, 247);
        font-size: 1.2rem;
        margin-left: 2rem;
        font-weight: bold;
    }
    
    .item{
    margin-bottom: 2rem;
    margin-top: 2rem;
    
    }
    .wadu-wadu{
    height: 40rem;
    
    }
    
    </style>
