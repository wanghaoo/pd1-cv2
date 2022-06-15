from itertools import product
import os

bgPath = "蝴蝶/背景"
bgFiles = os.listdir(bgPath)

dzPath = "蝴蝶/点缀"
dzFiles = os.listdir(dzPath)

hdPath = "蝴蝶/蝴蝶"
hdFiles = os.listdir(hdPath)

zsPath = "蝴蝶/装饰"
zsFiles = os.listdir(zsPath)


loop_val = [bgFiles, dzFiles, hdFiles, zsFiles]

for i in product(*loop_val):
  print(i)