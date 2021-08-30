function lastSurvivor(letters, coords) {
  coords.reverse();
  while (coords.length>0) {
    let index=coords.pop();
    letters=letters.substring(0, index)+letters.substring(index+1)
  }
  return letters
}