function getSum(a, b) {
  while (b != 0) {
    temp = (a & b) << 1;
    a = a ^ b;
    b = temp;
  }
  return a;
}

getSum(2, 3);
