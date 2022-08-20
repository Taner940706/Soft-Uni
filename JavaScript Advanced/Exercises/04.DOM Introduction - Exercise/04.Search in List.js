function search() {
    var a = document.getElementsByTagName("li");
    var b = document.getElementById("searchText").value;
    var c = document.getElementById('result');
    let lst = [];
    for (let i=0;i<a.length;i++){
        t = a[i].innerHTML;
        if (t.includes(b)){
            lst.push(t);
            a[i].style.fontWeight = "bold";
            a[i].style.textDecoration = "underline"
 
        }
 
    }
 
    c.innerHTML += `${lst.length} matches found`
 
    
 }