export function between(min: number, n: number, max: number) {
  // x in [min, max)
  return min <= n && n < max;
}