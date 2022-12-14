# Алгоритмы и структуры данных

## Оглавление:
1. [Простейшие алгоритмы *(Leson_1)*][Leson_1]
2. [Алгебра логики *(Leson_2)*][Leson_2]
   - [Составные высказывания][Compound statements]
   - [Таблица истинности][Truth table]
   - [Дизъюнктивная нормальная форма][Disjunctive normal form]
   - [Законы истиности][The Laws of truth]
3. [Системы счисления *(Leson_3)*][Leson_3]
   - [Схема Горнара][Gornar Scheme]
   - [Обозначения в Python][Notation in Python]
   - [Однопроходные алгоритмы][Single - pass algorithms]


<br><br><br><br><br><br><br>

## Простейшие алгоритмы *(Leson_1)*
1. **Обмен значениями переменных**
    ```python
    a = 2
    b = 3
    print(f'a = {a}\nb = {b}\n')
    a, b = b, a
    print(f'a = {a}\nb = {b}')
    ```
   *Output*
    ```
    a = 2
    b = 3
    
    a = 3
    b = 2
    
    Process finished with exit code 0
    ```
    В этом алгоритме используется множественное присваевание:<br>
    ```python
    x, y, z = 1, 2, 3
    ```
    Если алгоритм расписать полностью то получится:<br>
    ```python
    a = 2
    b = 3
    tmp_1 = a
    tmp_2 = b
    b = tmp_1
    a = tmp_2
    
    # или же
    a = 2
    b = 3
    tmp_1, tmp_2 = a, b
    a, b = tmp_2, tmp_1
    ```
2. **Цикл while**
    ```python
    while условие:    # заголовок цикла
        оператор_1    # тело цикла
        оператор_2    # тело цикла
        ...           # тело цикла
        оператор_n    # тело цикла
    else:
        '''выполняется после окончания цикла,
        если цикл был прерван то не выполняется'''
    ```


## Алгебра логики *(Leson_2)*
### Составные высказывания
1. Инверсия `¬A`
2. Конъюнкция `A и B`
3. Дизъюнкция `A или B`
4. Импликация `A ⟶ B`
5. Эквиваленция `A ⟷ B`
6. XOR (исключающее или) `A ⊕ B`

### Таблица истинности
| ***x*** | ***y*** | x * y | x + y | x ⊕ y | x ⟶ y | x = y | x ≠ y |
|:-------:|:-------:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| ***0*** | ***0*** |   0   |   0   |   0   |   1   |   1   |   0   |
| ***0*** | ***1*** |   0   |   1   |   1   |   1   |   0   |   1   |
| ***1*** | ***0*** |   0   |   1   |   1   |   0   |   0   |   1   |
| ***1*** | ***1*** |   1   |   1   |   0   |   1   |   1   |   0   |


### Дизъюнктивная нормальная форма
| ***x*** | ***y*** | ***z*** | F = | F₁ + | F₂ + | F₃  |
|:-------:|:-------:|:-------:|:---:|:----:|:----:|:---:|
| ***0*** | ***0*** | ***0*** |  1  |  1   |  0   |  0  |
| ***0*** | ***0*** | ***1*** |  0  |  0   |  0   |  0  |
| ***0*** | ***1*** | ***0*** |  0  |  0   |  0   |  0  |
| ***0*** | ***1*** | ***1*** |  1  |  0   |  1   |  0  |
| ***1*** | ***0*** | ***0*** |  0  |  0   |  0   |  0  |
| ***1*** | ***0*** | ***1*** |  0  |  0   |  0   |  0  |
| ***1*** | ***1*** | ***0*** |  1  |  0   |  0   |  1  |
| ***1*** | ***1*** | ***1*** |  0  |  0   |  0   |  0  |


Из чего следует, что:

`F = (¬x * ¬y * ¬z) + (¬x * y * z) + (x * y * ¬z)`

Так же по дизъюнктивнай нормальной форме:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Импликация:&nbsp;&nbsp;&nbsp;&nbsp;`x ⟶ y = ¬x + y`<br>
&nbsp;&nbsp;&nbsp;&nbsp;Эквиваленция: `x == y = x * y + ¬x * ¬y`<br>

### Законы истиности
1. Закон взаимодействия с константами<br>
   `0 + x = x` `1 + x = 1` `0 * x = 0` `1 * x = x`<br><br>
2. Закон повторения<br>
   `x * x = x` `x + x = x`<br><br>
3. Закон "Третий лишний"<br>
   `x + ¬x = 1` `x * ¬x = 0`<br><br>
4. Закон поглащения<br>
   `x * (x + y) = x` `x + x * y = x`<br><br>
5. Свойства логических операций __*__ и **+** (ассоциативность)<br>
   `(x * y) * z = x * (y * z) = x * y * z` `(x + y) + z = x + (y + z) = x + y + z`<br><br>
6. Свойства логических операций __*__ и **+** (коммутативность)<br>
   `x * y = y * x` `x + y = y + x`<br><br>
