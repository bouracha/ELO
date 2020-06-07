import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np

name = sys.argv[0]

def plot_rating(path_to_file, label):
  data = pd.read_csv(path_to_file)

  rating = np.array(data['rating'])
  print(label, rating[-1])

  plt.plot(rating, '-o', label=label)

print("Number of datasets: ", len(sys.argv)-1)
for i in range(1, len(sys.argv)):
  dataset = sys.argv[i]
  plot_rating(dataset, dataset)

plt.xlabel("Number of Games")
plt.ylabel("Rating")
plt.title("Rating progress")
plt.legend()
plt.savefig('rating.png')