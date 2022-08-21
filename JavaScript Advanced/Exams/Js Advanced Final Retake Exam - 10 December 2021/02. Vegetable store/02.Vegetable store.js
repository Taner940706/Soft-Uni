class VegetableStore {
    constructor(owner, location) {
        this.owner = owner;
        this.location = location;
        this.availableProducts = [];
        this._products = [];
    }

    loadingVegetables(vegetables) {
        let addedProducts = [];

        for (let element of vegetables) {
            let [type, quantity, price] = element.split(` `);

            price = Number(price);
            quantity = Number(quantity);

            const targetProduct = this.availableProducts.find(pro => pro.type == type);

            if (!targetProduct) {
                const newProduct = {
                    type,
                    price,
                    quantity,
                };

                this.availableProducts.push(newProduct);
            } else {
                const currentPrice = targetProduct.price;

                if (currentPrice < price) {
                    targetProduct.price = price;
                }

                targetProduct.quantity += quantity;
            }
        }

        let uniq = [...new Set(this.availableProducts.map(p => p.type))].join(`, `);

        return `Successfully added ${this.availableProducts.map(p => p.type).join(', ')}`;
    }

    buyingVegetables(selectedProducts) {
        let totalPrice = 0;

        for (let element of selectedProducts) {
            let [type, quantity] = element.split(` `);
            quantity = Number(quantity);

            const targetProduct = this.availableProducts.find(pro => pro.type == type);

            if (!targetProduct) {
                throw new Error(`${type} is not available in the store, your current bill is $${totalPrice.toFixed(2)}.`)
            }
            let currentQuantity = targetProduct.quantity;
            let price = targetProduct.price;
            if (currentQuantity < quantity) {
                throw new Error(`The quantity ${quantity} for the vegetable ${type} is not available in the store, your current bill is $${totalPrice.toFixed(2)}.`);
            } else {
                targetProduct.quantity -= quantity;
                totalPrice += price * quantity;
            }
        }

        return `Great choice! You must pay the following amount $${totalPrice.toFixed(2)}.`;
    }

    rottingVegetable(type, quantity) {
        let result = ``;

        const targetProduct = this.availableProducts.find(pro => pro.type == type);

        if (!targetProduct) {
            throw new Error(`${type} is not available in the store.`);
        } else {
            let product = targetProduct.type;
            let availableQuantity = targetProduct.quantity;

            if (product == type) {


                if (availableQuantity < quantity) {
                    targetProduct.quantity = 0;
                    result = `The entire quantity of the ${type} has been removed.`;
                } else {
                    targetProduct.quantity -= quantity;
                    result = `Some quantity of the ${type} has been removed.`;
                }
            }

            return result;
        }
    }

    revision() {
        let result = [];

        result.push(`Available vegetables:`);

        this.availableProducts.sort((a, b) => a.price - b.price);

        for (let element of this.availableProducts) {
            result.push(`${element.type}-${element.quantity}-$${element.price}`);
        }

        result.push(`The owner of the store is ${this.owner}, and the location is ${this.location}.`);

        return result.join(`\n`);
    }
}