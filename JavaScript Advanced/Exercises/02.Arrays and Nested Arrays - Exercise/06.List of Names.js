function list_of_name(arr){
    res = arr.sort()
    test_res = []
    for (let i = 0; i < res.length; i++){
        if (!test_res.includes(arr[i])){
            test_res.push(res[i])
        }
    }
    for (let i=0;i<test_res.length;i++){
        console.log((i+1)+"."+test_res[i])
    }
}