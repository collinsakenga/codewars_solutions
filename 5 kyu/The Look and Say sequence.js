function getLines(line){
  if (line<=0 || isNaN(line)) {
    return -1
  }
  let res=["1"]
  for (let i=0; i<line-1; i++) {
    let temp=[]
    let s=""
    for (let char of res[res.length-1]+" ") {
      if (s==="" || s[s.length-1]===char) {
        s+=char
      } else {
        temp.push(s)
        s=char
      }
    }
    let final=""
    for (let word of temp) {
      final+=word.length+word[0]
    }
    res.push(final)
  }
  return res.join(",")
}