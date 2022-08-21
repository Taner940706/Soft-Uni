class Garden {

    constructor(spaceAvailable){
        this.spaceAvailable = spaceAvailable;
        this.plants = [];
        this.storage = [];
    }

    addPlant (plantName, spaceRequired){
        let obj = {};
        if (this.spaceAvailable < spaceRequired){
            throw "Not enough space in the garden.";
        }
        obj.name = plantName
        obj.space = spaceRequired;
        obj.ripe = false;
        obj.quantity = 0;
        this.plants.push(obj);
        this.spaceAvailable -= spaceRequired;
        return `The ${plantName} has been successfully planted in the garden.`;
    }

    ripenPlant(plantName, quantity){
        if (!this.plants.find((plant) => plant.name === plantName)){
            throw `There is no ${plantName} in the garden.`;
        }
        if (this.plants.find((plant) => plant.name === plantName).ripe){
            throw `The ${plantName} is already ripe.`;
        }
        if (quantity <= 0){
            throw "The quantity cannot be zero or negative."
        }

        this.plants.find((plant) => plant.name === plantName).ripe = true;
        this.plants.find((plant) => plant.name === plantName).quantity += quantity;
        if (quantity == 1){
            return `${quantity} ${plantName} has successfully ripened.`;
        }
        else{
            return `${quantity} ${plantName}s have successfully ripened.`;
        }

    }

    harvestPlant(plantName){
        let obj = {};
        if (!this.plants.find((plant) => plant.name === plantName)){
            throw `There is no ${plantName} in the garden.`;
        }
        if (!this.plants.find((plant) => plant.name === plantName).ripe){
            throw `The ${plantName} cannot be harvested before it is ripe.`;
        }
        let x = this.plants.find((plant) => plant.name === plantName);
        this.plants = this.plants.filter(data => data.name !== plantName);
        obj.plantName = plantName;
        obj.quantity = x.quantity;
        this.spaceAvailable +=  x.space;
        this.storage.push(obj);
        return `The ${plantName} has been successfully harvested.`;
    }

    generateReport(){
        let res = ""
        res += `The garden has ${ this.spaceAvailable } free space left.\n`;
        let x = this.plants.sort((a, b) => {
            return a.name - b.name;
        });

        res +=`Plants in the garden: ${this.plants.map(u => u.name).join(', ')}\n`;

        if (this.storage.length == 0){
            res += "Plants in storage: The storage is empty."
        }
        else{
            res += `Plants in storage: ${this.storage.map(u => u.plantName+" "+"("+u.quantity+")").join(', ')}`;
        }

        return res.trim();
    }
}