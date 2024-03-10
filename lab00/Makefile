CFLAGS=-Wall -Wextra -Werror -pedantic -std=c99 -g
# задает флаги компилятора gcc, такие как проверка кода на ошибки, предупреждения, 
# стандарт языка Си и отладочная информация.
LDFLAGS=-lm -lhello
# задает флаги для линковщика, в данном случае подключает математическую библиотеку 
# libm и библиотеку libhello.
LIBDIR=~/../../usr/lib
# задает директорию для установки создаваемой библиотеки libhello.so.
CC=gcc
# задает используемый компилятор, в данном случае gcc.


all: clean build
# all: clean build - цель all вызывает сначала очистку clean, затем сборку build.

build: main.o libhello.so
	@$(CC) $(LDFLAGS) -o main main.o libhello.so -L. -o app
# цель build собирает исполняемый файл из объектных файлов main.o и библиотеки libhello.so.
main.o: test.c
	@$(CC) $(CFLAGS) -c test.c -o main.o
# правило для создания объектного файла main.o из исходного кода test.c.
hello.o: libfirst.c
	@$(CC) $(CFLAGS) -c libfirst.c -fpic -o hello.o
# аналогично, создает объектный файл из исходника библиотеки.
libhello.so: hello.o
	@$(CC) -shared -o libhello.so hello.o
	@sudo cp libhello.so $(LIBDIR)
# создает библиотеку libhello.so, используя объектный файл hello.o.
clean:
	@rm -f *.o *.so app
# удаляет созданные файлы.
