function peelTheOnion (s, d) {
  let num=BigInt(s**d)
  let res=[]
  let cumulative=0
  let count=s%2==0 ? 2 : 1
  while (num>0) {
    let pre=BigInt(num)
    let deduct=BigInt(count**d-cumulative)
    num-=deduct
    if (num>=-1999999999n) {
      res.push(Number(pre-num))
    }
    cumulative+=Number(pre-num)
    count+=2
  }
  return res.reverse()
}