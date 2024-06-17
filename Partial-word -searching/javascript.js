function wordSearch(query, seq) {
  const result = seq.filter((str) =>
    str.toLowerCase().includes(query.toLowerCase())
  );
  if (result.length == 0) {
    return ["Empty"];
  } else {
    return result;
  }
}

console.log(wordSearch("aB", ["za", "ab", "abc", "zab", "zbc"]), [
  "ab",
  "abc",
  "zab",
]);
console.log(wordSearch("ab", ["za", "ab", "abc", "zab", "zbc"]), [
  "ab",
  "abc",
  "zab",
]);
console.log(wordSearch("ab", ["za", "aB", "Abc", "zAB", "zbc"]), [
  "aB",
  "Abc",
  "zAB",
]);
console.log(wordSearch("abcd", ["za", "aB", "Abc", "zAB", "zbc"]), ["Empty"]);
