function arrayDiffTS(a: Array<number>, b: Array<number>): Array<number> {
  let result: Array<number> = [];
  if (b.length === 0) {
    return a;
  }
  for (const elementA of a) {
    let set = false;
    for (const elementB of b) {
      if (elementA === elementB) {
        set = true;
      }
    }
    if (!set) {
      result.push(elementA);
    }
  }
  console.log(result);
  return result;
}

arrayDiffTS([1, 2, 3], [1, 2]);
arrayDiffTS([1, 2, 2], [1]);
arrayDiffTS([1, 2, 2], [2]);
arrayDiffTS([1, 2, 2], []);
arrayDiffTS([1, 2, 3], [1, 2]);
