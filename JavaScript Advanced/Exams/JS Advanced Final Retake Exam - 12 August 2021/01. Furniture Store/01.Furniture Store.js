function solve() {
    let model = document.getElementById("model");
    let year = document.getElementById("year");
    let description = document.getElementById("description");
    let price = document.getElementById("price");
    let add = document.getElementById("add");
    let res = document.getElementsByClassName("total-price")[0];

    add.addEventListener("click", addFurniture);

    function addFurniture(e){
        e.preventDefault();

        if (model.value != "" && year.value != "" && description.value != "" && price.value != "" && Number(price.value) >= 0 && Number(year.value)>=0){
         let tbl = document.getElementById("furniture-list");
         let tr_main = document.createElement("tr");
         let tr_hide = document.createElement("tr");
         let td_model = document.createElement("td");
         let td_price = document.createElement("td");
         let td_description = document.createElement("td");
         let td_year = document.createElement("td");
         let td_buttons = document.createElement("td");
         let btn_1 = document.createElement("button");
         let btn_2 = document.createElement("button");
         btn_1.classList.add("moreBtn");
         btn_2.classList.add("buyBtn");
         btn_1.textContent = "More Info";
         btn_2.textContent = "Buy it";
         tr_main.classList.add("info");
         tr_hide.classList.add("hide");
         td_description.colSpan = "3";


         
         td_model.textContent = model.value;
         td_price.textContent = Number(price.value).toFixed(2);
         td_description.textContent = "Description: "+description.value;
         td_year.textContent = "Year: "+ Number(year.value);

         td_buttons.appendChild(btn_1);
         td_buttons.appendChild(btn_2)
         tr_main.appendChild(td_model);
         tr_main.appendChild(td_price);
         tr_main.appendChild(td_buttons);
         tr_hide.appendChild(td_year);
         tr_hide.appendChild(td_description);
         tbl.appendChild(tr_main);
         tbl.appendChild(tr_hide);

         model.value = "";
         year.value = "";
         description.value = "";
         price.value = "";


         btn_1.addEventListener("click",function likeSong(e) {
            if (btn_1.textContent == "More Info"){
                btn_1.textContent = "Less Info";
                tr_hide.style.display = "contents";
            }
            else{
                btn_1.textContent = "More Info";
                tr_hide.style.display = "none";

            }
            
        });

        btn_2.addEventListener("click",function LimeMike(e) {

            e.target.parentNode.parentNode.remove();
            tr_hide.remove();

            res.textContent.replace("0.00","");
            
            res.innerHTML += Number(td_price.textContent);
            
            
            
        });


        }
    }

    
}