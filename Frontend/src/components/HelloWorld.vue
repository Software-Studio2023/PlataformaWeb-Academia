<script setup>
import NavigationPrincipal from './NavigationPrincipal.vue'
import 'bootstrap/dist/css/bootstrap.min.css'

</script>
<template>
  <header>
    <NavigationPrincipal />
  </header>
   <body>
    <h1>Software Studio</h1>
      <section class="inicio">
          <h2 class="title1">¿Quienes somos?</h2>
          <p class="contexto">Somos una empresa orientada al aprendizaje en el mundo de la programacion y bases de datos
            , a traves de cursos que se relizan de forma presenciañ con el objetivo de dar las herramientas
            necesarias a las personas, para impulsar el avance tecnologico.
          </p>
          <img class="logomarca" src="../assets/logomarca.png">
      </section>

      <section class="cursos">
        <h2 class="title2">Cursos</h2>
        <p>Somos una empresa orientada al aprendizaje en el mundo de la programacion y bases de datos
            , a traves de cursos que se relizan de forma presenciañ con el objetivo de dar las herramientas
            necesarias a las personas, para impulsar el avance tecnologico.</p>
      </section>

      <section class="container">
        <h2>Aprende IA con nosotros</h2>
        <p>Somos una empresa orientada al aprendizaje en el mundo de la programacion, puedes aprender con nosotros
          como crear una inteligencia artificial. Puede interactuar con nuestra IA de reconocimiento Facial.
        </p>
            <a class="btn btn-outline-primary" href="http://localhost:3000/video/">Probar IA</a>
      </section>

      <section> 
        <h2>Trabajos realizados</h2>
        <img src="../assets/cursos.jpeg" alt="">
        <img src="../assets/Exp.jpeg" alt="">
        <img src="../assets/fundadora.jpeg" alt="">
      </section>
      
      <footer class="text-center">
        <h4>Derechos autor Software Studio 2023</h4>
      </footer>
   </body>
</template>

<style scoped>
*{
  margin: 1%;
}


header{
  align-items: center;
  justify-content: center;
  display: flex;
}

h1{
  font-weight: 500;
  font-size: 75px;
  color: blue;
  text-align: center;
}

.inicio{
  padding:0px;
  margin: 0px;
  text-align: justify;
  margin-right: 300px;
  margin-left: 20px;
  background-color: cyan;
  border-style: solid;
  border-radius: 20px;
  border-color: blue;
  display: flex;
}
.contexto{
  margin-right: 20px;
  font-size: 20px;
  align-items: center;
  justify-content: center;
}
.logomarca{
  width: 100px;
  height: 100px;
}

img{
  width: 200px;
  height: 200px;
  align-items: center;
  
}

.cursos{
  background-color: blue;
  color: white;
  border-style: solid;
  border-color: black;
  margin-left: 300px;
  margin-right: 20px;
  border-radius: 20px;
}

.container{
  background-color: lightgray;
  border: 4px;
  border-radius: 20px;
  border-style: solid;
}
</style>
