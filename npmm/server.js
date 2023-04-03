const app = require('express')()
const http = require('http').createServer(app)
const io = require('socket.io')(http)

io.on('connection', (socket) => {
  console.log('a user connected')
  setInterval(() => {
    io.emit('msg', { data: [1, 2, 3] })
  }, 5000)
  socket.on('msg_from_client' , (msg) => {
    console.log(msg)
  })
})

http.listen(3000, () => {
  console.log('listening on *:3000')
})
