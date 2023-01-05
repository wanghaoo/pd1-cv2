from itertools import product
import os
import json
import time
import threading

def doTrhead(pathes, imgList, fileIndex) :
  i = 0
  for img in imgList:
    imgPath = img
    bgPath = imgList[0]
    fileImgName = str(fileIndex) + ".png"
    print("imgPath", imgPath)
    print("bgPath", bgPath)
    print("fileImgName", fileImgName)
  with open(str(fileIndex) + '.json', 'w') as f:
    data = []
    for idx, path in enumerate(pathes) :
      fileNameArr = imgList[idx].split(".")
      data.append({
              "trait_type": path,
              "value": fileNameArr[0]
            })
    json.dump(data, f)

def coverImg(pathes):
  print("pathes", pathes)
  loop_val = []
  for path in pathes :
    files = os.listdir(path)
    loop_val.append(files)
  fileIndex = 0
  for imgList in product(*loop_val):
    t = threading.Thread(target=doTrhead, args=(pathes, imgList, fileIndex))
    t.start()
    time.sleep(1)
    fileIndex += 1

if __name__ == '__main__':
  pathes = ["Background","Fur", "Face", "Hand"]
  coverImg(pathes)