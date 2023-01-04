from itertools import product
import os
import json

def coverImg(pathes):
  print("pathes", pathes)
  loop_val = []
  for path in pathes :
    files = os.listdir(path)
    loop_val.append(files)
  fileIndex = 0
  for imgList in product(*loop_val):
    print(imgList)
    i = 0
    for img in imgList:
      imgPath = img
      bgPath = imgList[0]
      fileImgName = str(fileIndex) + ".png"
      print("imgPath", imgPath)
      print("bgPath", bgPath)
      print("fileImgName", fileImgName)
      # if os.path.exists(fileImgName):
      #   put_png_to_jpg(fileImgName, fileImgName, imgPath)
      # else:
      #   if i == 0:
      #     i = 1
      #     continue
      #   else:
      #     put_png_to_jpg(fileImgName, bgPath, imgPath)

      # floderName = imgList[1]
      # floderArr = floderName.split("/")
      # fileName = floderArr[len(floderArr)-1]
      # fileNameArr = fileName.split(".")
    with open(str(fileIndex) + '.json', 'w') as f:
      data = []
      for idx, path in enumerate(pathes) :
        fileNameArr = imgList[idx].split(".")
        data.append({
                "trait_type": path,
                "value": fileNameArr[0]
              })
      json.dump(data, f)
    fileIndex += 1

if __name__ == '__main__':
  pathes = ["Background","Fur","Expression"]
  coverImg(pathes)