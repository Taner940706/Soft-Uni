function solve() {
    document.getElementsByTagName("button")[0].addEventListener("click", AddToReceiveForm);
    let description = document.getElementById("description");
    let name = document.getElementById("client-name");
    let phone = document.getElementById("client-phone");
    let prod_type = document.getElementById("type-product")


    function AddToReceiveForm(){
    	if (description.value != "" || name.value != "" || phone.value != ""){

    		let section = document.getElementById("received-orders")

    		let div = document.createElement("div");
    		let h2 = document.createElement("h2");
    		let h3 = document.createElement("h3");
    		let h4 = document.createElement("h4");
    		let btn_1 = document.createElement("button");
    		let btn_2 = document.createElement("button");

    		div.classList.add("container");
    		h2.textContent = "Product type for repair: "+ prod_type.value;
    		h3.textContent = "Client information: "+name.value+", "+phone.value;
    		h4.textContent = "Description of the problem: "+description.value;
    		btn_1.classList.add("start-btn");
    		btn_1.textContent = "Start repair";
    		btn_2.textContent = "Finish repair";
    		btn_2.disabled = true;
    		btn_2.classList.add("finish-btn");

    		div.appendChild(h2);
    		div.appendChild(h3);
    		div.appendChild(h4);
    		div.appendChild(btn_1);
    		div.appendChild(btn_2);

    		section.appendChild(div)

    		description.value = "";
    		name.value = "";
    		phone.value = "";

    		let temp = document.getElementsByClassName("start-btn");
    		let temp_1 = document.getElementsByClassName("finish-btn");
    		for (let i=0;i<temp.length;i++){
    			temp[i].addEventListener("click", startRepair);
    			function startRepair(){
    					document.getElementsByClassName("start-btn")[i].disabled = true;
    			        document.getElementsByClassName("finish-btn")[i].disabled = false;
    				}

    		}

    		for (let j=0;j<temp_1.length;j++){
    			temp_1[j].addEventListener("click", finishRepair);
    			let section_complete = document.getElementById("completed-orders");
    			function finishRepair(){
    					
    					let divs = document.getElementsByClassName("container")[j];
    					let clone = divs.cloneNode(true)
    					section_complete.appendChild(clone);
    					document.querySelectorAll("#completed-orders .start-btn")[0].remove();
    					document.querySelectorAll("#completed-orders .finish-btn")[0].remove();
    					divs.remove();


    				}

    		}
    		document.getElementsByClassName("clear-btn")[0].addEventListener("click", clearAll)

    		


    		function finishRepair(){
    			let section_complete = document.getElementById("completed-orders");
    			let clone = div.cloneNode(true)
    			section_complete.appendChild(clone);
    			div.remove();

    		}

    		function clearAll(){
    			let div_1 = document.getElementsByClassName("container");
    			for (let i=0;i<div_1.length;i++){
    				div_1[i].remove();
    			}
    			
    		}


    	}
    }
}