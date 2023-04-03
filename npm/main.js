const { getRxStoragePouch } = require("rxdb");

const database = await createRxDatabase({
    name: 'cilvekudb',
    storage: getRxStoragePouch('idb'),
    password: 'admin',
    multiInstance: true,
    eventReduce: true
})