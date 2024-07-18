/**
 * @param {number} n
 * @return {string[]}
 */

function generateParenthesis(n) {
  const stack = [];
  const result = [];
  function backtrace(open, close) {
    if (open === close && close === n) {
      result.push(stack.join(""));
      return;
    }
    if (open < n) {
      stack.push("(");
      backtrace(open + 1, close);
      stack.pop();
    }
    if (open > close) {
      stack.push(")");
      backtrace(open, close + 1);
      stack.pop();
    }
  }
  backtrace(0, 0);
  return result;
}

console.log(generateParenthesis(3));
