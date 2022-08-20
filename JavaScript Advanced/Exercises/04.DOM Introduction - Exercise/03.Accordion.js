function toggle() {

    var x = document.getElementById("extra");
    if (x.style.display === "none") {
    	x.style.display = "block";

        y=document.getElementsByClassName("button");  // Find the elements
        for(var i = 0; i < y.length; i++){
        	y[i].innerText="Less";
    }
    }
    else {
    	x.style.display = "none";
    	y=document.getElementsByClassName("button");  // Find the elements
        for(var i = 0; i < y.length; i++){
        	y[i].innerText="More";

}

}
}