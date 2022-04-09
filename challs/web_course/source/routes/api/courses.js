const express = require('express');
const router = express.Router();

const courseController = require('../../app/api/controllers/courses');

router.get('/', courseController.getAll);
router.get('/:courseId', courseController.getById);



module.exports = router;