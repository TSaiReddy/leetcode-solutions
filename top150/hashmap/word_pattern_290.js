function wordPattern(pattern, s) {
  const arr = s.split(" ");
  if (pattern.length !== arr.length) return false;

  const hash = {};

  for (let i = 0; i < pattern.length; i++) {
    const key = pattern[i];
    const value = arr[i];
    if (!(key in hash)) {
      if (!Object.values(hash).includes(value)) hash[key] = value;
      else return false;
    } else {
      if (hash[key] !== value) return false;
    }
  }

  return true;
}

console.log(wordPattern("abba", "dog cat cat dog"));
