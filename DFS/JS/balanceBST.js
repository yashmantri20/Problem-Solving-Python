var balanceBST = function (root) {
  function traverse(root) {
    if (!root) return

    traverse(root.left)
    sortedArr.push(root.val)
    traverse(root.right)
  }

  function sortedArrayToBST(arr, start, end) {
    if (start > end) {
      return null;
    }
    var mid = parseInt((start + end) / 2);
    var node = new TreeNode(arr[mid]);
    node.left = sortedArrayToBST(arr, start, mid - 1);
    node.right = sortedArrayToBST(arr, mid + 1, end);
    return node;
  }

  const sortedArr = []
  traverse(root)
  return sortedArrayToBST(sortedArr, 0, sortedArr.length - 1)
};