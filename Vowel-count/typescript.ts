export class Kata {
  static getCount(str: string): number {
    let count: number = 0;
    for (let i = 0; i < str.length; i++) {
      const char: string = str.charAt(i);
      if (
        char === "a" ||
        char === "e" ||
        char === "i" ||
        char === "o" ||
        char === "u"
      ) {
        count++;
      }
    }
    return count;
  }
}
