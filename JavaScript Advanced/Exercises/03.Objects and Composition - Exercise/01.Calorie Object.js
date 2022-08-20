function calorie_object(arr){
    res = {}
    for (let i = 0; i<arr.length;i += 2){
        res[arr[i]] = parseInt(arr[i+1])
        
    }
    
    console.log(res)
}