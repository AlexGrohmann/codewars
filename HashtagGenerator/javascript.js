function generateHashtag(str) {
  let result = "#";
  const words = str.split(" ");
  for (const element of words) {
    result = result + element.charAt(0).toUpperCase() + element.slice(1);
  }
  if (result.length === 1 || result.length > 140) {
    return false;
  } else {
    return result;
  }
}

console.log(generateHashtag(""), false);
console.log(generateHashtag(" ".repeat(200)), false);
console.log(generateHashtag("Do We have A Hashtag"), "#DoWeHaveAHashtag");
console.log(generateHashtag("Codewars"), "#Codewars");
console.log(generateHashtag("Codewars Is Nice"), "#CodewarsIsNice");
console.log(generateHashtag("Codewars is nice"), "#CodewarsIsNice");
console.log(generateHashtag("code" + " ".repeat(140) + "wars"), "#CodeWars");
console.log(
  generateHashtag(
    "Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat"
  ),
  false
);
console.log(generateHashtag("a".repeat(139)), "#A" + "a".repeat(138));
console.log(generateHashtag("a".repeat(140)), false);
