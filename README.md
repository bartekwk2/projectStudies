# projectStudies
Projekt na przedmiot Zaawansowane Programowanie

Adres Url: https://guarded-hamlet-47284.herokuapp.com

<br><br>
Zadanie 1
<ul>
<li>Endpoint: [GET] /prime<input></li>
<li>Request data: {input} as path param</li>
<li>Response data: info wheter number is prime or not</li>
</ul>

<br><br>
Zadanie 2
<ul>
<li>Endpoint: [POST] /picture/invert</li>
<li>Request data: picture in jpg format as binary file in request body</li>
<li>Response data: jpg picture with inverted colors</li>
</ul>

<br><br>
Zadanie 3

<i>Register new user </i>
<ul>
<li>Endpoint: [POST] /register</li>
<li>Request data: "email":String, "password":String in json body</li>
<li>Response data: info wheter user is added succesfully</li>
</ul>
<br>

<i>Login user </i>
<br>
<ul>
<li>Endpoint: [POST] /login</li>
<li>Request data: "email":String, "password":String in json body</li>
<li>Response data: access token</li>
</ul>
<br>

<i>Get current time</i>
<br>
<ul>
<li>Endpoint: [POST] /time</li>
<li>Request header: Bearer {access_token}</li>
<li>Response data: current time in UTC timezone</li>
</ul>

