import tika
import matplotlib.colors as colors
from tika import parser
import os
import matplotlib.pyplot as plt
import numpy as np

lan_dict = {}
lan_list = ['JavaScript', 'Python', 'Java', 'C++', 'C', 'PHP', 'C#',  'Kotlin', 'Swift', 'Go', 'Dart', 'Object C',
            'Ruby', 'React', 'Matlab']
directory = '/home/renataqq/Downloads/Telegram Desktop/CV/ChatExport_2022-03-23/files/'
tika.initVM()
dir_list = os.listdir(directory)
new_content = ''
val_people = 0

for name in dir_list:
    val_people += 1
    try:
        print(name + ' : ', end='')
        parsed = parser.from_file(directory + name)
        content = parsed['content']
        for string in content:
            string = string.replace("\n", " ")
            string = string.replace("●", " ")
            string = string.replace("\t", " ")
            string = string.replace("-", " ")
            string = string.replace(",", " ")
            string = string.replace(".", " ")
            string = string.replace("\xa0", " ")
            string = string.replace("|", " ")
            string = string.replace(")", " ")
            string = string.replace("(", " ")
            string = string.replace("/", " ")
            new_content += string
        norm_content = new_content.split(' ')

        for language in lan_list:

            if language in norm_content:
                print(language, end=' ')
                if language not in lan_dict.keys():
                    lan_dict[language] = 1
                else:
                    lan_dict[language] += 1
            elif language.lower() in norm_content:
                print(language, end=' ')
                if language not in lan_dict.keys():
                    lan_dict[language] = 1
                else:
                    lan_dict[language] += 1
    except:
        print("Не парситься %s" % name)
    print('\n')
    new_content = ''
    norm_content = []
sort_dict = {k: v for k, v in sorted(lan_dict.items(), key=lambda item: item[1])}
print(sort_dict)
print("Всего человек участвовало: %d" % val_people)
counts = sort_dict.values()
letters = sort_dict.keys()

# graph data
bar_x_locations = np.arange(len(counts))
plt.rcParams["figure.figsize"] = (15, 10)
colors_list = list(colors._colors_full_map.values())
plt.bar(bar_x_locations, counts, align='center', color=colors_list[::7])
plt.xticks(bar_x_locations, letters)
plt.ylabel('Value')
plt.xlabel('Language')
plt.show()

