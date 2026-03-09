const express = require('express');
const app = express();

app.get('/', (req, res) => {
res.send('<h1>Servidor Node.js Rodando!</h1><p>Alunos, este é o Back-End em ação.</p>');
});

app.listen(3000, () => console.log('Acesse http://localhost:3000 no seu navegador!'));

