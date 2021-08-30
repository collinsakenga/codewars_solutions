function permissions (code, fileName) {
  let first=+(code[0]==='r')*4+(+(code[1]==="w")*2)+(+(code[2]==="x"))
  let second=+(code[3]==='r')*4+(+(code[4]==="w")*2)+(+(code[5]==="x"))
  let third=+(code[6]==='r')*4+(+(code[7]==="w")*2)+(+(code[8]==="x"))
  return `chmod ${first}${second}${third} ${fileName}`
}