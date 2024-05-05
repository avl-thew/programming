# programming
lab №0
# Отчет 
## Задание 
Сложность:
    Rare

    1. Создайте репозиторий для дисциплины на GitHub.
    2. Склонируйте его себе на ПК.
    3. Напишите свою первую программу.
    4. Скомпилируйте и запустите её.
    5. Получите по отдельности результаты каждого этапа компиляции.
    6. Напишите отчёт в README.md. Отчёт должен содержать:
        6.1 Задание
        6.2 Описание проделанной работы
        6.3 Консольные команды
        6.4 Скриншоты результатов
        6.5 Ссылки на используемые материалы
    7. Сделайте коммит и пуш.
    8. Добавьте для себя в отчёт шпаргалку по работе с git.
 
 ## Этапы работы 
 ### 1. Создайте репозиторий для дисциплины на GitHub
 репозиторий: https://github.com/mgrkikyan/programming.git
 ### 2. Склонируйте его себе на ПК
 ```
 get clone https://github.com/mgrkikyan/programming.git
 ```

### 3. Напишите свою первую программу
```
#include <stdio.h>

int main()
{
    printf("Hello, World!\n");
    return 0;
    
}
```

### 4. Скомпилируйте и запустите её
![Image text](https://github.com/mgrkikyan/programming/blob/main/lab0/команда%20компиляции.png)

### 5. Получите по отдельности результаты каждого этапа компиляции
## Препроцессор
![Image text](https://github.com/mgrkikyan/programming/blob/main/lab0/препроцессор.png)
```
gcc first.c -Wall -E > first.e
```
## Компилятор
### Код ассемблера
![Image text](https://github.com/mgrkikyan/programming/blob/main/lab0/код%20ассемблера.png)
```
gcc first.c -Wall -o first.s -S
```
## Ассемблирование 
### Объектный файл 
![Image text](https://github.com/mgrkikyan/programming/blob/main/lab0/объектный%20файл.png)

### 7. Сделайте коммит и пуш
![Image text](https://github.com/mgrkikyan/programming/blob/main/lab0/коммит%20и%20пуш.png)

### 8. Добавьте для себя в отчёт шпаргалку по работе с git
 ```shell
git clone
git add .
git commit
git push
```

`git clone` - команда, используемая для создания копии определенного репозитория или ветки в репозитории.

`git add` добавляет новые или измененные файлы в рабочем каталоге в промежуточную область Git.

`git commit` создает фиксацию, которая похожа на снимок репозитория. Фиксации включают в себя множество метаданных в дополнение к содержимому и сообщению, таких как автор, временная метка и многое другое.

`git push` загружает все локальные фиксации ветки в соответствующую удаленную ветку.

## Список использованных источников:
1. https://github.com/git-guides
2. https://github.com/still-coding/report_demo/blob/main/README.md?plain=
