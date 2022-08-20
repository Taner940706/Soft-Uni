function car_factory(obj){
    if (obj.power <= 90){
        obj.power = 90
        obj.volume = 1800
    }
    else if (obj.power>90 && obj.power <= 120){
        obj.power = 120
        obj.volume = 2400
    }
    else if (obj.power>120 && obj.power <= 200){
        obj.power = 200
        obj.volume = 3500
    }
    else {
        obj.power = 200
        obj.volume = 3500
    }
    if(obj.wheelsize % 2 == 0){
        obj.wheelsize = obj.wheelsize - 1
    }

    res = { model: obj.model,
    engine: { power: obj.power,
              volume: obj.volume },
    carriage: { type: obj.carriage,
                color: obj.color },
    wheels: [obj.wheelsize, obj.wheelsize, obj.wheelsize,obj.wheelsize] }

    return(res)
}