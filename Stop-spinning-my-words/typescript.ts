export function spinWords(words: string): string {
  let wordsSplit: Array<string> = words.split(" ");
  let result: string = "";
  wordsSplit.forEach((word: string) => {
    if (word.length >= 5) {
      result += " " + word.split("").reverse().join("");
    } else {
      result += " " + word;
    }
  });
  return result.trim();
}
