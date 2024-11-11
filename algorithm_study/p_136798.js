function solution(number, limit, power) {
  const numberOfDivider = [];

  for (let n = 1; n <= number; n++) {
    const divider = [];
    for (let i = 1; i <= Math.sqrt(n); i++) {
      if (n % i == 0) {
        divider.push(i);
        if (i != n / i) divider.push(n / i);
      }
    }
    numberOfDivider.push(divider.length);
  }

  return numberOfDivider.reduce(
    (acc, cur) => acc + (cur > limit ? power : cur),
    0
  );
}
