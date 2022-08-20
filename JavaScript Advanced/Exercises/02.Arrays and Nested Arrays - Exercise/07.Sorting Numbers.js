function sort_nums(arr){
    temp = arr.sort(function(a, b){return a-b})
    res = []
    for (let i = 0; i < temp.length; i++){
        res.push(temp.shift())
        res.push(temp.pop())
    }
    x = res.concat(temp)
    return x
}