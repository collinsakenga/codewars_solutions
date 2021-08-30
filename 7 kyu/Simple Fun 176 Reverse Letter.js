function reverseLetter(str) {
  const res=Array.from(str).reverse()
  return res.filter(s=>"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".includes(s)).join("")
}