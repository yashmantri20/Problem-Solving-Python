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
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var rangeSumBST = function (root, low, high) {

  // BFS

  // const stack = [root]
  // let sum = 0
  // while(stack.length) {
  //     const node = stack.shift()
  //     if (low <= node.val && node.val <= high) {
  //         sum += node.val
  //     }
  //     if(node.left) {
  //         stack.push(node.left)
  //     } 
  //     if(node.right) {
  //         stack.push(node.right)
  //     }   
  // }
  // return sum

  // DFS
  let sum = 0
  function DFS(root) {
    if (!root) return 0;
    if (low <= root.val && root.val <= high) {
      sum += root.val
    }
    DFS(root.left)
    DFS(root.right)
  }
  DFS(root)
  return sum
};
