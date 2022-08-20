class Hex {
    constructor(value){
        this.value = Number(value);
    }
    
    toString(){
        return `0x${this.value.toString(16).toUpperCase()}`;
    }
    
    valueOf(){
        return this.value;
    }
    
    plus(number){
        let result = (this.value + Number(number.valueOf()));
        return new Hex(result);
    }
    
    minus(number){
        let result = (this.value - Number(number.valueOf()));
        return new Hex(result);
    }
    
    parse(string){
        return parseInt(string, 16);
        
    } 
    
    
}