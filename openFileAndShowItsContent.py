import matplotlib.pyplot as plt
import numpy as np  
from PyQt5.QtWidgets import QFileDialog, QApplication

app = QApplication([])
file = QFileDialog.getOpenFileName(filter="*.txt")

if file:
    with open(file[0], "r") as f:
        lines = f.readlines()

        print(lines)

        data = [int(line.strip()) for line in lines]

        plt.plot(data)
        plt.show()

else:
    print("We haven't selected a file")