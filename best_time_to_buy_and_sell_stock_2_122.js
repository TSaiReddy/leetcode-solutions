function maxProfit(prices) {
  let totalProfit = 0;

  for (let i = 1; i < prices.length; i++)
    if (prices[i] > prices[i - 1]) totalProfit += prices[i] - prices[i - 1];

  return totalProfit;
}

console.log(maxProfit([7, 1, 5, 3, 6, 4])); // 1 - 5 = 4; 3 - 6 = 3 ==> 7
console.log(maxProfit([1, 2, 3, 4, 5])); // 1 - 5 ==> 4
console.log(maxProfit([7, 6, 4, 3, 1])); // 0
console.log(maxProfit([6, 1, 3, 2, 4, 7])); // 1 - 3 = 2; 2 - 7 = 5 ==> 7
