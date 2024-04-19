"""
Расстояние на одометре моего автомобиля отображается в целых числах (милях), до 999999.
На прошлой неделе я ехал по автостраде и заметил, что последние пять цифр - сформировали палиндром: то есть,
число, которое одинаково читается и назад, и вперед (например, 12321).
После того, как я проехал одну милю, мои последние пять цифр снова показывали палиндром;
и после еще одной мили - средние четыре цифры сформировали палиндром.
И, наконец, после третьей мили  - все шесть цифр сформировали палиндром.
Каков был мой пробег в то время, когда я сначала заметил все эти палиндромы?
"""


def chk1(x):
    x1 = x // 10000
    x2 = (x // 1000) % 10
    x3 = (x // 100) % 10
    x4 = (x // 10) % 10
    x5 = x % 10
    if x1 == x5 and x2 == x4:
        return True


def chk2(x):
    x1 = x // 1000
    x2 = (x // 100) % 10
    x3 = (x // 10) % 10
    x4 = x % 10
    if x1 == x4 and x2 == x3:
        return True


def chk3(x):
    x1 = x // 100000
    x2 = (x // 10000) % 10
    x3 = (x // 1000) % 10
    x4 = (x // 100) % 10
    x5 = (x // 10) % 10
    x6 = x % 10
    if x1 == x6 and x2 == x5 and x3 == x4:
        return True


def main():
    for i in range(100000, 999999+1):
        if chk1(int(str(i)[1:])) and chk1(int(str(i + 1)[1:])) and chk2(int(str(i + 2)[1:4])) and chk3(i + 3):
            print(i)
            return


main()
