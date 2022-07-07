/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function (rooms) {
  function traverse(temp, visited) {
    for (let room of temp) {
      if (!visited.has(room)) {
        visited.add(room)
        traverse(rooms[room], visited)
      }
    }
  }
  const zeroRoom = rooms[0]
  const visited = new Set()
  visited.add(0)
  traverse(zeroRoom, visited)
  return visited.size === rooms.length
};