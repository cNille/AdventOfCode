const fs = require('fs')
const input = fs.readFileSync('my.input', 'utf-8')
let lines = input.split('\n')
const re = /p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>/

lines = lines.filter(l => l)
let particles = lines.map( l => {
  return re.exec(l).slice(1,10).map(x => parseInt(x))
})

function collisiondetector(list){
  groupedByPos = list.reduce((acc, curr) => {
    pos = curr.slice(0,3).join(',')
    if(!(pos in acc)){
      acc[pos] = []
    }
    acc[pos].push(curr)
    return acc
  }, {}) 
  return Object.keys(groupedByPos)
    .map(key => groupedByPos[key])
    .filter(value => value.length < 2)
    .map( v => v[0])
}

function positionIncrement(list){
  return list.map(l => {
    const [px,py,pz,vx,vy,vz,ax,ay,az] = l
    return [
      px + vx + ax,
      py + vy + ay,
      px + vx + ax,
      vx + ax,
      vy + ay,
      vx + ax,
      ax,
      ay,
      ax,
    ]
  })
}

for(let i = 0; i < 100; i++){
  particles = collisiondetector(particles)
  particles = positionIncrement(particles)
  console.log(i, particles.length)
}
