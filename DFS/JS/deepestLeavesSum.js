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
var deepestLeavesSum = function (root) {
    function findDepth(node) {
        if (!node) return 0;
        return Math.max(findDepth(node.left), findDepth(node.right)) + 1;
    }

    const depth = findDepth(root);

    function callDFS(node, height) {
        if (!node) return 0;
        if (height === 1) return node.val;
        return callDFS(node.left, height - 1) + callDFS(node.right, height - 1);
    }
    return callDFS(root, depth);
};


var deepestLeavesSum = function (root) {
    let stack = [root];
    let lastLevelSum = 0;
    while (stack.length != 0) {
        let len = stack.length;
        lastLevelSum = 0;
        for (let i = 0; i < len; i++) {
            let node = stack.shift();
            lastLevelSum += node.val;
            if (node.left) {
                stack.push(node.left)
            }
            if (node.right) {
                stack.push(node.right)
            }
        }


    }
    return lastLevelSum;
};