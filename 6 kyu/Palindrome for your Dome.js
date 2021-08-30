function palindrome(string) {
  let s=""
  for (let char of string) 
    {
      let n = char.charCodeAt(s);
      if ((n >= 65 && n < 91) || (n >= 97 && n < 123)) {
        s+=char.toLowerCase()
      }
    }
  return helper(s)
}
function helper(s) {
  if (s.length<=1) {
    return true
  } else if (s[0]!=s[s.length-1]) {
    return false
  }
  return helper(s.slice(1, s.length-1))
}