#!/bin/bash
env | grep "$(whoami)" | cut -d "=" -f 1
