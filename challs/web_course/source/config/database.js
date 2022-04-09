const mongoose = require("mongoose");
const dotenv = require("dotenv");
dotenv.config();

const dbUri = process.env.DB_URI || 'mongodb://localhost:27017/chall'

mongoose.connect(dbUri);

mongoose.connection.on('connected', function() {
    console.log('Mongoose default connection open to ' + dbUri);
});

mongoose.Promise = global.Promise;

module.exports = mongoose;