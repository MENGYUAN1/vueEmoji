<!DOCTYPE html>
<html>
  <head>
    <title>Learn Emojis </title>
    <h3>Deployed by MENG YUAN Team 1d4</h3>
  </head>
  <!-- Global site tag (gtag.js) - Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-147552064-1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'UA-147552064-1');
  </script>

  <body>
    <div id="app">
      <h3>Learn Emojis</h3>
      <span v-for="problem in problems">
        <span v-if="problem===currentProblem">
           <b> {{problem}} </b>
        </span>
        <span v-else-if="isComplete(problem)">
          <button @click="currentProblem=problem"
                  style="background-color:green">
            {{problem}}
          </button>
        </span>
       <span v-else>
          <button @click="currentProblem=problem">
            {{problem}}
          </button>
       </span>
      </span>
      <br />
      <h4>Directions:</h4>
        {{directions[currentProblem]}} 
      <br/>
      <input v-model="givens[currentProblem]"> <br/>
      <span v-if="isComplete(currentProblem)"
            style="color:green">
        Correct!
      </span>
    </div>
    <script src="https://unpkg.com/vue"></script>
    <script src="./main.js"></script>
  </body>
</html>
