function likes(names) {
  switch (names.length) {
    case 0:
      return "no one likes this";
    case 1:
      return names[0] + " likes this";
    default:
      if (names.length > 3) {
        return (
          names[0] +
          ", " +
          names[1] +
          " and " +
          (names.length - 2) +
          " others like this"
        );
      }
      let result = "";
      names.map((name, index) => {
        if (index + 1 >= names.length) {
          result += " and " + name;
        } else if (index === 0) {
          result += name;
        } else {
          result += ", " + name;
        }
      });
      return result + " like this";
  }
}

function likesBestPractice(names) {
  names = names || [];
  switch (names.length) {
    case 0:
      return "no one likes this";
    case 1:
      return names[0] + " likes this";
    case 2:
      return names[0] + " and " + names[1] + " like this";
    case 3:
      return names[0] + ", " + names[1] + " and " + names[2] + " like this";
    default:
      return (
        names[0] +
        ", " +
        names[1] +
        " and " +
        (names.length - 2) +
        " others like this"
      );
  }
}
