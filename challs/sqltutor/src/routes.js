const express = require("express");
const router = express.Router();
const {
  hashPayload,
  sanitizeSQLtext,
  getConnection,
  failInternal,
  ALL_QUERIES,
  formatString,
} = require("./util");

router.get("/", (req, res) => {
  // Render webpage
  console.log("Router");
  res.render("index", {
    queries: ALL_QUERIES.map((v) => formatString(v.query, "...")),
  });
});

router.post("/verify_and_sign_text", (req, res) => {
  console.log(req.body);
  //Check body has md5 specified
  //prepend secret and hash
  const steps = [];
  const { alg, text = "", debug = false } = req.body;
  if (alg !== "sha256")
    return res.json({
      status: "error",
      message: "Invalid signature generation algorithm!",
      debug: debug ? { input: { alg, text }, steps } : null,
    });
  steps.push("Selected sha256 algorithm ✅");
  let textAscii;
  try {
    const textBuff = Buffer.from(text, "base64");
    textAscii = textBuff.toString("ascii");
  } catch (e) {
    console.error(e);
    return res.json({
      status: "error",
      message: "Invalid text form paramter - not in base64",
      debug: debug ? { input: { alg, text }, steps } : null,
    });
  }
  steps.push("Decoded text from base64 ✅");
  const [msg, sanitized] = sanitizeSQLtext(textAscii);
  if (msg) {
    return res.json({
      status: "error",
      message: msg + " text!",
      debug: debug ? { input: { alg, text }, steps } : null,
    });
  }
  steps.push("Trimmed and checked the text ✅");
  const retText = Buffer.from(sanitized).toString("base64");
  // strip in client
  // Make it one-time ?
  const signature = hashPayload(sanitized);
  steps.push("Created signature: prepended secret and sha256 ✅");
  return res.json({
    status: "ok",
    trimmedText: retText,
    signature,
    debug: debug ? { input: { alg, text }, steps } : null,
  });
});

router.post("/execute", (req, res) => {
  console.log(req.body);
  const steps = [];
  // Execute sql if sha1 matches
  const { text = "", signature = "", debug = false, queryNo = "1" } = req.body;
  if (!text)
    return res.json({
      status: "error",
      message: "Missing text form paramter",
      debug: debug ? { input: { signature, text }, steps } : null,
    });
  if (!signature)
    return res.json({
      status: "error",
      message: "Missing signature form paramter",
      debug: debug ? { input: { signature, text }, steps } : null,
    });

  let textAscii;
  try {
    const textBuff = Buffer.from(text, "base64");
    textAscii = textBuff.toString("ascii");
  } catch (e) {
    console.error(e);
    return res.json({
      status: "error",
      message: "Invalid text form paramter - not in base64",
      debug: debug ? { input: { signature, text }, steps } : null,
    });
  }
  steps.push("Decoded text from base64 ✅");
  let selectedQuery = ALL_QUERIES[0];
  //parse integer from queryNo
  let queryNoInt = parseInt(queryNo);
  if (!Number.isInteger(queryNoInt)) {
    steps.push("Invalid queryNo - not an integer. Fallback to query #1 ⚠");
  } else {
    queryNoInt = Math.max(0, Math.min(queryNoInt, ALL_QUERIES.length - 1));
    selectedQuery = ALL_QUERIES[queryNoInt];
    steps.push(`Selected query #${queryNoInt} ✅`);
  }

  const hashed = hashPayload(textAscii);
  if (hashed !== signature)
    return res.json({
      status: "error",
      message: "Invalid text signature, this incident will be reported!",
      debug: debug ? { input: { signature, text }, steps } : null,
    });

  steps.push("Confirmed text and signature match ✅");
  // Make sure sql injection is possible
  const connection = getConnection();
  const description = formatString(selectedQuery.description || "", [
    textAscii,
  ]);
  const sqlQuery = formatString(selectedQuery.query, [textAscii]);
  connection.execute(sqlQuery, (err, results) => {
    if (err) {
      console.error(err);
      return failInternal(res);
    }
    steps.push("Executed query ✅");
    return res.json({
      status: "ok",
      query: sqlQuery,
      results,
      description: description || "",
      debug: debug ? { input: { signature, text }, steps } : null,
    });
  });
});

module.exports = router;
