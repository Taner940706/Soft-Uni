function solve() {
    let txt = document.getElementById('text').value;
    let command = document.getElementById('naming-convention').value;
    let result = document.getElementById('result');
    let res = ''
  
    let a = txt.split(" ");
    if (command == "Camel Case"){
        res = a[0].toLowerCase();
        for (let i=1;i<a.length;i++){
            res += a[i].charAt(0).toUpperCase() + a[i].slice(1).toLowerCase();
        }
    }
    else if (command == "Pascal Case"){
  
        for (let i=0;i<a.length;i++){
            res += a[i].charAt(0).toUpperCase() + a[i].slice(1).toLowerCase();
        }
  
    }
    else{
        res = "Error!"
    }
  
    result.innerHTML += res; 
  
  }