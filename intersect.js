/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function (nums1, nums2) {
  const ans = []
  const temp = {}
  for (let val of nums2) {
    if (val in temp) temp[val] += 1
    else temp[val] = 1
  }

  for (let val of nums1) {
    if (temp[val]) {
      ans.push(val)
      temp[val] -= 1
    }
  }

  return ans
};