const courseModel = require('../../../models/courses');

const dotenv = require("dotenv");
dotenv.config();

course = {
    name: 'Locked course',
    cost: 10,
    content: process.env.FLAG + '',
    owner: 'admin',

}
course2 = {
    name: 'Mongo DB course',
    cost: 1,
    content: 'MongoDB is a source-available cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas. MongoDB is developed by MongoDB Inc. and licensed under the Server Side Public License (SSPL).',
    owner: 'lavbic',

}
course3 = {
    name: 'JSON course',
    cost: 2,
    content: 'JSON (JavaScript Object Notation, pronounced /ˈdʒeɪsən/; also /ˈdʒeɪˌsɒn/) is an open standard file format and data interchange format that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and arrays (or other serializable values). It is a common data format with diverse uses in electronic data interchange, including that of web applications with servers.',
    owner: 'lara',

}

courseModel.create(course, function(err, course) {
    if (err) {
        console.log(err);
    } else {
        console.log(course);
    }


})
courseModel.create(course2, function(err, course) {
    if (err) {
        console.log(err);
    } else {
        console.log(course);
    }

})

courseModel.create(course3, function(err, course) {
    if (err) {
        console.log(err);
    } else {
        console.log(course);
    }
})


module.exports = {
    getAll: function(req, res, next) {
        let courseList = []
        courseModel.find({}, function(err, courses) {
            if (err) {
                next(err);
            } else {
                for (let course of courses) {
                    if (course.owner !== 'admin') {
                        courseList.push({
                            id: course._id,
                            name: course.name,
                            cost: course.cost,
                            content: course.content,
                            owner: course.owner,
                        });
                    } else {
                        if (req.body.name !== 'admin') {
                            courseList.push({
                                id: course._id,
                                name: course.name,
                                cost: course.cost,
                                content: 'You must be admin to see the content of this course!',
                                owner: course.owner,
                            });
                        } else {
                            courseList.push({
                                id: course._id,
                                name: course.name,
                                cost: course.cost,
                                content: course.content,
                                owner: course.owner,
                            });
                        }

                    }

                }
                res.render('courses', {
                    courses: courseList,
                    user: {
                        name: req.body.name
                    }
                });
            }
        });
    }
}