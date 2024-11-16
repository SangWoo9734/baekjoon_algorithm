function getDividable(arrA, arrB) {
  let res = 0;

  const gcd = (a, b) => (a % b === 0 ? b : gcd(b, a % b));

  arrA.forEach((val) => (res = gcd(res, val)));

  if (arrB.some((val) => val % res === 0)) return 0;

  return res;
}

function solution(arrayA, arrayB) {
  let resA = getDividable(arrayA, arrayB);
  let resB = getDividable(arrayB, arrayA);
  return Math.max(resA, resB);
}
