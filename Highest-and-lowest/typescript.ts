export class Kata {
  static highAndLow2(numbers: string): string {
    const parts = numbers.split(" ");
    let smallest: number = Number(parts[0]);
    let biggest: number = Number(parts[0]);
    for (const element of parts) {
      if (Number(element) > biggest) {
        biggest = Number(element);
      }
      if (Number(element) < smallest) {
        smallest = Number(element);
      }
    }
    return biggest + " " + smallest;
  }

  static highAndLow(numbers: string) {
    const max = Math.max(...numbers.split(" ").map((i) => +i));
    const min = Math.min(...numbers.split(" ").map((i) => +i));

    return `${max} ${min}`;
    // throw new NotImplementedException() ?
    // No, wait, this is TypeScript.
  }
}
