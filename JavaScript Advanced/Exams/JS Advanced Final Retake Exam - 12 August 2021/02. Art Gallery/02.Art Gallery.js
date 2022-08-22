class ArtGallery{
    
    constructor(creator){
        this.creator = creator;
        this.possibleArticles = { "picture":200,"photo":50,"item":250 };
        this.listOfArticles = [];
        this.guests = [];
    }
    
    addArticle( articleModel, articleName, quantity ){
        let art = ["picture","Picture","PICTURE","photo","Photo","PHOTO","item", "Item","ITEM"];
        let obj = {};
        if (!art.includes(articleModel)){
            throw "This article model is not included in this gallery!";
        }
        if (this.listOfArticles.find( ({ name }) => name === articleName) ){
            this.listOfArticles.find( ({ name }) => name === articleName ).quantity += Number(quantity);
            return `Successfully added article ${articleName} with a new quantity- ${quantity}.`
        }
        else{
            obj.model = articleModel.toLowerCase();
            obj.name = articleName;
            obj.quantity = quantity;
            this.listOfArticles.push(obj);
            return `Successfully added article ${articleName} with a new quantity- ${quantity}.`
        }
    }
    
    inviteGuest ( guestName, personality){
        let obj = {};
        if (this.guests.find( ({ name }) => name === guestName)){
            throw new Error(`${guestName} has already been invited.`)
        }
        else{
            obj.name = guestName;
            if (personality == "Vip"){
                obj.points = 500;
            }
            else if (personality == "Middle"){
                obj.points = 250;
            }
            else{
                 obj.points = 50;
            }
            
        }
        obj.purchaseArticle = 0;
        this.guests.push(obj)
        return `You have successfully invited ${guestName}!`;
        
    }
    
    buyArticle ( articleModel, articleName, guestName){
        if (!this.listOfArticles.find((p) => p.name == articleName && p.model === articleModel))
        {
            throw new Error("This article is not found.");
        }
        if (this.listOfArticles.find( ({ name }) => name === articleName).quantity == 0 ){
            return `The ${articleName} is not available.`; 
         }
        if (!this.guests.find( ({ name }) => name === guestName)){
            return "This guest is not invited."
         }
         
         let x = this.guests.find( ({ name }) => name === guestName).points;
         let y =  this.possibleArticles[articleModel];
         
         if (x<y){
             return "You need to more points to purchase the article.";
         }
         else{
             x -= y;
             this.listOfArticles.find( ({ name }) => name === articleName).quantity -= 1;
             this.guests.find( ({ name }) => name === guestName).purchaseArticle += 1;
             return `${guestName} successfully purchased the article worth ${y} points.`;
         }
         
        
    }
    
    showGalleryInfo (criteria){
        let res = "";
        if (criteria == "article"){
            res += "Articles information:\n";
            for (let i=0;i<this.listOfArticles.length;i++){
                res += `${this.listOfArticles[i].model} - ${this.listOfArticles[i].name} - ${this.listOfArticles[i].quantity}\n`;
            }
            
        }
        else{
            res += "Guests information:\n";
            for (let i=0;i<this.guests.length;i++){
                res += `${this.guests[i].name} - ${this.guests[i].purchaseArticle}\n`;
            }
        }
        
        return res.trim();
    }
    
    
}