const crypto = require("crypto");
const aesCmac = require("node-aes-cmac").aesCmac;

function calculateCmac(data, key, iv) {
    return aesCmac(key, data, {iv: iv, returnAsBuffer:true})
}

const zeros = Buffer.from("00000000000000000000000000000000", "hex")

let masterDecipher = crypto.createDecipheriv("aes-128-cbc", zeros, zeros);
masterDecipher.setAutoPadding(false);
let RndB = masterDecipher.update(Buffer.from("A71845BE528A7E8E08163D063D9542AA", "hex"));
let RndA = masterDecipher.update(Buffer.from("2C2ABDA6A1F9DFF50B87376C30575BC3", "hex"));
console.log('RndA:', RndA);
console.log('RndB:', RndB);

let key = Buffer.alloc(16);
RndA.copy(key, 0, 0, 4);
RndB.copy(key, 4, 0, 4);
RndA.copy(key, 8, 12, 16);
RndB.copy(key, 12, 12, 16);
console.log('Key: ', key);

let cmac1 = calculateCmac(Buffer.from("F501", "hex"), key)
let cmac2 = calculateCmac(Buffer.from("0003000019000000", "hex"), key, cmac1)
let cmac3 = calculateCmac(Buffer.from("BD01000000000000", "hex"), key, cmac2)

let decipher = crypto.createDecipheriv("aes-128-cbc", key, cmac3);
let decrypted = decipher.update(Buffer.from("4CBEB52C4915350EAFB5DCFCA952D950994C12A1CF070982339957B440A10A36017C", "hex"));
console.log('Data:',decrypted.toString())
