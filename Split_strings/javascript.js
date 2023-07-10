function solution(str) {
  let inputArray = str.split("");
  if (inputArray.length % 2 !== 0) {
    inputArray.push("_");
  }
  let result = [];
  for (let i = 0; i < inputArray.length; i = i + 2) {
    result.push(inputArray[i] + inputArray[i + 1]);
  }

  return result;
}

console.log(solution("abcdefg"));
console.log(solution("abcdef"));

// function solution(s){
//     return (s+"_").match(/.{2}/g)||[]
//  }
