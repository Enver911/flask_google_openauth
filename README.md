1. Fill in the following fields in the config:<br>
<b>client_id</b><br>
<b>client_secret</b><br>
<b>redirect_uri</b><br>
3. Obtain self-signed certificates:<br>
<b>openssl req -x509 -newkey rsa:4096 -keyout certificates/key.pem -out certificates/cert.pem -days 365 -nodes</b>
4. Start server on localhost:<br>
<b>python main.py</b>
5. Paste in browser to test:<br>
<b>https://127.0.0.1:5000</b>
