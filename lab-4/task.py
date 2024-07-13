def find_open_tag(xml_str: str, tag: str): # ищет все первые символы после указанного тэга
    tags = []
    for i in range(len(xml_str) - len(tag)):
        if xml_str[i:i+len(tag)] == tag:
            tags += [i+len(tag)]
    return tags

def find_close_tag(xml_str: str, tag: str): # ищет все последние символы перед указанным тэгом
    tags = []
    for i in range(len(xml_str) - len(tag)):
        if xml_str[i:i+len(tag)] == tag:
            tags += [i]
    return tags

def task():
    with open('site.xml') as fin:
        s = fin.read()
    with open("file.json", "w") as fout:
        print('{\n\t\"schedule\": {', file=fout)
        open_day = find_open_tag(s, "<day>")
        close_day = find_close_tag(s, "</day>")
        tag = 'day'
        for i in range(len(open_day)):
            print('\t\t\"' + tag + '\": \"' + s[open_day[i]:close_day[i]] + '\",', file=fout)

        open_lesson = find_open_tag(s, "<lesson>")
        close_lesson = find_close_tag(s, "</lesson>")
        tag = 'lesson'
        print('\t\t\"' + tag + '\": [', file=fout)
        for i in range(len(open_lesson)):
            lessonstr = s[open_lesson[i]:close_lesson[i]]
            print('\t\t\t{', file=fout)
            tags = ['time', 'weeks', 'place', 'class', 'discipline', 'tw', 'teacher', 'format']
            for name_of_tag in tags:
                open_tag = find_open_tag(lessonstr, "<" + name_of_tag + ">")
                close_tag = find_close_tag(lessonstr, "</" + name_of_tag + ">")
                tag = name_of_tag
                for j in range(len(open_tag)):
                    if name_of_tag == 'weeks':
                        print('\t\t\t\t\"' + tag + '\": [' + lessonstr[open_tag[j]:close_tag[j]] + '],', file=fout)
                    elif name_of_tag == 'format':
                        if i == len(open_lesson) - 1:
                            print('\t\t\t\t\"' + tag + '\": \"' + lessonstr[open_tag[j]:close_tag[j]] + '\"\n\t\t\t}', file=fout)
                        else:
                            print('\t\t\t\t\"' + tag + '\": \"' + lessonstr[open_tag[j]:close_tag[j]] + '\"\n\t\t\t},', file=fout)
                    else:
                        print('\t\t\t\t\"' + tag + '\": \"' + lessonstr[open_tag[j]:close_tag[j]] + '\",', file=fout)
        print('\t\t]\n\t}\n}', file=fout)

task()