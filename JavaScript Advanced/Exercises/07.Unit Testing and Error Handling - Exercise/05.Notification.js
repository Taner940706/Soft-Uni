function notify(message) {

    document.getElementById("notification").addEventListener("click", hidediv);
    document.getElementById("notification").style.display = "block"
    document.getElementById("notification").textContent = message;
  
  
    function hidediv(){
      document.getElementById("notification").style.display = "none"
  
    }
  }