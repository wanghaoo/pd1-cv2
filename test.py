from itertools import product
import os


Background = "Background"
bgFiles = os.listdir(Background)
Fur = "Fur"
FurFiles = os.listdir(Fur)
Expression = "Expression"
EFiles = os.listdir(Expression)

loop_val = [bgFiles, FurFiles, EFiles]

for i in product(*loop_val):
  print(i)