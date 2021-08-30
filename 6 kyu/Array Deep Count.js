let total=0
function deepCount(a){
  let record=total
  for (let i=0; i<a.length; i++) {
    if (Array.isArray(a[i])) {
      total++
      deepCount(a[i])
    } else {
      total++
    }
  }
  return total-record
}