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
 * @return {number}
 */
var minDepth = function (root) {
  if (!root) return 0;
  let minDepth = Infinity;
  function dfsTraversal(root, depth) {
    if (!root) return;
    if (!root.left && !root.right) {
      minDepth = Math.min(minDepth, depth);
      return;
    }
    dfsTraversal(root.left, depth + 1);
    dfsTraversal(root.right, depth + 1);
  }
  dfsTraversal(root, 1);
  return minDepth;
};