function validate() {
    document.addEventListener("change", validate_email);

    function validate_email(){
        let emailAdress = document.getElementById("email").value;

        let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        if (emailAdress.match(regexEmail)) {
            document.getElementById("email").classList.remove("error");
        } 
        else 
        {
            document.getElementById("email").classList.add("error"); 
}
    }
}
