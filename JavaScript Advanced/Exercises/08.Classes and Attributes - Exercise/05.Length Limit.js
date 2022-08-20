class Stringer{
    
    constructor(innerString , innerLength){
        this.innerString = String(innerString);
        this.innerLength = Number(innerLength);
    }
    
    increase(length){
        this.innerLength += length;
    }
    decrease(length){
        this.innerLength -= length;
        if (this.innerLength<0){
            this.innerLength = 0;
        }
        
        
    }
    
    toString(){
        if (this.innerLength == 0){
            return "..."
        }
        if (this.innerLength<this.innerString.length){
            return `${this.innerString.slice(0,(this.innerString.length-this.innerLength))}...`
        }
        return `${this.innerString}`;
    }
    
}