String.prototype.toJadenCase = function () {
  return this.split(" ")
    .map((w) => w[0].toUpperCase() + w.slice(1))
    .join(" ");
};

var str = "How can mirrors be real if our eyes aren't real";
console.log(str.toJadenCase());
