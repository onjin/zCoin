PHONY=miner

all:
	gcc -o miner miner.c -l pthread -l sqlite3
