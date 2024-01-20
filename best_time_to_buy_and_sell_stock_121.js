function maxProfit(prices) {
  let buy_price = prices[0];
  let cur_profit = 0;
  let max_profit = 0;

  for (let i = 0; i < prices.length; i++) {
    const element = prices[i];

    if (buy_price > element) {
      buy_price = element;
    }

    if (element >= buy_price) {
      cur_profit = element - buy_price;
    }

    if (max_profit < cur_profit) {
      max_profit = cur_profit;
    }
  }
  return max_profit;
}
// console.log(maxProfit([2, 4, 1])); // 2 - 4 = 2
// console.log(maxProfit([4, 7, 1, 2])); // 4 - 7 = 3
console.log(maxProfit([7, 1, 5, 3, 6, 4])); // 1 - 6 = 5
