const { NODE_ENV = "production" } = process.env;
module.exports["NODE_ENV"] = NODE_ENV;
if (NODE_ENV === "development") {
  require("dotenv").config();
}

const vars = ["DBURI",
"PORT",
"HOST",
"HASHING_SECRET"];

vars.forEach((v) => {
  const pv = "SQLTUT_" + v;
  if (!(pv in process.env)) {
    throw Error(`Variable ${pv} not specified!`);
  }
  module.exports[v] = process.env[pv];
});

