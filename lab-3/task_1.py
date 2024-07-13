import re


# 367522
# Глаза - 2, нос - 2, рот - 1

def count(s):
    how_much = len(re.findall(r'X-\{\)', s))
    print(how_much, "smiles in test")
    return how_much


def Test():
    tests = [
        ("smile X-{) is a smile X-{)", 2),
        ("I dont know X-{) X-{) what X-{) i have to X-{) write X-{) in message", 5),
        ("Do X-{) you know X-{) the way X-{)", 3),
        ("This is not X-{G smiles that I need X-{}", 0),
        ("X-{)X-{)", 2)
    ]
    for test, answer in tests:
        print(count(test) == answer)

Test()

