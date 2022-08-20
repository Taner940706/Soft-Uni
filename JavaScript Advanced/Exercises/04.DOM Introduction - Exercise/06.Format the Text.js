function solve() {
    let txt = document.getElementById("input").value;
    arr = txt.split(".");
    let counter = 0;
    let txt_1 = '';
    let txt_2 = '';
  
    for (let i=0;i<arr.length; i++){
  
      if (arr.length <= 3){
        let app3 = document.createElement("p");
        app3.innerHTML = document.getElementById("input").value;
        document.getElementById("output").appendChild(app3);
        return;
      }
  
      if (arr[i].length >= 1){
  
        if (counter <= 2){
          txt_1 += `${arr[i]}.`
        }
        else{
          let app = document.createElement("p");
          app.innerHTML = txt_1;
          document.getElementById("output").appendChild(app);
  
          counter = 0;
          txt_1 = "";
          txt_1 += `<p>${arr[i]}.</p>`
  
        }
  
      }
      counter += 1;
    }
  
    for (let j = counter + 1; j<arr.length; j++){
  
      if (arr[j].length >= 1){
        txt_2 += `${arr[j]}.`
  
      }
  
    }
  
    let app1 = document.createElement("p");
          app1.innerHTML = txt_2;
          document.getElementById("output").appendChild(app1);
  
  
  }