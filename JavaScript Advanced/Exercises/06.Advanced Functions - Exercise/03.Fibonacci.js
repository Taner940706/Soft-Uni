function getFibonator() {
    
    let n1 = 0, n2 = 1, nextTerm;

    return function fib(){
        nextTerm = n1 + n2;
        n1 = n2;
        n2 = nextTerm;
        return(n1);
    }
  }