const a = '0 1 2 3 4 5'.split(' ');
const b = [
  [0, 1],
  [0, 2],
  [1, 3],
  [1, 4],
  [2, 5]
]

const list = new Map();

const addNode = (s) => {
  list.set(s, [])
}

const addEdge = (o, d) => {
  list.get(o).push(d);
  list.get(d).push(o);
}

a.forEach(s => addNode(Number(s)));
b.forEach(r => addEdge(r[0], r[1]));

/* for(let c of list) {
console.log(c)
}
 */

const BFS = (start) => {
  const queue = [start];
  const visited = new Set();

  while (queue.length > 0) {
    const temp = queue.shift();
    const data = list.get(temp);
    for (const t of data) {
      if (!visited.has(t)) {
        queue.push(t);
        visited.add(t)
      }
    }
  }
}

const DFS = (start, visited) => {
  visited.add(start)
  const data = list.get(start);
  for (const t of data) {
    if (!visited.has(t)) {
      DFS(t, visited)
    }
  }
}
const visited = new Set();
DFS(0, visited)

/* BFS(0) */
