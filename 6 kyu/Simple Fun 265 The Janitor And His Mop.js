function theJanitor(word) {
  length=word.length
  s1=word;
  s2=word.split("").reverse().join("");
  res=new Array(26).fill(0)
  for (let i=0; i<26; i++) {
    let char=String.fromCharCode(97+i)
    let left=s1.indexOf(char), right=length-s2.indexOf(char)
    if (left!=-1) {
      res[i]=right-left;
    }
  }
  return res
}