function add(a, b) {
  var res = "",
    c = 0;
  a = a.split("");
  b = b.split("");
  while (a.length || b.length || c) {
    c += ~~a.pop() + ~~b.pop();
    res = (c % 10) + res;
    c = c > 9;
  }
  return res;
}

console.log(add("1", "1"), "2");
console.log(add("123", "456"), "579");
console.log(add("888", "222"), "1110");
console.log(add("1372", "69"), "1441");
console.log(add("12", "456"), "468");
console.log(add("101", "100"), "201");
console.log(
  add("63829983432984289347293874", "90938498237058927340892374089"),
  "91002328220491911630239667963"
);
