function encodeAndDecodeMessages() {
    
    let btn1 = document.getElementsByTagName("button")[0];
    let btn2 = document.getElementsByTagName("button")[1];
    btn1.addEventListener("click", encode_func);
    btn2.addEventListener("click", decode_func);

    function encode_func(){


        let txt_area = document.getElementsByTagName("textarea")[0].value;
        let txt_area_1 = document.getElementsByTagName("textarea")[1];
        let temp = "";

        if (document.getElementsByTagName("textarea")[0].value == ""){
            return;
        }

        for (let i=0;i<txt_area.length;i++){
            temp += String.fromCharCode(txt_area[i].charCodeAt(0)+1);
        }

        txt_area_1.value = temp;
        document.getElementsByTagName("textarea")[0].value = '';
        
    }

    function decode_func(){

        let txt_area00 = document.getElementsByTagName("textarea")[0];
        let txt_area_11 = document.getElementsByTagName("textarea")[1].value;
        let temp1 = "";

        if (document.getElementsByTagName("textarea")[1].value == ""){
            return;
        }

        for (let i=0;i<txt_area_11.length;i++){
            temp1 += String.fromCharCode(txt_area_11[i].charCodeAt(0)-1)
        }

        txt_area00.value = temp1;



    }

}