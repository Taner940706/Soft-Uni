function Sort_Array(arr, order){
    if (order == "asc"){
        return(arr.sort(function(a, b){return a-b}));
    }
    else{
        return(arr.sort(function(a, b){return b - a}));
    }
}