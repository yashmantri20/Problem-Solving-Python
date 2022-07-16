/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function (nums) {
  function helper(arr, start, end) {
    if (start > end) {
      return null;
    }
    var mid = parseInt((start + end) / 2);
    var node = new TreeNode(arr[mid]);
    node.left = helper(arr, start, mid - 1);
    node.right = helper(arr, mid + 1, end);
    return node;
  }

  return helper(nums, 0, nums.length - 1)
};