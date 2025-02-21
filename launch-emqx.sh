#!/bin/sh
mkdir -p data
docker run -d --name emqx \
           -p 8085:8085 -p 8086:8086 -p 18083:18083 \
           -v $(pwd)/emqx.conf:/opt/emqx/etc/emqx.conf \
           -v $(pwd)/data:/opt/emqx/data \
           emqx/emqx:latest
