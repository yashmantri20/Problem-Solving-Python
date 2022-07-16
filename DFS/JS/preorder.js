var preorder = function (root) {
  const res = [];
  traverse(root);
  return res;

  function traverse(node) {
    if (!node) return;
    res.push(node.val);
    for (child of node.children) {
      traverse(child);
    }
  }
};