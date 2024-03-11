CFLAGS=-Wall -Wextra -Werror -pedantic -std=c99 -g

LDFLAGS=-lm -lhello

LIBDIR=~/../../usr/lib

CC=gcc



all: clean build


build: main.o libhello.so
	@$(CC) $(LDFLAGS) -o main main.o libhello.so -L. -o app

main.o: test.c
	@$(CC) $(CFLAGS) -c test.c -o main.o

hello.o: libfirst.c
	@$(CC) $(CFLAGS) -c libfirst.c -fpic -o hello.o

libhello.so: hello.o
	@$(CC) -shared -o libhello.so hello.o
	@sudo cp libhello.so $(LIBDIR)

clean:
	@rm -f *.o *.so app
