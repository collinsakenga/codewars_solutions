function pay(prices, whoAteWhat){
  let count=Array(prices.length).fill(0)
  for (let i of Object.values(whoAteWhat)) {
    for (let j of i) {
      count[j]+=1
    }
  }
  let res={}
  for (let [i, j] of Object.entries(whoAteWhat)) {
    res[i]=0
    for (let k of j) {
      res[i]+=prices[k]/count[k]
    }
  }
  return res
}