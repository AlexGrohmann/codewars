function spinWords(string) {
  let words = string.split(" ");
  let result = "";
  words.forEach((word) => {
    if (word.length >= 5) {
      result += " " + word.split("").reverse().join("");
    } else {
      result += " " + word;
    }
  });
  return result.trim();
}
