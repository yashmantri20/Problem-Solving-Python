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
var goodNodes = function (root) {
  let count = 0;
  dfs(root, []);
  return count;
  function dfs(root, path) {
    if (!root) {
      return;
    }
    if (root.val >= Math.max(...path)) {
      count++;
    }
    dfs(root.left, [...path, root.val]);
    dfs(root.right, [...path, root.val]);
  }
};

var goodNodes = function (root) {
  let count = 0;
  dfs(root, root.val);
  return count;
  function dfs(root, max) {
    if (!root) return;
    if (root.val >= max) ++count;
    max = Math.max(max, root.val);
    dfs(root.left, max);
    dfs(root.right, max);
  }
};