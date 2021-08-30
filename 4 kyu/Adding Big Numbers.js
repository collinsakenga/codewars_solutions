function add(a, b) {
  let arr=[]
  let carry=0
  a=a.padStart(b.length, "0")
  b=b.padStart(a.length, "0")
  for (let i=a.length-1; i>=0; i--) {
    let num=+(a[i])+(+b[i])+carry
    arr.push((num%10).toString())
    carry=Math.floor(num/10)
  }
  if (carry>0) {
    arr.push(carry)
  }
  while (arr.length>0 && arr[arr.length-1]=="0") {
    arr.pop()
  }
  return arr.reverse().join("")
}