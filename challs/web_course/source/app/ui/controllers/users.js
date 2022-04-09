const userModel = require("../../../models/users");
const jwt = require("jsonwebtoken");
const dotenv = require("dotenv");
dotenv.config();

userModel.create({
        name: 'admin',
        email: 'admin',
        password: process.env.ADMIN_PASSWORD + '',
    },
    function(err, result) {
        if (err) {
            console.log(err);
        } else {
            console.log(result);
        }
    }
);

module.exports = {
    create: function(req, res, next) {
        if (req.body.name && req.body.password && req.body.email) {
            if (req.body.name !== "admin") {
                userModel.create({
                        name: req.body.name,
                        email: req.body.email,
                        password: req.body.password
                    },
                    function(err, result) {
                        if (err) {
                            res.render("register", {
                                message: {
                                    error: 'Database Error!'
                                }
                            });
                        } else {
                            res.render("login", {
                                message: {
                                    success: "User created successfully!"
                                }
                            });
                        }
                    }
                );
            } else {
                res.render("login", {
                    message: {
                        error: "You can't use admin, sorry!"
                    }
                })
            }
        } else {
            res.render("register", {
                message: {
                    error: 'Check form data!'
                }
            });
        }
    },
    authenticate: function(req, res, next) {
        if (req.body.name && req.body.password) {
            userModel.findOne({
                    name: req.body.name,
                    password: req.body.password
                },
                function(err, userInfo) {
                    if (err) {
                        next(err);
                    } else {
                        if (userInfo === null) {
                            res.render('login', {
                                message: {
                                    error: 'Login/password incorrect!'
                                }
                            });
                        } else {
                            const token = jwt.sign({
                                    id: userInfo._id,
                                    name: userInfo.name
                                },
                                req.app.get("secret_key"), {
                                    expiresIn: "1h"
                                }
                            );
                            let options = {
                                maxAge: 1000 * 60 * 15,
                                httpOnly: true
                            };
                            res.cookie("token", token, options);
                            res.redirect("/");
                        }

                    }
                }
            );
        } else {
            res.render("login", {
                message: {
                    error: "Check your data!"
                }
            });
        }
    }
};