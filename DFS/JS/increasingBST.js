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
var increasingBST = function (root) {
  let node = new TreeNode();
  let res = node
  function traverse(root) {
    if (!root) return

    if (root.left) traverse(root.left)
    node.right = new TreeNode(root.val);
    node = node.right
    if (root.right) traverse(root.right)
  }
  traverse(root)
  return res.right
};