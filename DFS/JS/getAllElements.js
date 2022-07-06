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
 * @return {number[]}
 */
var getAllElements = function (root1, root2) {
  const arr1 = [];
  const arr2 = [];
  if (!root1 && !root2) return res;
  dfs(root1, arr1)
  dfs(root2, arr2)
  return merge(arr1, arr2)
};

// In Order DFS
function dfs(root, res) {
  if (!root) return
  if (root.left)
    dfs(root.left, res)

  res.push(root.val)

  if (root.right)
    dfs(root.right, res)
}

function merge(a, b) {
  const res = [];
  while (a.length && b.length) {
    if (a[0] < b[0])
      res.push(a.shift())
    else
      res.push(b.shift())
  }
  return res.concat(a, b)
}