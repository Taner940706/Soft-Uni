function solution() {

    let supplies = { protein: 0, carbohydrate: 0, fat: 0, flavour: 0 }
  
    let foodRecipes = {
      apple: { protein: 0, carbohydrate: 1, fat: 0, flavour: 2 },
      lemonade: { protein: 0, carbohydrate: 10, fat: 0, flavour: 20 },
      burger: { protein: 0, carbohydrate: 5, fat: 7, flavour: 3 },
      eggs: { protein: 5, carbohydrate: 0, fat: 1, flavour: 1 },
      turkey: { protein: 10, carbohydrate: 10, fat: 10, flavour: 10 },
      cookRecipe(recipe, quantity) {
  
        let deductedQuantity = {};
  
        for (const value in this[recipe]) {
          if (this[recipe][value] * quantity > supplies[value]) {
            return `Error: not enough ${value} in stock`;
          }
          deductedQuantity[value] = supplies[value] - this[recipe][value] * quantity;
        }
  
        Object.assign(supplies, deductedQuantity);
        return 'Success';
  
      }
    }
  
    return controller = (str) => {
  
      if (str.includes('restock')) {
        let [, nutrient, quantity] = str.split(' ');
        supplies[nutrient] += Number(quantity);
        return 'Success';
      }
  
      if (str.includes('prepare')) {
        let [,  recipe, quantity] = str.split(' ');
        return foodRecipes.cookRecipe(recipe, Number(quantity));
      }
  
      return `protein=${supplies.protein} carbohydrate=${supplies.carbohydrate} fat=${supplies.fat} flavour=${supplies.flavour}`;
  
    }
  
  }