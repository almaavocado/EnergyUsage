const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();
const port = 5000; // You can change this to any available port

app.use(
  '/api',
  createProxyMiddleware({
    target: 'https://sandbox.voltus.co',
    changeOrigin: true,
  })
);

app.listen(port, () => {
  console.log(`Proxy server is running on http://localhost:${port}`);
});
