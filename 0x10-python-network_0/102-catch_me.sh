#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -s -o 0.0.0.0:5000/catch_me | grep "You got me!"
