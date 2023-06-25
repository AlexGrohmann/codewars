function sumDigits(number) {
  let result = 0;
  for (let i = 0; i < number.toString().length; i++) {
    if (number.toString().charAt(i) !== "-") {
      result += Number(number.toString().charAt(i));
    }
  }
  console.log(result);
  return result;
}

sumDigits(-52);
