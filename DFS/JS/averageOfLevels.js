/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var averageOfLevels = function (root) {
  const ans = []
  const stack = [root]
  while (stack.length) {
    let sum = 0
    let stackLength = stack.length
    for (let i = 0; i < stackLength; i++) {
      const node = stack.shift()
      sum += node.val
      if (node.left) stack.push(node.left)
      if (node.right) stack.push(node.right)
    }
    ans.push(sum / stackLength)
  }
  return ans
};