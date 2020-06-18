import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np

import datetime

name = sys.argv[0]

def plot_rating(path_to_file, label):
  data = pd.read_csv(path_to_file)

  rating = np.array(data['rating'])
  timestamp = np.array(data['timestamp'])
  print(label, rating[-1])

  day_list = []
  for i in timestamp:
    date = datetime.datetime.strptime(i[:-7], "%Y-%m-%d %H:%M:%S")
    day_list.append(date.timetuple().tm_yday + (1.0/24)*date.timetuple().tm_hour + (1.0/(24*60))*date.timetuple().tm_min)
  now = datetime.datetime.now()
  date_today = datetime.datetime.strptime(str(now)[:-7], "%Y-%m-%d %H:%M:%S")
  #print((1.0/24)*date_today.timetuple().tm_hour)
  #print((1.0/(24*60))*date_today.timetuple().tm_min)
  day_list.append(date_today.timetuple().tm_yday + (1.0/24)*date_today.timetuple().tm_hour + (1.0/(24*60))*date_today.timetuple().tm_min)
  #print(day_list)
  rating = np.append(rating, rating[-1])

  plt.plot(day_list, rating, '-o', label=label[:-4])


print("Number of datasets: ", len(sys.argv)-1)
for i in range(1, len(sys.argv)):
  dataset = sys.argv[i]
  plot_rating(dataset, dataset)

plt.xlabel("Day")
plt.ylabel("Rating")
plt.title("Rating progress")
plt.legend()
plt.savefig('rating.png')