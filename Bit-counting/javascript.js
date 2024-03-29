var countBits = function (n) {
  return n
    .toString(2)
    .split("")
    .reduce((sum, num) => sum + Number(num), 0);
};

const countBitsNiceVersion = (n) =>
  n
    .toString(2)
    .split("")
    .filter((ele) => ele == 1).length;
