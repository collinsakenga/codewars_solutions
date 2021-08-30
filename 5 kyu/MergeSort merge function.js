// TODO: implement 'mergesorted'
// test ensures: a and b are both arrays, consisting entirely of integers...
//...,both arrays are sorted and contain at least 1 integer.
// ALSO: the Array.sort function has been disabled for this excercise.
function mergesorted(a, b) {
  if (a===undefined) {
    return b
  } else if (b===undefined) {
    return a
  }
  let i1=0
  let i2=0
  let res=[]
  while (i1<a.length && i2<b.length) {
    if (a[i1]<b[i2]) {
      res.push(a[i1++])
    } else {
      res.push(b[i2++])
    }
  }
  while (i1<a.length) {
    res.push(a[i1++])
  }
  while (i2<b.length) {
    res.push(b[i2++])
  }
  return res
}
