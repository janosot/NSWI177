#!/bin/bash
awk 'BEGIN {FS = ":"} ; {sum+=$3} END {print sum}' /etc/group
