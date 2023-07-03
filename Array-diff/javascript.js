function arrayDiff(a, b) {
  let result = [];
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

arrayDiff([1, 2, 3], [1, 2]);
arrayDiff([1, 2, 2], [1]);
arrayDiff([1, 2, 2], [2]);
arrayDiff([1, 2, 2], []);
arrayDiff([1, 2, 3], [1, 2]);
