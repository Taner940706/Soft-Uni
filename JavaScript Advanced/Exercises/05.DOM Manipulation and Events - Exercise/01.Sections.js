function create(words) {

	let content = document.getElementById("content");

	for (let i=0;i<words.length;i++){
		let divs = document.createElement("div");
		let p = document.createElement("p");
		let txt = document.createTextNode(words[i]);
		content.appendChild(divs);
		p.appendChild(txt);
		divs.appendChild(p)
		p.style.display = "none";
		divs.addEventListener("click", visible);

		function visible() {
			p.style.display = "block";
  }


	}



}