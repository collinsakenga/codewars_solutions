function multiply(a, b)
{
  let res=new Array(a.length+b.length).fill(0, 0, a.length+b.length);
  console.log(a, b)
  a=a.split("").reverse()
  b=b.split("").reverse()
  cur=a.length-1
  while (cur>=0) {
    let temp=b.length-1
    while (temp>=0) {
      let index=res.length-cur-temp-1
      res[index]+=+(a[cur])*+(b[temp])
      temp-=1
    }
    cur-=1
  }
  for (let i=res.length-1; i>0; i--) {
    res[i-1]+=Math.floor(res[i]/10)
    res[i]%=10
  }
  let start=0
  while (res[start]<res.length && res[start]==0) {
    start+=1
  }
  return res.slice(start).join("") || "0"
}