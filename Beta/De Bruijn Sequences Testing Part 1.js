function deBruijnSequence(sequence, n){
  let res=new Set();
  sequence=sequence+sequence.substring(0, n-1)
  for (let i=0; i<sequence.length; i++) {
    let s=sequence.substring(i, i+n)
    if (res.has(s)) {
      return false
    }
    res.add(s)
  }
  return true
}