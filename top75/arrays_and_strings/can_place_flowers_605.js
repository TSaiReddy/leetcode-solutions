function canPlaceFlowers(flowerbed, n) {
  for (let i = 0; i < flowerbed.length; i++) {
    if (flowerbed[i] === 0) {
      const left = i === 0 || flowerbed[i - 1] === 0;
      const right = i === flowerbed - 1 || flowerbed[i + 1] === 0;
      if (left && right) {
        flowerbed[i] = 1;
        n--;
      }
    }
  }

  return n === 0;
}

console.log(canPlaceFlowers([1, 0, 0, 0, 1], 1));
