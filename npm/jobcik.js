// cmd i think (mape ir nosaukta 'RxBD-WebSockets-Express')

mkdir RxBD-Websockets-Express/
cd RxBD-Websockets-Express
npm init -y
npm i socket.io express





// server.js

const app = require('express')();
const http = require('http').createServer(app);
const io = require('socket.io')(http);

io.on('connection', (socket) = {
    console.log('a user connected');
    setInterval(() = io.emit('data', {mag: 'hello websockt'}), 3000);
b;
http.listen(3000, () = {
console.log('listening on *:3000');
});



// iekš html

<script src="socket.io.js"></script>
<script>
    const socket = io('http://localhost:3000/");
    socket.on('data', msg = console.log(msg));
</script>;


//vs code cmd

// npm i leveldown pouchdb-adapter-leveldb rxdb rxjs colors shortid



// createCon.js

const { createRxDatabase, addRxPlugin } = require('rxdb');
const leveldown = require('leveldown')
addRxPlugin(require('pouchdb-adapter-leveldb'))
require('colors')

const initDB = async () => {
    try{
        const db = createRxDatabase({
            name: 'tutorial',
            adapter: leveldown,

        }).then((db) => {
            console.log('Created the tutorial RxDB'.green)
            return db            
        })

        db.dump() .then(console.log)
        return db
     }  catch (error) {
        console.error(error)
    }
}


module.exports = {initDB:initDB}


// main.js

const {initDB} = require('./db_stuff')
require('colors')

const initApp =  async () => {
    const db = await initDB()
}

initApp


// index.js


module.exports = {
    ...require('./createCon'),
}



// es ceru ka datubāze

import { createRxDatabase } from 'rxdb';

import { getRxStoragePouch, addPouchPlugin } from 'rxdb/plugins/pouchdb';
addPouchPlugin(require('pouchdb-adapter-idb'));


const dbPouch = await createRxDatabase({
    name: 'mydatabase',
    storage: getRxStoragePouch('idb')
  });                                           //ja izmanto pouchdb

const db = await createRxDatabase({
    name: 'heroesdb',                   // <- name
    storage: getRxStoragePouch('idb'),  // <- RxStorage
    password: 'myPassword',             // <- password (optional)
    multiInstance: true,                // <- multiInstance (optional, default: true)
    eventReduce: true                   // <- eventReduce (optional, default: true)
});

