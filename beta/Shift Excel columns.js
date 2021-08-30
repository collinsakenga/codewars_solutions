const shiftColumns = (column, shift) => {
  const table = new Map();
  const table2 = new Map();
  for (let [i, j] of Object.entries("abcdefghijklmnopqrstuvwxyz".toUpperCase())) {
    table[j]=Number(i)+1
    table2[Number(i)+1]=j
  }
  let newNum=[...column].reduce((prev, cur, index) => {
    return prev+table[cur]*(26**(column.length-1-index))
  }, 0)+shift
  const res=[]
  let div=1
  while (newNum) {
    let newDiv=div*26
    let index=Math.floor(((newNum)%newDiv)/div) 
    if (index===0) {
      index=26
    }
    res.push(table2[index])
    newNum-=index*div
    div=newDiv
  }
  return res.reverse().join("")
}