function addItem() {

    var txt = document.getElementById("newItemText").value;
    var vlu = document.getElementById("newItemValue").value;
    var x = document.getElementById("menu");
	var option1 = document.createElement("option");
	option1.text = txt;
	option1.value = vlu;
	x.add(option1);
    document.getElementById("newItemText").value = '';
    document.getElementById("newItemValue").value = '';


    
}