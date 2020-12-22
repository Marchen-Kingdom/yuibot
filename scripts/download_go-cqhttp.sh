#!/bin/bash

rm -r go-cqhttp
mkdir go-cqhttp
cd go-cqhttp
curl -LJO https://github.com/Mrs4s/go-cqhttp/releases/download/v0.9.35-fix1/go-cqhttp-v0.9.35-fix1-linux-amd64.tar.gz
tar -xvzf go-cqhttp-v0.9.35-fix1-linux-amd64.tar.gz
rm go-cqhttp-v0.9.35-fix1-linux-amd64.tar.gz
