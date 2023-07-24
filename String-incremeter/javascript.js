function incrementString(input) {
  if (isNaN(parseInt(input[input.length - 1]))) return input + "1";
  return input.replace(/(0*)([0-9]+$)/, function (match, p1, p2) {
    let up = parseInt(p2) + 1;
    return up.toString().length > p2.length ? p1.slice(0, -1) + up : p1 + up;
  });
}

console.log(incrementString("foobar000"), "foobar001");
console.log(incrementString("foobar999"), "foobar1000");
console.log(incrementString("foobar00999"), "foobar01000");
console.log(incrementString("foo"), "foo1");
console.log(incrementString("foobar001"), "foobar002");
console.log(incrementString("foobar1"), "foobar2");
console.log(incrementString("1"), "2");
console.log(incrementString("009"), "010");
console.log(incrementString("fo99obar99"), "fo99obar100");
