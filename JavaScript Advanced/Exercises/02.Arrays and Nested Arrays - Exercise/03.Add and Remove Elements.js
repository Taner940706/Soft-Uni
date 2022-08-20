function add_remove(arr){
    res = []
    for (let i = 0; i < arr.length; i++){
        if (arr[i] == "add"){
            res.push(i+1)
        }
        else{
            res.pop()
        }
    }
    if (res.length != 0){
        for (let i = 0; i < res.length; i++){
            console.log(res[i])
        }
    }
    else{
        console.log("Empty")
    }
    
}