/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function (n) {
  //  let count = 0;

  // 	while (n !== 0) {
  // 		count++;
  // 		n = n & (n - 1);
  // 	}

  // 	return count;
  n = n.toString(2)
  let counter = 0
  for (let i = 0; i < n.length; i++) {
    if (n[i] == 1) {
      counter++
    }
  }
  return counter
};