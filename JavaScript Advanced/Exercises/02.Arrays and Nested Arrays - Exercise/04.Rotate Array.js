function rotate(arr, n){
    for (let i = 0; i < n; i++){
        arr.unshift(arr.pop())
    }
    console.log(arr.join(" "))
}