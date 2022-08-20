function first_task(fruit, weight, price_per_kilos)
{
    money = weight*price_per_kilos/1000
    console.log(`I need $${money.toFixed(2)} to buy ${(weight/1000).toFixed(2)} kilograms ${fruit}.`)
}