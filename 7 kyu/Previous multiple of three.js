const prevMultOfThree = n => {
  while (n && sumDigits(n)%3!=0) {
    n=Math.trunc(n/10);
  }
  return n===0 ? null : n
}
const sumDigits = n => {
  let res=0
  while (n) {
    res+=n%10
    n=Math.trunc(n/10);
  }
  return res
}