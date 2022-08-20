function Argument_Info(...arr){
    let str = 0;
    let func = 0;
    let num = 0;
    let obj1 = 0;
    let obj = {};
 

    for (let i=0;i<arr.length;i++){

        if (typeof(arr[i])=="function"){
            func += 1;
        }
        else if (typeof(arr[i])=="number"){
            num += 1;
        }
        else if (typeof(arr[i])=="object"){
            obj1 += 1;
        }
        else if (typeof(arr[i])=="string"){
            str += 1;
        }
        

        console.log(`${typeof(arr[i])}: ${arr[i]}`)

    }


    obj.string = str;
    obj.number = num;
    obj.function = func;
    obj.object = obj1;

    let srt = Object.entries(obj).sort((a,b) => b[1]-a[1]);

    for (let i=0;i<srt.length;i++){
        if (srt[i][1]>0){
            console.log(`${srt[i][0]} = ${srt[i][1]}`)
        }
    }

}