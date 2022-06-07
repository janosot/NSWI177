#!/bin/bash
head /dev/urandom | tr -dc "$2" | head -c "$1"; echo ' '