7. Свойства логических операций __*__ и **+** (дистрибутивность)<br>
   `x * (y + z) = x * y + x * z` `x + (y * z) = (x + y) * (x + z)`<br><br>
8. Законы Де Моргана<br>
   `¬(x + y) = ¬x * ¬y` `¬(x * y) = ¬x + ¬y`<br><br>
9. Закон отрицания<br>
   `¬¬x = x`

## Системы счисления (Leson_3)
| 2-ая | 4-ая | 8-ая | 10-ая | 16-ая |
|:----:|:----:|:----:|:-----:|:-----:|
| 0000 |  00  |  00  |  01   |   0   |
| 0001 |  01  |  01  |  02   |   1   |
| 0010 |  02  |  02  |  03   |   2   |
| 0011 |  03  |  03  |  04   |   3   |
| 0100 |  10  |  04  |  05   |   4   |
| 0101 |  11  |  05  |  06   |   5   |
| 0110 |  12  |  06  |  07   |   6   |
| 0111 |  13  |  07  |  08   |   7   |
| 1000 |  20  |  10  |  09   |   8   |
| 1001 |  21  |  11  |  10   |   9   |
| 1010 |  22  |  12  |  11   |   A   |
| 1011 |  23  |  13  |  12   |   B   |
| 1100 |  30  |  14  |  13   |   C   |
| 1101 |  31  |  15  |  14   |   D   |
| 1110 |  32  |  16  |  15   |   E   |
| 1111 |  33  |  17  |  16   |   F   |


### Схема Горнара для систем счисления
```
1234₅
1₅ = 1
12₅ = 10₅ + 2 = 1 * 5 + 2
123₅ = 120₅ + 3 = (1 * 5 + 2) * 5 + 3
1234₅ = 1230₅ + 4 = ((1 * 5 + 2) * 5 + 3) * 5 + 4
```
Схема позволяет вычислять число двигаясь слева на право

### Обозначения в Python
```python
x = 0b1111 # binary (двоичная)
y = 0o4567 # octal (восьмеричная)
z = 0x89AB # hexadecimal (шестнадцатеричная)
a = int('Z3F9', base=36) # заданная система исчисления (max == 36)
b = 127
bin(b) # функция возвращает строку соответствующую двоичной записи числа
oct(b) # функция возвращает строку соответствующую восьмеричной записи числа
hex(b) # функция возвращает строку соответствующую шестнадцатеричной записи числа
```

Перевод из 10-ой в N-ую систему исчисления:
```python
base = int(input())
x = int(input())
x_base = ''
while x > 0:
    digit = x % base
    x_base = digit + x_base
    x //= base
else:
   x_base = int(x_base)
print(x_base)
```

### Однопроходные алгоритмы
```mermaid
graph TD;
    number-->number;
    number-->sequence_of_numbers;
    sequence_of_numbers-->number
```

Алгоритм не требующий запоминать все числа
```
[x₁, x₂, ..., xₙ] ⟶ yₙ₋₁
F(yₙ₋₁, xₙ) ⟶ yₙ
```

| Название алгоритма                 |  [ ]  |      Переход       |
|:-----------------------------------|:-----:|:------------------:|
| Подсчёт (n)                        |   0   |       n += 1       |
| Сумма (S)                          |   0   |       S += x       |
| Произведение (p)                   |   1   |       p *= x       |
| Максимум (m)                       | None  |   m = max(m, x)    |
| Поиск числа последовательности (f) | False | f = f or (x == xₙ) |
`где xₙ - искомое число`



















[Leson_1]: https://github.com/BurdichxD4r/test_tasks_and_algorithms/blob/main/algorithms/README.md#простейшие-алгоритмы-leson_1
[Leson_2]: https://github.com/BurdichxD4r/test_tasks_and_algorithms/blob/main/algorithms/README.md#алгебра-логики-leson_2
[Compound statements]: https://github.com/BurdichxD4r/test_tasks_and_algorithms/blob/main/algorithms/README.md#составные-высказывания
[Truth table]: https://github.com/BurdichxD4r/test_tasks_and_algorithms/blob/main/algorithms/README.md#таблица-истиности
[Disjunctive normal form]: https://github.com/BurdichxD4r/test_tasks_and_algorithms/blob/main/algorithms/README.md#дизъюнктивная-нормальная-форма
[The Laws of truth]: https://github.com/BurdichxD4r/test_tasks_and_algorithms/blob/main/algorithms/README.md#законы-истиности
[Leson_3]: https://github.com/BurdichxD4r/test_tasks_and_algorithms/blob/main/algorithms/README.md#системы-счисления-leson_3
[Gornar Scheme]: https://github.com/BurdichxD4r/test_tasks_and_algorithms/blob/main/algorithms/README.md#схема-горнара-для-систем-счисления
[Notation in Python]: https://github.com/BurdichxD4r/test_tasks_and_algorithms/blob/main/algorithms/README.md#обозначения-в-python
[Single - pass algorithms]: https://github.com/BurdichxD4r/test_tasks_and_algorithms/blob/main/algorithms/README.md#однопроходные-алгоритмы




