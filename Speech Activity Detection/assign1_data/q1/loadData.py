import librosa as lb
import numpy as np
import pandas as pd 
import IPython.display as ipd
import matplotlib.pyplot as plt


#load audio file
#path = "C:\Users\DELL\OneDrive\Desktop\PR Assignment\assign1_data\q1\"
seg2_ste = np.loadtxt("Segment2_STEnergy.csv")
seg2_mel = np.loadtxt("Segment2_MelEnergy.csv")

plt.plot(seg2_ste)
plt.plot(seg2_ste)
plt.show()

