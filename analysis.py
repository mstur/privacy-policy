import textstat
import os
import pandas as pd
import matplotlib.pyplot as plt

directory = r'./data/'
data = {}
df = pd.DataFrame()
for filename in os.listdir(directory):
    # if filename != "microsoft.txt":
    f = open(directory+filename)
    lines = f.readlines()
    text = " ".join(lines)
    stats = {}
    stats["website"] = filename[:-4]
    stats["reading time"] = textstat.reading_time(text, ms_per_char=14.69)/60
    stats["difficulty"] = textstat.text_standard(text, float_output=True)
    stats["word count"] = textstat.lexicon_count(text, removepunct=True)
    # print(stats)
    df = df.append(stats, ignore_index=True)
    f.close()

df = df.sort_values(by=['website'])
print(df)

fig = plt.figure()
fig.set_size_inches(14, 4, forward=True)
ax = fig.add_subplot(111)
ax.axhline(8, color='blue', linewidth=2) # average US reading level
ax.set_title("Difficulty")
ax.bar(df["website"],df["difficulty"])
# plt.show()
plt.savefig('difficulty.png')


fig = plt.figure()
fig.set_size_inches(14, 4, forward=True)
ax = fig.add_subplot(111)
ax.set_title("Word Count")
ax.bar(df["website"],df["word count"])
# plt.show()
plt.savefig('words.png')

df.to_csv("out.csv", index=False)





