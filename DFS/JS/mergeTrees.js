/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {TreeNode}
 */
var mergeTrees = function (root1, root2) {
  function traverse(root1, root2) {
    if (!root1 || !root2) return root1 || root2

    const root = new TreeNode(root1.val + root2.val);
    const left = traverse(root1.left, root2.left)
    const right = traverse(root1.right, root2.right)
    root.left = left
    root.right = right
    return root

  }
  return traverse(root1, root2)
};