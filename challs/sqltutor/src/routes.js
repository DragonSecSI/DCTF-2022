const express = require("express");
const router = express.Router();

const { HASHING_SECRET } = require("./config");

router.get("/", (req, res) => {
  // Render webpage
  console.log("Router");
  res.render("index");
});

router.post("/verify_signature", (req, res) => {
  console.log(req.body);
  //Check body has md5 specified
  //prepend secret and hash
  const { alg, payload="" } = req.body;
  if (alg !== "md5")
    return res.status(400).json({
      status: "error",
      message: "Invalid signature generation algorithm!",
    });
  const re =
    /(drop|alter|delete|remove|show|select|union|on|[='"+:;,#*%<>]|join|where|0x)/gi;
  const wspace = /\s+/gi;
  let newpayload = payload.replace(wspace, " ").trim();
  console.log(newpayload);
  const m = newpayload.match(re);
  if (newpayload==="" || m) {
    return res.status(400).json({
      status: "error",
      message: "Dangerous or invalid sql query!",
    });
  }
  // strip in client
  // Make it one-time ?
  return res.json({
    status: "ok",
    payload:newpayload,
    signature: "adfebf18a6b7f8e998c7e",
  });
});

router.post("/execute", (req, res) => {
  console.log(req.body);
  // Execute sql if md5 matches
  return res.json({
    result: [],
  });
});

module.exports = router;
