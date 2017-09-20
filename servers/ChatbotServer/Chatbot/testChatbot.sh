#!/bin/bash

curl -H "Content-Type: application/json" -X POST -d '{"message":"Hello Ovation","clientId":"1"}' http://127.0.0.1:5000/message
curl -H "Content-Type: application/json" -X POST -d '{"message":"I want to move!","clientId":"1"}' http://127.0.0.1:5000/message
curl -H "Content-Type: application/json" -X POST -d '{"message":"Dominik","clientId":"1"}' http://127.0.0.1:5000/message
