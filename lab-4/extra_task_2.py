from bs4 import BeautifulSoup
import re

def task():
    with open("site.xml") as fin:
        s = fin.read()
    soup = BeautifulSoup(s, "lxml")

    with open("file_for_extra_task_2.json", "w") as fout:
        print("{\n\t\"schedule\": {", file=fout)
        day = soup.find("day")
        print('\t\t\"day\": \"' + day.get_text() + '\",', file=fout)
        lessonstr = soup.find_all("lesson")
        print('\t\t\"lesson\": [', file=fout)
        for i in range(len(lessonstr)):
            print('\t\t\t{', file=fout)
            with open("lesson.xml", 'w') as file:
                print(lessonstr[i], file=file)
            with open("lesson.xml") as file:
                d = file.read()
            x = re.findall(r"<\S+>.+</\S+>", d)
            for j in range(len(x)):
                tag_and_text = re.match(r'<(\S+)>(.+)</\S+>', x[j]).groups()
                if j == len(x) - 1:
                    print("\t\t\t\t\"" + tag_and_text[0] + "\": \"" + tag_and_text[1] + "\"", file=fout)
                elif tag_and_text[0] == 'weeks':
                    print("\t\t\t\t\"" + tag_and_text[0] + "\": [" + tag_and_text[1] + "],", file=fout)
                else:
                    print("\t\t\t\t\"" + tag_and_text[0] + "\": \"" + tag_and_text[1] + "\",", file=fout)
            if i == len(lessonstr) - 1:
                print('\t\t\t}', file=fout)
            else:
                print('\t\t\t},', file=fout)
        print('\t\t]\n\t}\n}', file=fout)

task()