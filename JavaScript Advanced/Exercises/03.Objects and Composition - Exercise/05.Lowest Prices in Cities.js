function Lowest_Prices_in_Cities(input){

    let products = [];

    while (input.length > 0){
        let [town, product, price] = input.shift().split(" | ");

        if (products.filter(x => x.product === product).length > 0){
            let obj = products.find(x=>x.product === product);

            if (obj.price > Number(price)){
                obj.price = Number(price)
                obj.town = town
            }

        }
        else{
            let obj = {product,town,price:Number(price)};
            products.push(obj)
        }
    }

    for (let product of products){
        console.log(`${product.product} -> ${product.price} (${product.town})`)
    }

}