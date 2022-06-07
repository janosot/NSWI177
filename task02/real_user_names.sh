#!/bin/bash
getent passwd | cut -d: -f 1,5 | grep -E ".*:.+" | sort | sed 's#\(.*\):\(.*\)#\2:\1#'
