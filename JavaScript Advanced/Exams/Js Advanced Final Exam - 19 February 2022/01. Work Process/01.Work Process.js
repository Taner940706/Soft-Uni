function solve() {
    document.getElementById('add-worker').addEventListener('click', hireSomeone);
    let fname = document.getElementById('fname');
    let lname = document.getElementById('lname');
    let email = document.getElementById('email');
    let birth = document.getElementById('birth');
    let position = document.getElementById('position');
    let salary = document.getElementById('salary');
    let suma = 0;
 
    function hireSomeone(){
        let tbl = document.getElementById("tbody");
        if (fname.value != "" && lname.value != "" && email.value != "" && birth.value != "" && position.value != "" && salary.value != ""){
            const tr = document.createElement("tr");
            const td_1 = document.createElement("td");
            const td_2 = document.createElement("td");
            const td_3 = document.createElement("td");
            const td_4 = document.createElement("td");
            const td_5 = document.createElement("td");
            const td_6 = document.createElement("td");
            const td_7 = document.createElement("td");
            const btn_1 = document.createElement("button");
            const btn_2 = document.createElement("button");
 
            btn_1.classList.add("fired");
            btn_2.classList.add("edit");
 
            btn_1.textContent = "Fired";
            btn_2.textContent = "Edit";
            td_1.textContent = fname.value;
            td_2.textContent = lname.value;
            td_3.textContent = email.value;
            td_4.textContent = birth.value;
            td_5.textContent = position.value;
            td_6.textContent = salary.value;
 
            td_7.appendChild(btn_1);
            td_7.appendChild(btn_2);
            tr.appendChild(td_1);
            tr.appendChild(td_2);
            tr.appendChild(td_3);
            tr.appendChild(td_4);
            tr.appendChild(td_5);
            tr.appendChild(td_6);
            tr.appendChild(td_7);
            tbl.appendChild(tr);
 
            fname.value = "";
            lname.value = "";
            email.value = "";
            birth.value = "";
            position.value = "";
            salary.value = "";
 
            suma += Number(td_6.textContent);
 
            document.getElementById('sum').textContent = suma.toFixed(2);
 
            btn_2.addEventListener('click', function editSomeone(){
 
             fname.value = td_1.textContent;
             lname.value = td_2.textContent;
             email.value = td_3.textContent;
             birth.value = td_4.textContent;
             position.value = td_5.textContent;
             salary.value = td_6.textContent;
 
             suma -= Number(td_6.textContent);
             document.getElementById('sum').textContent = suma.toFixed(2);
 
             tbl.removeChild(tr);
 
 
 
 
         });
            btn_1.addEventListener('click', function firedSomeone(){
             suma -= Number(td_6.textContent);
             document.getElementById('sum').textContent = suma.toFixed(2);
             tbl.removeChild(tr);
 
         });
 
        }
    }
 
 
 }