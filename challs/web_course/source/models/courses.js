const mongoose = require('mongoose');

// Schema definition

const Schema = mongoose.Schema;

const CourseSchema = new Schema({
    name: {
        type: String,
        trim: true,
        required: true,
    },
    cost: {
        type: Number,
        default: 10,
        required: true,
    },
    content: {
        type: String,
        default: "",
        trim: true,
        required: true,
    },
    owner: {
        type: String,
        trim: true,
        required: true,
    }

});

module.exports = mongoose.model('Course', CourseSchema);