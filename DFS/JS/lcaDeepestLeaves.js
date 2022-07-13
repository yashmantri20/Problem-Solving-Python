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
 * @return {TreeNode}
 */
var lcaDeepestLeaves = function (root) {
  const maxDepth = (root) => {
    if (!root) return 0
    let left = maxDepth(root.left)
    let right = maxDepth(root.right)
    return Math.max(left, right) + 1
  };

  const mDepth = maxDepth(root)
  function dfs(root, depth) {
    if (!root) return
    if (depth === mDepth) {
      return root
    }

    let left = dfs(root.left, depth + 1);
    let right = dfs(root.right, depth + 1);
    return left && right ? root : left || right;

  }
  return dfs(root, 1)

};