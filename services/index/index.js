const express = require('express');
const fetch = require('node-fetch');
const app = express();
const PORT = process.env.PORT || 8080;
const BACKEND = process.env.EMPLOYEE_API_URL || 'http://localhost:5000';

app.get('/', (req, res) => {
  res.send(`<h1>Employee Management - 25RP18224-nzayisenga</h1>\n<p>Endpoints:</p>\n<ul>\n<li><a href="/api/employees">/api/employees</a> - proxied to the Flask service</li>\n</ul>`);
});

app.get('/api/employees', async (req, res) => {
  try {
    const r = await fetch(`${BACKEND}/employees`);
    const data = await r.json();
    res.json(data);
  } catch (err) {
    res.status(502).json({ error: 'Bad gateway', detail: err.message });
  }
});

app.listen(PORT, () => console.log(`Index server running on ${PORT}, proxy -> ${BACKEND}`));
