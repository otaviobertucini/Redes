all: alternated gobackn

alternated: alternated.o
	gcc -o alternated alternated.o

alternated.o: alternated.c
	gcc -c -Wall alternated.c

gobackn: gobackn.o
	gcc -o gobackn gobackn.o

gobackn.o: gobackn.c
	gcc -c -Wall gobackn.c

clean:
	rm -f alternated alternated.o gobackn gobackn.o