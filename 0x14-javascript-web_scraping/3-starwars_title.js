#!/usr/bin/node
const rq = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
rq(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
