function Juice_Flavors(arr){
    let res = new Map();
    let wow = new Map();
    

    for (x of arr){
        x=x.split(" => ");
        key = x[0];
        value = Number(x[1]);
        if (!res.has(key)){
            res.set(key,value);

        }
        else{
            temp = res.get(key) + value;
            res.set(key,temp)
        }

        if (res.get(key) >= 1000){
            r = parseInt(res.get(key) / 1000);
            if (!wow.has(key)){
                wow.set(key,r);
    
            }
            else{
                temp1 = wow.get(key) + r;
                wow.set(key,temp1)
            }
            m = res.get(key) % 1000;
            res.set(key, m);
            
        }
        
    }

    for(let [key, value] of wow) {
        console.log(`${key} => ${value}`);
      }

}