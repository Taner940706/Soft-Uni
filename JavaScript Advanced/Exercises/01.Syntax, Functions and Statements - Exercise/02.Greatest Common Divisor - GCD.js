function gcd(first, second)
{
    temp = 0
    for (let i = second;i>=1;i--){
        if (first % i == 0 && second % i == 0){
            temp = i
            break
        }
        
    }
    console.log(temp)
}