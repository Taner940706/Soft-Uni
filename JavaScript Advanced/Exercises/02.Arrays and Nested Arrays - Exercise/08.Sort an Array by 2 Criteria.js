function multiple_criteria(arr){
    arr.sort(function(a, b) {
        return a.length - b.length || a.localeCompare(b)
        })
    for (let i=0;i<arr.length;i++){
        console.log(arr[i])
    }
}