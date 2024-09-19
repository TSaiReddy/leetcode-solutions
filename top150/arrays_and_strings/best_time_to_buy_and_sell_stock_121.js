function maxProfit(prices) {
  let profit = 0;
  let buyPrice = prices[0];

  for (const price of prices) {
    if (price - buyPrice > profit) {
      profit = price - buyPrice;
    }
    if (buyPrice > price) {
      buyPrice = price;
    }
  }

  return profit;
}

console.log(maxProfit([7, 1, 5, 3, 6, 4]));
console.log(maxProfit([7, 6, 4, 3, 1]));
