export class Challenge {
  static solution(number: number) {
    let result: number = 0;
    for (let i = 0; i < number; i++) {
      if (i % 5 === 0 || i % 3 === 0) {
        result += i;
      }
    }
    return result; //change this
  }
}
