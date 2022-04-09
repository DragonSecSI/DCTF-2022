const express = require("express");
const router = express.Router();
const userController = require("../../app/ui/controllers/users");

router.post("/register", userController.create);
router.post("/login", userController.authenticate);
router.get("/login", function (req, res) {
  res.render("login", {
    message: undefined
  });
});

router.get('/register', (req, res) => {
  res.render('register', {
    message: undefined
  });
});

module.exports = router;