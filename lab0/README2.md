# programming
lab №0
# Отчет 
## Задание 
Сложность:
    Medium 
    
    Соберите для своей программы 2 библиотеки - статическую и динамическую

## Этапы работы 

### 1. Создание статической библиотеки 
Я буду создавать библиотеку, которая будет содержать функцию вывода фразы «Hello, world!» на экран.
Создам реализацию функции в файле `libfirst.c` :

```
#include <stdio.h>

void say_hello() {
    printf("Hello, world!\n");
}
```

Каждую функцию библиотеки необходимо объявить в её заголовочном файле, в моем случае это `libfirst.h` :

```
void say_hello();
```

Теперь, все это дело надо скомпилировать:

```
gcc -g -c -o libfirst.o libfirst.c
```

Флаг `-с` сообщает компилятору, что необходимо пропустить этап компоновки (linking), а `-g` — сообщает о том, что отладчик — `gdb`.

После компиляции библиотеки будет создан объектный файл который необходимо упаковать в архив:

```
ar rcs libfirst.a libfirst.o
```

* r — удалять libhello.o после добавления в архив
* с — создавть новый архив, если существует — перезаписать.
* s — добавить индекс объектного файла в архив


Теперь перейдем к тесту. Создам файл `test.c` :

```
#include "libfirst.h"

int main(){
  say_hello();
  return 0;
}
```

Компилируем :

```
gcc test.c -o test -lfirst -L.
```

Ключ `-L` нужен, чтобы сообщить компилятору о месте нахождения статической библиотеки, а ключ `-l`, чтобы подключить библиотеку.

#### Скрин работы 
![Image text](https://github.com/mgrkikyan/programming/blob/main/lab0/стат_результат.png)

### 2. Создание динамической библиотеки 
Динамическая библиотека создается очень быстро и просто.

```
gcc -shared -fPIC -o libfirst.so first.o
```

Когда используются статическая библиотека и динамическая библиотека, параметры компиляции GCC одинаковы: 
```
gcc test.c -o test -lfirst -L.
```

#### Скрин работы
![Image text](https://github.com/mgrkikyan/programming/blob/main/lab0/создание_динамической_библиотеки.png)
![Image text](https://github.com/mgrkikyan/programming/blob/main/lab0/компиляция_и_тест.png)

# Список использованных источников:
1. https://blablacode.ru/programmirovanie/84
2. https://www.youtube.com/watch?v=gq_ZXCuRhU4&list=PLA1FTfKBAEX4hblYoH6mnq0zsie2w6Wif
3. https://russianblogs.com/article/29112860416/
