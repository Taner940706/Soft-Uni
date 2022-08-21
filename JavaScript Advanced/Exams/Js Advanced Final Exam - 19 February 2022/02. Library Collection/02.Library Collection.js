class LibraryCollection{
    constructor(capacity){
        this.capacity = capacity;
        this.books = [];
    }
    
    addBook (bookName, bookAuthor){
        let obj = {};
        if (this.capacity<=0){
            throw "Not enough space in the collection."
        }
        else{
            obj.name = bookName;
            obj.author = bookAuthor;
            obj.payed = false;
            this.books.push(obj);
            this.capacity -= 1;
            return `The ${bookName}, with an author ${bookAuthor}, collect.`
            
        }
    }
    
    payBook(bookName){
        if (!this.books.find(e => e.name === bookName)){
            throw `${bookName} is not in the collection.`;
        }
        else{
            let x = this.books.find(e => e.name === bookName);
            if (x.payed == true){
                throw `${bookName} has already been paid.`;
            }
            else{
                x.payed = true;
                return `${bookName} has been successfully paid.`
                
            }
           
            
        }
         
        
    }
    
    removeBook(bookName) {
        if (!this.books.find(e => e.name === bookName)){
            throw `The book, you're looking for, is not found.`;
        }
        else{
            let x = this.books.find(e => e.name === bookName);
            if (x.payed == false){
                throw `${bookName} need to be paid before removing from the collection.`;
            }
            else{
                this.books = this.books.filter(data => data.name != bookName);
                this.capacity += 1;
                return `${bookName} remove from the collection.`
            }
            
            
        }
        
    }
    
    
getStatistics(bookAuthor){
    let res = "";
    let is_payed_1 = "";
    let is_payed_2 = "";
    if (!bookAuthor){
        let y = this.books.sort((a,b) => (a.name > b.name) ? 1 : ((b.name > a.name) ? -1 : 0));
        y.forEach((element) => {
        if (element.payed == true){
            element.is_payed_1 = "Has Paid";
        }
        else{
            element.is_payed_1 = "Not Paid";
            
        }
        });

        
        res += `The book collection has ${this.capacity} empty spots left.\n`
        for (let i = 0; i<y.length;i++){
            res += `${y[i].name} == ${y[i].author} - ${y[i].is_payed_1}.\n`
        }
        
        return res.trim();
        
    }
    else{

        let x = this.books.find(e => e.author === bookAuthor);
        if (x.payed == true){
            x.is_payed_2 = "Has Paid";
        }
        else{
            x.is_payed_2 = "Not Paid";
            
        }
        if (!x){
            throw `${bookAuthor} is not in the collection.`;
        }
        else{
            return `${x.name} == ${x.author} - ${x.is_payed_2}.`
        }
        
        
    }
}
}