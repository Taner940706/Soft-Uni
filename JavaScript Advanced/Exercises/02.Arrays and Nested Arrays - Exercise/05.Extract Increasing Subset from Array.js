function extract(arr){
    let max = arr[0];
    let new_arr = [];
    new_arr.push(max)
    for(let i=1;i<=arr.length;i++){
        if(arr[i]>max){
            new_arr.push(arr[i]);
            max = arr[i];
        }
    }
    return new_arr;
}