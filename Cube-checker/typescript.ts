function cubeCheckerTypeScript(volume: number, side: number): boolean {
  if (volume < 1) {
    return false;
  }
  if (side < 1) {
    return false;
  }
  return volume / side / side / side === 1;
}
