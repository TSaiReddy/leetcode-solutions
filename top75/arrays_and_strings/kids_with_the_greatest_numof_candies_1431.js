function kidsWithCandies(candies, extraCandies) {
  const max = Math.max(...candies);

  for (let i = 0; i < candies.length; i++)
    candies[i] = candies[i] + extraCandies < max ? false : true;

  return candies;
}

console.log(kidsWithCandies([2, 3, 5, 1, 3], 3));
