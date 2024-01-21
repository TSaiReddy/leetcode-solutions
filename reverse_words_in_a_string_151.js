function reverse(s) {
  const arr = s.split(" ");
  let reversedStr = "";
  for (let index = arr.length - 1; index >= 0; index--) {
    const element = arr[index];
    if (!(reversedStr[-1] === undefined && element === "")) {
      reversedStr = reversedStr + " " + element;
    }
  }
  return reversedStr.slice(1);
}

console.log(reverse("  the sky is    blue   "));
