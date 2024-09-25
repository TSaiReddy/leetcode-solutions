function isIsomorphic(s, t) {
  if (s.length !== t.length) return false;
  const hash = {};

  for (let i = 0; i < s.length; i++) {
    const key = s[i];
    const value = t[i];
    if (!(key in hash)) {
      if (Object.values(hash).includes(value)) return false;
      hash[key] = value;
    } else {
      if (hash[key] !== value) return false;
    }
  }

  return true;
}

console.log(isIsomorphic("egg", "add"));
console.log(isIsomorphic("foo", "bar"));
