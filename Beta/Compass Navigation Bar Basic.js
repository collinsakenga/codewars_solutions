function getCompass(yaw) {
  let arr=['NW', 'N', 'NE', 'E', 'SE', 'S', 'SW', 'W'];
  let start=Math.floor(((yaw%360+315)%360)/45);
  let res=[]
  for (let i=0; i<5; i++) {
    res.push(arr[start])
    start=(start+1)%arr.length
  }
  return res.join("..")
}