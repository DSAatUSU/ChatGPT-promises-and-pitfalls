import matplotlib.pyplot as plt
from datetime import datetime, date
import numpy
from csv import DictReader

csvfile = open("tests_data/dataTimestamp.csv")
csv_dict = DictReader(csvfile)
timestamps = [int(row["timestamp"]) for row in csv_dict]
csvfile.close()

csvfile = open("tests_data/dataTimestamp.csv")
csv_dict = DictReader(csvfile)
ids = [int(row["id"]) for row in csv_dict]
csvfile.close()

min_date = numpy.min(timestamps) 
max_date = numpy.max(timestamps)

print(ids)
print(timestamps)
labels = ['{} - {}'.format(id, t) for id, t in zip(ids, timestamps)]
print(labels)
fig, ax = plt.subplots(figsize=(15, 4), constrained_layout=True)
_ = ax.set_ylim(-2, 1.75)
_ = ax.set_xlim(min_date, max_date)
_ = ax.axhline(0, xmin=0.05, xmax=0.95, c='deeppink', zorder=1)
_ = ax.scatter(timestamps, numpy.zeros(len(timestamps)), s=120, c='palevioletred', zorder=2)
_ = ax.scatter(timestamps, numpy.zeros(len(timestamps)), s=30, c='darkmagenta', zorder=3)

label_offsets = numpy.zeros(len(timestamps))
label_offsets[::2] = 0.35
label_offsets[1::2] = -0.7
for i, (l, d) in enumerate(zip(labels, timestamps)):
    _ = ax.text(d, label_offsets[i], l, rotation="vertical", ha='center', fontfamily='serif', fontweight='bold', color='royalblue',fontsize=12)

stems = numpy.zeros(len(timestamps))
stems[::2] = 0.3
stems[1::2] = -0.3   
markerline, stemline, baseline = ax.stem(timestamps, stems)
_ = plt.setp(markerline, marker=',', color='darkmagenta')
_ = plt.setp(stemline, color='darkmagenta')

# hide lines around chart
for spine in ["left", "top", "right", "bottom"]:
    _ = ax.spines[spine].set_visible(False)
# hide tick labels
_ = ax.set_xticks([])
_ = ax.set_yticks([])
_ = ax.set_title('Important Milestones in Rock and Roll', fontweight="bold", fontfamily='serif', fontsize=16, 
                 color='royalblue')

plt.show()
