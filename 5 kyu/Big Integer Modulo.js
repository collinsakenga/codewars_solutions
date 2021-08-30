function bigModulo(numString, divisor) {
  let res=0
  for (let i of numString) {
    res=(res*10+(+i))%divisor
  }
  return res
}