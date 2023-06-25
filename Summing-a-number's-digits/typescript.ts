export function sumDigits(n: number): number {
  let result: number = 0;
  for (let i: number = 0; i < n.toString().length; i++) {
    if (n.toString().charAt(i) !== "-") {
      result += Number(n.toString().charAt(i));
    }
  }
  return result;
}
