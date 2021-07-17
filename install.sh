#!/usr/bin/env bash
# This Code write by Mr.nope
# Version: 1.4.1
if [[ "$(id -u)" -ne 0 ]]; then
  echo "Please, Run This Programm as Root!"
  echo ""
  exit 1
fi
start() {
    printf '\033]2;Make-File-Installing\a'
    clear
    echo "Installing..."
    sleep 2
    apt install python3
    apt install python
    apt install python3-pip
    pip3 install --upgrade pip
}
chmod +x tool.py
start
