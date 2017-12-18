const fs = require('fs')
const input = fs.readFileSync('my.input', 'utf-8')
const lines = input.split('\n')
let tree = {} 

// Parse all lines and create tree
lines.forEach( line => {
  [node, leaves] = line.split('->')
  if(!node){
    return;
  }
  let n = /(\w+)\s+\((\d+)\)/g.exec(node)
  name = n[1]
  weight = parseInt(n[2])
  leaves = leaves || ''

  tree[name] = {
    weight,
    leaves: leaves.split(',').map(x => x.trim()).filter( x => x.length)
  }
})

var found = false;

// Recursive function to get weight
function getWeight(name){
  const node = tree[name];
  if(!node || !node.leaves || !node.leaves.length){
    return node.weight
  } 
  const leaves = node.leaves.map(x => getWeight(x));
  const sumweight = leaves.reduce( (acc, curr) => acc + curr , 0 )

  if(!found && (new Set(leaves)).size !== 1){
    console.log('Found!')
    console.log('Weight:', node.weight)
    console.log('Leaves:',leaves)
    console.log('node.leavel:',node.leaves)
    console.log('sumweight:',sumweight)
    found = true;
  }
  return node.weight + sumweight 
}

getWeight('mkxke');
