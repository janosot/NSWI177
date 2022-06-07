#!/bin/bash
find "${@:2}" -type f -exec wc "$1" {} +
