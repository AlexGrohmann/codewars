function flickSwitch(arr) {
  let result = [];
  let state = true;
  arr.forEach((item) => {
    if (item === "flick") {
      state = !state;
    }
    result.push(state);
  });
  return result;
}
