/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function (grid) {
  let height = grid.length
  let width = grid[0].length;

  let perimeter = 0

  for (let row = 0; row < height; row++) {
    for (let col = 0; col < width; col++) {
      if (grid[row][col] == 1) {
        perimeter += 4

        if (row > 0 && grid[row - 1][col] == 1) perimeter--
        if (row < height - 1 && grid[row + 1][col] == 1) perimeter--
        if (grid[row][col - 1] == 1) perimeter--
        if (grid[row][col + 1] == 1) perimeter--
      }
    }
  }
  return perimeter;
};