/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[][]} descriptions
 * @return {TreeNode}
 */
var createBinaryTree = function (descriptions) {
  const set = new Set()
  const treeStruct = {}  // {parent: {1: childLeft, 0: childRight}}

  for (let [parent, child, isLeft] of descriptions) {
    set.add(child)
    if (!treeStruct[parent]) treeStruct[parent] = {}
    treeStruct[parent][isLeft] = child
  }

  let rootval
  for (let d of descriptions) {
    if (!set.has(d[0])) {
      rootval = d[0]
      break
    }
  }

  function dfs(val) {
    let root = new TreeNode(val)
    root.left = treeStruct[val] && treeStruct[val][1] ? dfs(treeStruct[val][1]) : null
    root.right = treeStruct[val] && treeStruct[val][0] ? dfs(treeStruct[val][0]) : null
    return root
  }

  return dfs(rootval)
};