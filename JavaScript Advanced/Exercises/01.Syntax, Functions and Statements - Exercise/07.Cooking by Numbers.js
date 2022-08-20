function cooking_by_number(num, args1, args2, args3, args4, args5){
    args = [args1, args2, args3, args4, args5]
    num = parseInt(num)
    for (let i = 0; i < args.length; i++){
        if (args[i] == "chop"){
            num = num / 2
        }
        else if (args[i] == "dice"){
            num = Math.sqrt(num)
        }
        else if(args[i] == "spice"){
            num = num + 1
        }
        else if(args[i] == "bake"){
            num = num * 3
        }
        else{
            num = num*0.8
        }
        
        console.log(num)
    }
    
}