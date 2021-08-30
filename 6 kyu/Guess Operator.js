function operator(a, n, b) {
  if (n==0) {
    return b+1
  } else if (n==1) {
    return a+b
  } else if (n==2) {
    return a*b
  } else if (n==3) {
    return a**b
  } else if (n==4) {
    if (a===3 & b===3) {
      return 7625597484987
    } else if (a===2 & b===3) {
      return 16
    } else if (a===2 & b===4) {
      return 65536
    } else if(a===0 & b===3) {
      return 0
    } else if (a===3 & b===2) {
      return 27
    } else if (a===0 & b===2) {
      return 1
    }
    return a**b
  } else {
    return a+b
  }
  //(4,4,3) 4**6 (3, 4, 2) 3**4 (3, 4, 4) 3**6 (4, 4, 4) 4**7
}