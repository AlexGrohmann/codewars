function humanReadable(seconds) {
  let hoursLeft = Math.floor(seconds / 3600);
  let min = Math.floor((seconds - hoursLeft * 3600) / 60);
  let secondsLeft = seconds - hoursLeft * 3600 - min * 60;
  secondsLeft = Math.round(secondsLeft * 100) / 100;
  let hhString = hoursLeft.toString();
  let mmString = min.toString();
  let ssString = secondsLeft.toString();
  if (hhString.length < 2) {
    hhString = "0" + hhString;
  }
  if (mmString.length < 2) {
    mmString = "0" + mmString;
  }
  if (ssString.length < 2) {
    ssString = "0" + ssString;
  }
  return hhString + ":" + mmString + ":" + ssString;
}

console.log(humanReadable(0));
console.log(humanReadable(59));
console.log(humanReadable(60));
console.log(humanReadable(90));
console.log(humanReadable(3599));
console.log(humanReadable(3600));
console.log(humanReadable(45296));
console.log(humanReadable(86399));
console.log(humanReadable(86400));
console.log(humanReadable(359999));
