function getCommonDirectoryPath(pathes) {
  let length=Number.MAX_SAFE_INTEGER
  for (let i=0; i<pathes.length; i++) {
    pathes[i]=pathes[i].split("/")
    length=Math.min(length, pathes[i].length)
  }
  let s=[]
  for (let i=0; i<length; i++) {
    let compare=pathes[0][i]
    for (let j=1; j<pathes.length; j++) {
      if (compare!==pathes[j][i]) {
        return s.length!==0 ? s.join("/")+"/" : ""
      }
    }
    s.push(compare)
  }
  return s.length!==0 ? s.join("/")+"/" : ""
}