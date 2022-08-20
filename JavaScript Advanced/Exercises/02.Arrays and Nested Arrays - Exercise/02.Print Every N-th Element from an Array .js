function n_steps(arr, n){
    test_arr = []
    for (let i = 0; i < arr.length; i += n){
        test_arr.push(arr[i])
    }
    return test_arr
}