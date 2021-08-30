function lastSurvivors(str) {
  const a="a".charCodeAt(0);
  let flag=true;
  let table={};
  for (let i of str) {
    if (!(i in table)) {
      table[i]=1;
    } else {
      table[i]+=1;
    }
  }
  while (flag) {
    flag=false;
    for (let k of Object.keys(table)) {
      if (table[k]>1) {
        flag=true;
        let num=Math.floor(table[k]/2);
        table[k]-=num*2;
        let char=String.fromCharCode(a+(k.charCodeAt(0)-a+1)%26);
        if (!(char in table)) {
          table[char]=num;
        } else {
          table[char]+=num;
        }
      }
    }
  }
  let res="";
  for (const [k, v] of Object.entries(table)) {
    res+=k.repeat(v)
  }
  return res
}