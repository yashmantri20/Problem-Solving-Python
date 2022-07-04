var averageOfSubtree = function (root) {
  let count = 0;

  let queue = [root];
  if (!root) return 0;
  while (queue.length) {
    let node = queue.shift();
    if (isValid(node)) {
      count++;
    }
    if (node.left) {
      queue.push(node.left);
    }
    if (node.right) {
      queue.push(node.right);
    }
  }
  return count;
};

var isValid = function (node) {
  let sum = 0;
  let count = 0;

  let queue = [node];
  if (!node) return false;

  while (queue.length) {
    let node = queue.shift();
    sum += node.val;
    count++;
    if (node.left) {
      queue.push(node.left);
    }
    if (node.right) {
      queue.push(node.right);
    }
  }
  if (Math.floor(sum / count) === node.val) return true;
  return false;
}

// DFS

var averageOfSubtree = function (root) {
  let count = 0;

  function traverse(node) {
    if (!node) {
      return [0, 0];
    }

    let [sumLeft, countLeft] = traverse(node.left);
    let [sumRight, countRight] = traverse(node.right);

    if (Math.floor((sumLeft + sumRight + node.val) / (countLeft + countRight + 1)) === node.val) {
      count++;
    }

    return [sumLeft + sumRight + node.val, countLeft + countRight + 1];
  }

  traverse(root);

  return count;
};