all: exe

exe: main.o
	gcc -o exe main.o

main.o: main.c
	gcc -c -Wall main.c

clean:
	rm -f exe main.o