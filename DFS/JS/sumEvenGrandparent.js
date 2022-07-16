var sumEvenGrandparent = function (root) {
  let sum = 0;
  getSumByDFS(root);
  return sum;

  function getSumByDFS(node, parent = null, grandparent = null) {
    if (!node) {
      return;
    }
    if (grandparent && grandparent.val % 2 === 0) {
      sum += node.val;
    }
    getSumByDFS(node.left, node, parent);
    getSumByDFS(node.right, node, parent);
  }
};
