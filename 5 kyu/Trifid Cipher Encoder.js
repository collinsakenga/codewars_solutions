function trifidEncode(key, period, data){
  let res=[[], [], []]
  for (let i of data) {
    let num=key.indexOf(i)
    let first=Math.ceil((num+1)/9), second=Math.ceil((num%9+1)/3), third=num%3+1
    res[0].push(first)
    res[1].push(second)
    res[2].push(third)
  }
  let s=""
  for (let i=0; i<Math.ceil(res[0].length/period); i++) {
    let size=Math.min(res[0].length-period*i, period)
    let temp=Array(size*3)
    let cur=period*i
    for (let j=0; j<size; j++) {
      temp[j]=res[0][cur+j]
      temp[j+size]=res[1][cur+j]
      temp[j+size*2]=res[2][cur+j]
    }
    for (let j=0; j<temp.length; j+=3) {
      let pos=(temp[j]-1)*9+(temp[j+1]-1)*3+(temp[j+2]-1)
      s+=key[pos]
    }
  }
  return s
}
function trifidDecode(key, period, data){
  let res=[[], [], []]
  for (let i of data) {
    let num=key.indexOf(i)
    let first=Math.ceil((num+1)/9), second=Math.ceil((num%9+1)/3), third=num%3+1
    res[0].push(first)
    res[1].push(second)
    res[2].push(third)
  }
  let decode=[[], [], []]
  for (let i=0; i<Math.ceil(res[0].length/period); i++) {
    let size=Math.min(res[0].length-period*i, period)
    let cur=period*i
    let arr=[]
    for (let j=0; j<size; j++) {
      arr.push(res[0][cur+j], res[1][cur+j], res[2][cur+j])
    }
    for (let j=0; j<arr.length; j++) {
      if (j<size) {
        decode[0].push(arr[j])
      } else if (j<size*2) {
        decode[1].push(arr[j])
      } else {
        decode[2].push(arr[j])
      }
    }
  }
  let s=""
  for (let j=0; j<decode[0].length; j++) {
    let pos=(decode[0][j]-1)*9+(decode[1][j]-1)*3+(decode[2][j]-1)
    s+=key[pos]
  }
  return s
}