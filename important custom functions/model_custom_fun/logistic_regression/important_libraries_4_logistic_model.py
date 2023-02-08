#hide earrings 
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
#plt.style.use('seaborn')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
logR = LogisticRegression()
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, plot_confusion_matrix,roc_curve