function same_nums(num){
    k = 0
    suma = 0
    t = String(num)
    for (let i = 0; i < t.length; i++) {
        
        if (t[i] != t[i + 1]){
            k = k + 1
        }
        suma = suma + parseInt(t[i])

    }
    if (k > 1){
        console.log("false")
    }
    else{
        console.log("true")
    }
    console.log(suma)
    
}