function solution(n) {
  const isPrime = new Array(n + 1).fill(true);

  for (let i = 2; i < n + 1; i += 1) {
    if (isPrime[i]) {
      let primeIndex = i * 2;

      while (primeIndex < n + 1) {
        isPrime[primeIndex] = false;
        primeIndex += i;
      }
    }
  }

  return isPrime.reduce((acc, cur) => acc + (cur ? 1 : 0), 0) - 2;
}
