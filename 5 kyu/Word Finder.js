function Dictionary(words) {
  this.words = words;
}

Dictionary.prototype.getMatchingWords = function(pattern) {
  res=[]
  for (let s of this.words) {
    if (s.length!==pattern.length) {
      continue
    }
    flag=true
    for (let i=0; i<pattern.length; i++) {
      if (pattern[i]=="?" || pattern[i]==s[i]) {
        continue
      }
      flag=false
      break
    }
    if (flag) {
      res.push(s)
    }
  }
  return res
}