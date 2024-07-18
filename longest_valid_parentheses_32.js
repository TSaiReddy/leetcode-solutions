/**
 * @param {string} s
 * @return {number}
 */

function longestValidParentheses(s) {
  const stack = [-1];
  let maxLength = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      stack.push(i);
    } else {
      stack.pop();
      if (stack.length === 0) {
        stack.push(i);
      } else {
        maxLength = Math.max(maxLength, i - stack.at(-1));
      }
    }
  }
  return maxLength;
}

longestValidParentheses("(()");
longestValidParentheses(")()())");
longestValidParentheses("()(()");
