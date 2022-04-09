const courseModel = require('../../../models/courses');

module.exports = {
    getById: function (req, res, next) {
        console.log(req.body);
        courseModel.findById(req.params.courseId, function (err, courseInfo) {
            if (err) {
                next(err);
            } else {
                if (courseInfo.owner === 'admin') {
                    if (req.body.name === 'admin') {
                        res.json({
                            status: "success",
                            message: "Course Found!",
                            data: {
                                course: courseInfo
                            }
                        });
                    } else {
                        res.json({
                            status: "error",
                            message: "Can not view this source",
                            data: null,
                        });
                    }

                } else {
                    res.json({
                        status: "success",
                        message: "Course Found!",
                        data: {
                            course: courseInfo
                        }
                    });
                }
            }
        })
    },
    getAll: function (req, res, next) {
        console.log(req.body);
        let courseList = [];
        courseModel.find({}, function (err, courses) {
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
                res.json({
                    status: "success",
                    message: "Courses list found!",
                    data: {
                        courses: courseList
                    }
                });
            }
        })
    }
}