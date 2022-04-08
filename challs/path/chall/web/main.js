const express = require("express");
const path = require("path");

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

app.get('/*', function(req, res) {
    const t = decodeURIComponent(req.originalUrl)
    return res.sendFile(path.join(__dirname, t))
});

app.listen(port, () => {
    console.log(`Example app listening at ${port}`);
});
