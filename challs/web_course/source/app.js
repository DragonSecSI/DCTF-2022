const express = require("express");
const logger = require("morgan");
const path = require("path");
const usersAPI = require("./routes/api/users");
const usersUI = require("./routes/ui/users");
const coursesUI = require("./routes/ui/courses");
const coursesAPI = require("./routes/api/courses");
const bodyParser = require("body-parser");
const mongoose = require("./config/database");
const cookieParser = require("cookie-parser");
var jwt = require("jsonwebtoken");
const dotenv = require("dotenv");
dotenv.config();

port = process.env.PORT || 80;
const app = express();
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "pug");

app.use(cookieParser());

app.use(express.static(path.join(__dirname, "assets")));

app.set("secret_key", process.env.SECRET_KEY + "");

mongoose.connection.on(
    "error",
    console.error.bind(console, "Mongodb connection error: ")
);

app.use(logger("dev"));

app.use(
    bodyParser.urlencoded({
        extended: false
    })
);
app.use(bodyParser.json());

app.get("/", function(req, res) {
    jwt.verify(req.cookies.token, req.app.get("secret_key"), function(
        err,
        decoded
    ) {
        if (err) {
            res.render("index");
        } else {
            res.render("index", {
                user: {
                    name: decoded.name
                }
            });
        }
    });
});

app.use("/api/users", usersAPI);
app.use("/api/courses", validateApiUser, coursesAPI);

app.use("/users", usersUI);
app.use("/courses", validateUIUser, coursesUI);

app.get("/favicon.ico", function(req, res) {
    res.sendStatus(204);
});

function validateUIUser(req, res, next) {
    jwt.verify(req.cookies.token, req.app.get("secret_key"), function(
        err,
        decoded
    ) {
        if (err) {
            res.render("login", {
                message: {
                    error: "you must login to see courses!"
                }
            });
        } else {
            req.body.name = decoded.name;
            next();
        }
    });
}

function validateApiUser(req, res, next) {
    jwt.verify(req.headers["x-access-token"], req.app.get("secret_key"), function(
        err,
        decoded
    ) {
        if (err) {
            res.json({
                status: "error",
                message: "x-access-token header is missing from request",
                data: null
            });
        } else {
            req.body.name = decoded.name;
            next();
        }
    });
}

app.use(function(req, res, next) {
    let err = new Error("Not Found");
    err.status = 404;
    next(err);
});

app.use(function(err, req, res, next) {
    console.log(err);

    if (err.status === 404)
        res.status(404).json({
            message: "Not found"
        });
    else
        res.status(500).json({
            message: "Something looks wrong :( !!!"
        });
});

app.listen(port, function() {
    console.log(`Server listening on port ${port}`);
});