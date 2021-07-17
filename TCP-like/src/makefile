all: alternated

alternated: alternated.o
	gcc -o alternated alternated.o

alternated.o: alternated.c
	gcc -c -Wall alternated.c

clean:
	rm -f alternated alternated.o