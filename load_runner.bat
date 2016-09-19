@echo off

type simp

timeout 1 >nul

echo starting logger
start /realtime python logger.py -s 102400
timeout 3

echo starting tcp server
start /realtime python net_load.py
timeout 3

echo starting tcp clients
start /realtime python tcp_client.py
timeout 3

echo starting memory load
start /realtime python memory_load.py -c 128
start /realtime python memory_load.py -c 256
start /realtime python memory_load.py -c 512
timeout 3

echo starting cpu load
start /realtime python cpu_load.py
timeout 3
