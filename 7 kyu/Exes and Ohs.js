function XO(str) {
  str=str.toLowerCase()
  return str.split("x").length==str.split("o").length
}