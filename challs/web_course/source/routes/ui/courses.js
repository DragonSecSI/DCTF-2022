const express = require('express');
const router = express.Router();

const courseController = require('../../app/ui/controllers/courses');

router.get('/', courseController.getAll);


module.exports = router;