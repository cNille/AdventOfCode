const fs = require('fs')
const input = fs.readFileSync('./data.txt', 'utf-8')


const lines = input.trim().split('\n')

let bots = []
for(let i = 0; i < 300; i++){
  bots.push({low: 0, high:0 })
}

re1 = /bot (\d+) gives low to bot (\d+) and high to bot (\d+)/
re2 = /bot (\d+) gives low to output (\d+) and high to bot (\d+)/
re2 = /bot (\d+) gives low to bot (\d+) and high to output (\d+)/
re2 = /bot (\d+) gives low to output (\d+) and high to output (\d+)/
valReg = /value (\d+) goes to bot (\d+)/

console.log(bots)
lines.forEach(function(line){
  
  if(line.match(re1)){
    [l, id, low, high] = line.match(re1)
    bot = bots[id]
    bots[low].low = Math.min(bot[0], bot[1])
    bots[high].high = Math.max(bot[0], bot[1])
  }
  if(line.match(valReg)){
    [l, value, bot] = line.match(valReg)
    console.log(l, value, bot)
    bots[bot] = { low: Math.min(bots[bot].low, value), high: Math.max(bots[bot][1], value)}
    console.log(line, bots[bot])
  
  }
})

console.log(bots)
