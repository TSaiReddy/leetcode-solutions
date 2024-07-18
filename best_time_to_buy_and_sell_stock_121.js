/**
 * @param {number[]} prices
 * @return {number}
 */

function maxProfit(prices) {
  let buyPrice = prices[0];
  let profit = 0;

  for (const price of prices) {
    const curProfit = price - buyPrice;

    if (buyPrice > price) {
      buyPrice = price;
    } else if (curProfit > profit) {
      profit = curProfit;
    }
  }
  return profit;
}

console.log(maxProfit([2, 4, 1])); // 2 - 4 = 2
console.log(maxProfit([4, 7, 1, 2])); // 4 - 7 = 3
// console.log(maxProfit([7, 1, 5, 3, 6, 4])); // 1 - 6 = 5
