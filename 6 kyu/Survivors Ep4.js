function survivors(listOfMomentum, listOfPowerups) {
  let res=[];
  for (let i=0; i<listOfMomentum.length; i++) {
    let index=-1;
    let start=listOfMomentum[i]
    while (index<listOfPowerups[i].length && start>0) {
      start+=listOfPowerups[i][++index]-1;
    }
    if (index==listOfPowerups[i].length) {
      res.push(i)
    }
  }
  return res
}