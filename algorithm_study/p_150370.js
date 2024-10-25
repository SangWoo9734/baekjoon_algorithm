function solution(today, terms, privacies) {
  let answer = [];
  const termsDuration = {};
  const [year, month, date] = today.split(".").map(Number);

  terms.forEach((t) => {
    const [type, duration] = t.split(" ");
    termsDuration[type] = parseInt(duration);
  });

  privacies.forEach((p, index) => {
    const [startDate, term] = p.split(" ");
    const [pYear, pMonth, pDate] = startDate.split(".").map(Number);
    const duration = termsDuration[term];

    let expireYear = pYear + Math.floor((pMonth + duration - 1) / 12);
    let expireMonth = ((pMonth + duration - 1) % 12) + 1;
    const expireDate = pDate;

    if (
      expireYear < year ||
      (expireYear === year && expireMonth < month) ||
      (expireYear === year && expireMonth == month && expireDate <= date)
    )
      answer.push(index + 1);
  });

  return answer;
}
