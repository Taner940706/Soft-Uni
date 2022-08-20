function subtract() {
	let a = document.getElementById('firstNumber').value;
    let b = document.getElementById('secondNumber').value;
    let theDiv = document.getElementById("result");
    let res = Number(a) - Number(b);
    
    theDiv.innerHTML += res; 

}