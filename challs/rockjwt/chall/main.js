const express = require("express");
const jose = require('jose')
const fs = require('fs')
const super_special_stuff = process.env.SECRET

const app = express();
var port = "3000";
if(process.env.NODE_ENV === "production") {
    port = "8000"
}

app.use(express.json());
app.use(express.urlencoded({ extended: false }));


app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header(
        'Access-Control-Allow-Headers',
        'Origin, X-Requested-With, Content-Type, Accept, Authorization'
    );
    res.header('Access-Control-Allow-Methods', 'GET');
    res.charset = 'utf-8';
    next();
});

app.get("/", function (req, res) {
    (async () => {
        const guestJwt = await new jose.SignJWT({ "username": "guest", "auth_level": "guest" })
            .setProtectedHeader({typ: "JWT", alg: 'HS256'})
            .sign(Buffer.from(super_special_stuff, 'utf8'))
        return res.status(200).json(guestJwt)
    })();
})

app.get("/secret", function (req, res) {
    if(req.header('authorization')) {
        const tok = req.header('authorization').split(" ")[1];
        (async () => {
            try {
                const {payload, protectedHeader} = await jose.jwtVerify(tok, Buffer.from(super_special_stuff, 'utf8'))
                if (payload != null) {
                    if (payload.auth_level === "admin") {
                        try {
                            const data = fs.readFileSync('flag.txt', 'utf8')
                            return res.status(200).json(data.trim())
                        } catch (err) {
                            return res.status(500).json("Something went wrong.")
                        }
                    } else {
                        return res.status(400).json("Your auth_level is too low to access this resource.")
                    }
                } else {
                    return res.status(400).json("Your auth_level is too low to access this resource.")
                }
            } catch (e) {
                return res.status(400).json("Something went wrong")
            }
        })();
    }
    else {
        return res.status(400).json("No authorization token provided")
    }
})

app.listen(port, () => {
    console.log(`Example app listening at ${port}`);
});
