function getMiddleTs(s: string): string {
  if (s.length % 2 === 0) {
    const middle = s.length / 2;
    return s[middle - 1] + s[middle];
  } else {
    const middle = Math.round(s.length / 2);
    return s[middle - 1];
  }
}
