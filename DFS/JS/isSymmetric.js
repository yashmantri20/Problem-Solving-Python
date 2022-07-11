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
var isSymmetric = function (root) {
  function isEqual(root1, root2) {
    if (!root1 && !root2) return true;
    if (!root1 || !root2) return false;
    return root1.val === root2.val
      && isEqual(root1.left, root2.right)
      && isEqual(root1.right, root2.left);
  }
  if (!root) return true;
  return isEqual(root.left, root.right)
};