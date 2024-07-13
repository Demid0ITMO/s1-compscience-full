import re


def function(x):
    return 3 * x * x + 5


def change(s):
    x = re.findall('\d+', s)
    s = re.sub('\d+', 'SOME_INT', s)
    for i in x:
        s = re.sub('SOME_INT', str(function(int(i))), s, 1)
    return s


def Test():
    tests = [
        '20 + 22 = 42',
        '234 - 24 = 190',
        '2 - 23 + 23 = 2',
        '56 + 76 = 132',
        '45 - 12 = 33'
    ]

    for test in tests:
        print(change(test))


Test()