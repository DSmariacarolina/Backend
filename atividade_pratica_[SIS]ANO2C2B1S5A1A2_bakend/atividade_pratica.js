const os = require("os");

console.log("__Informações do Sistema__");
console.log("Sistema Operacional", os.type());
console.log("Memoria livre:", (os.freemem()/1024/1024/1024) .toFixed(2), "GB");
