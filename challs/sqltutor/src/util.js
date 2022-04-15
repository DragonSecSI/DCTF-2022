const crypto = require("crypto");
const { HASHING_SECRET, DBURI } = require("./config");
const mysql2 = require("mysql2");

console.log("HASHING SECRET:", HASHING_SECRET);

/// DATABASE SECTION ///

function getConnection() {
  return mysql2.createConnection(DBURI);
}

const ALL_QUERIES = [
  {
    query: "SELECT * FROM users WHERE users.name='{0}'",
    description: "This query selects all users with the name '{0}'.",
  },
  {
    query:
      "SELECT u.*, COUNT(c.id) as `rich meter` FROM users u JOIN cars c ON c.ownerID=u.id WHERE u.name='{0}' GROUP BY u.id",
    description:
      "This query selects all users with the name '{0}' and the number of cars they own.",
  },
  {
    query: "SELECT * FROM users WHERE users.name !='{0}'",
    description: "This query selects all users that don't have name '{0}'.",
  },
  {
    query: "SELECT * FROM cars WHERE cars.make='{0}'",
    description: "This query selects all cars made by '{0}'.",
  },
  {
    query: "SELECT * FROM users WHERE users.name LIKE '%{0}%'",
    description: "This query selects all users with name containing '{0}'.",
  },
  {
    query: "SELECT * FROM users WHERE users.name LIKE BINARY '%{0}%'",
    description:
      "This query selects all users with name containing '{0}', case sensitive.",
  },
  {
    query: "SELECT * FROM users WHERE users.name LIKE BINARY '%{0}'",
    description:
      "This query selects all users with name ending in '{0}', case sensitive.",
  },
  {
    query:
      "SELECT cars.* FROM cars JOIN users ON cars.ownerID=users.id WHERE users.name='{0}'",
    description: "This query selects all cars owned by '{0}'.",
  },
  {
    query: "SELECT name AS `{0}` FROM users WHERE users.id < 10",
    description:
      "This query selects all users with id less than 10, and rename the result column to '{0}'.",
  },
];

/// CRYPTO SECTION ///
function sanitizeSQLtext(query) {
  const re =
    /(drop|alter|delete|remove|show|select|union|on|[='"+:;,#*`%<>]|where|0x|database|sql|null|true|false)/gi;
  let trimmed = query.replace(/\s+/gi, " ").trim();
  const m = trimmed.match(re);
  const s = Array.from(new Set(m)).join(" ").toUpperCase();
  if (m) return [`Dangerous strings:[ ${s} ] in`, ""];
  if (trimmed == "") return ["Empty", ""];
  return [null, trimmed];
}

function hashPayload(payload) {
  const b = Buffer.concat([Buffer.from(HASHING_SECRET, "ascii"), payload]);
  return crypto.createHash("sha1").update(b).digest("hex");
}

/// UTIL SECTION ///

function failInternal(res) {
  return res.status(500).json({
    status: "error",
    message: "Internal server error, contact challenge owner",
  });
}

function formatString(string, ...args) {
  // store arguments in an array
  // use replace to iterate over the string
  // select the match and check if related argument is present
  // if yes, replace the match with the argument
  return string.replace(/{([0-9]+)}/g, function (match, index) {
    // check if the argument is present
    return typeof args[index] == "undefined" ? match : args[index];
  });
}

module.exports = {
  hashPayload,
  sanitizeSQLtext,
  failInternal,
  getConnection,
  ALL_QUERIES,
  formatString,
};
