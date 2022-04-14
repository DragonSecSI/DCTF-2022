const express = require("express");
const morgan = require("morgan");
const path = require('path')
const helmet = require("helmet");
const routes = require('./routes')

const {PORT, HOST}= require("./config");


const app = express();

app.set('views', path.join(__dirname, '/views'));
app.set("view engine", "pug");

app.use(helmet());
app.use(morgan("combined"));
//app.use(express.json())
app.use(express.urlencoded( {extended: false} ));

app.use("/", routes)
app.use('/public', express.static(path.join(__dirname, "..",'public')))

app.use((req,res,next)=>{
    return res.status(404).render("error", {title:"Not Found"});
})

app.use((err,req,res,next)=>{
    console.log(err)
    return res.render("error")
})

app.listen(PORT, HOST, ()=>{
    console.log(`Running http://${HOST}:${PORT}`);
});