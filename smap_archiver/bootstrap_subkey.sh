#!/usr/bin/env bash
echo "Starting server"
./start_postgres.sh >log 2>&1 &
echo "Delaying"
sleep 5
echo "Server log: "
cat log
echo "Doing bootstrap"
echo "----"

python subkey_bootstrap.py

pkill -term postgres
sleep 2
