function highAndLow(numbers) {
  const parts = numbers.split(" ");
  let smallest = parts[0];
  let biggest = parts[0];
  for (const element of parts) {
    if (Number(element) > biggest) {
      biggest = Number(element);
    }
    if (Number(element) < smallest) {
      smallest = Number(element);
    }
  }
  console.log(biggest + " " + smallest);
  return biggest + " " + smallest;
}

highAndLow("8 3 -5 42 -1 0 0 -9 4 7 4 -4");
