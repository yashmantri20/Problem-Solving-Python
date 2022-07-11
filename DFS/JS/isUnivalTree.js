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
 * @return {boolean}
 */
var isUnivalTree = function (root) {
  const val = root.val
  function Dfs(root) {
    if (!root) return true

    if (root.val !== val) return false

    if (!Dfs(root.left)) return false
    if (!Dfs(root.right)) return false

    return true
  }
  return Dfs(root)
};