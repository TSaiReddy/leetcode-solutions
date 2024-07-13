function isValid(s) {
  const stack = [];

  const opposites = {
    "{": "}",
    "[": "]",
    "(": ")",
  };

  for (const w of s) {
    if (w === "(" || w === "[" || w === "{") stack.push(opposites[w]);
    else {
      if (stack.at(-1) === w) stack.pop();
      else return false;
    }
  }
  if (stack.length > 0) return false;
  return true;
}

isValid("()[]{}");
