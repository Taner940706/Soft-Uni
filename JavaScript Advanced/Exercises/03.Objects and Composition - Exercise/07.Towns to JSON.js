function Towns_to_JSON(arr){

    const result = []
    const splitted = arr[0].split("|");
    const town = splitted[1].trim();
    const latitude = splitted[2].trim();
    const longitude = splitted[3].trim();
    for (let i=1;i< arr.length;i++){
        const obj = {};
        const splttedEntry = arr[i].split("|")
        obj[town] = splttedEntry[1].trim();
        obj[latitude] = Number(Number(splttedEntry[2].trim()).toFixed(2));
        obj[longitude] = Number(Number(splttedEntry[3].trim()).toFixed(2));
        result.push(obj)
    }
    console.log(JSON.stringify(result))

}