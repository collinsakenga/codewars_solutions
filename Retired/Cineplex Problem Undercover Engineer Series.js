function planMeals(list){
  const res={}
  for (let i of list) {
    if (!(i.meal in res)) {
      res[i.meal]=1
    } else {
      res[i.meal]++;
    }
  }
  return res
}
function planMealsWithShortage(list,NotAvailable){
  const disallow=new Set(NotAvailable)
  const res={}
  for (let i of list) {
    const meal=i.meal
    if (disallow.has(meal)) {
      continue
    }
    if (!(meal in res)) {
      res[meal]=1
    } else {
      res[meal]++;
    }
  }
  return res
}
function planMealsWithAlternative(list,NotAvailable){
  const res=planMealsWithShortage(list,NotAvailable)
  const disallow=new Set(NotAvailable)
  const replace = Object.entries(res).reduce((prev, cur) => {
    const [key, val]=cur
    if (prev===null || res[key]>res[prev] || (res[key]===res[prev] && key.localeCompare(prev)<0)) {
      return key
    }
    return prev
  }, null)
  const newRes={}
  for (let i of list) {
    const meal=i.meal
    if (disallow.has(meal)) {
      if (!(replace in newRes)) {
        newRes[replace]=1
      } else {
        newRes[replace]++;
      }
      continue
    }
    if (!(meal in newRes)) {
      newRes[meal]=1
    } else {
      newRes[meal]++;
    }
  }
  return newRes
}