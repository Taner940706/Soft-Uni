function construction_crew(obj){
    if (obj.dizziness){
        obj.levelOfHydrated = obj.levelOfHydrated + (obj.weight*obj.experience)/10
        obj.dizziness = false
    }
    return obj
}