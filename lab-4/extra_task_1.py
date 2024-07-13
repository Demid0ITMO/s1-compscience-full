from bs4 import BeautifulSoup
def task():
    with open("site.xml") as fin:
        s = fin.read()
    soup = BeautifulSoup(s, "lxml")

    with open("file_for_extra_task_1.json", "w") as fout:
        print("{\n\t\"schedule\": {", file=fout)
        day = soup.find("day")
        print('\t\t\"day\": \"' + day.get_text() + '\",', file=fout)
        lessonstr = soup.find_all("lesson")
        tags = ['time', 'weeks', 'place', 'class', 'discipline', 'tw', 'teacher', 'format']
        print('\t\t\"lesson\": [', file=fout)
        for i in range(len(lessonstr)):
            print('\t\t\t{', file=fout)
            with open("lesson.xml", 'w') as file:
                print(lessonstr[i], file=file)
            with open("lesson.xml") as file:
                x = file.read()
            soup = BeautifulSoup(x, "lxml")
            for j in range(len(tags)):
                if j == len(tags) - 1:
                    print('\t\t\t\t\"' + tags[j] + '\": \"' + soup.find(tags[j]).text + '\"', file=fout)
                elif tags[j] == 'weeks':
                    print('\t\t\t\t\"' + tags[j] + '\": [' + soup.find(tags[j]).text + '],', file=fout)
                else:
                    print('\t\t\t\t\"' + tags[j] + '\": \"' + soup.find(tags[j]).text + '\",', file=fout)
            if i == len(lessonstr) - 1:
                print('\t\t\t}', file=fout)
            else:
                print('\t\t\t},', file=fout)
        print('\t\t]\n\t}\n}', file=fout)

task()