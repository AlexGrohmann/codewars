function isValidWalkTs(walk: string[]) {
  const verticalWalk: boolean =
    walk.filter((i) => i === "n").length ==
    walk.filter((i) => i === "s").length;
  const horizontalWalk: boolean =
    walk.filter((i) => i === "e").length ==
    walk.filter((i) => i === "w").length;
  const length: boolean = walk.length == 10;
  console.log(!!verticalWalk && !!horizontalWalk && !!length);
  return !!verticalWalk && !!horizontalWalk && !!length;
}

isValidWalk(["n", "s", "n", "s", "n", "s", "n", "s", "n", "s"]);
isValidWalk(["w", "e", "w", "e", "w", "e", "w", "e", "w", "e", "w", "e"]);
isValidWalk(["w"]);
isValidWalk(["n", "n", "n", "s", "n", "s", "n", "s", "n", "s"]);
