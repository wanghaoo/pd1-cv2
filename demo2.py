import json
import cv2
import numpy as np
import os
import threading
import time
from itertools import product
 
 
def add_alpha_channel(img):
    # 为jpg图像添加alpha通道
    b_channel, g_channel, r_channel = cv2.split(img)  # 剥离jpg图像通道
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255  # 创建Alpha通道
    img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))  # 融合通道
    return img_new
 
 
def merge_img(jpg_img, png_img, y1, y2, x1, x2):
    # 判断jpg图像是否已经为4通道
    if jpg_img.shape[2] == 3:
        jpg_img = add_alpha_channel(jpg_img)
    # 获取要覆盖图像的alpha值，将像素值除以255，使值保持在0-1之间
    alpha_png = png_img[y1:y2, x1:x2, 3] / 255.0
    alpha_jpg = 1 - alpha_png
    # 开始叠加
    for c in range(0, 3):
        jpg_img[y1:y2, x1:x2, c] = ((alpha_jpg * jpg_img[y1:y2, x1:x2, c]) + (alpha_png * png_img[y1:y2, x1:x2, c]))
    return jpg_img
 
 
def Resize_cv2(img_file_name, img_png):
    imgFile = cv2.imread(img_file_name)
    newImg = cv2.resize(imgFile, (img_png.shape[1], img_png.shape[0]))
    return newImg
 
 
def put_png_to_jpg(fileName, img_jpg, img_png):
    img_png = cv2.imread(img_png, cv2.IMREAD_UNCHANGED)
    img_jpg = Resize_cv2(img_jpg, img_png)  # 变换大小跟透明图一样
    res_img = merge_img(img_jpg, img_png, 0, img_png.shape[0], 0, img_png.shape[1])
    cv2.imwrite(fileName, res_img)
 
def doThread(pathes, imgList, fileIndex) : 
  i = 0
  for idx, img in enumerate(imgList):
    imgPath = pathes[idx] + "/" + img
    bgPath = pathes[0] + "/" + imgList[0]
    fileImgName = str(fileIndex) + ".png"
    if os.path.exists(fileImgName):
      put_png_to_jpg(fileImgName, fileImgName, imgPath)
    else:
      if i == 0:
        i = 1
        continue
      else:
        put_png_to_jpg(fileImgName, bgPath, imgPath)

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

def coverImg(pathes):
  loop_val = []
  for path in pathes :
    files = os.listdir(path)
    loop_val.append(files)
  fileIndex = 2976
  for imgList in product(*loop_val):
    t = threading.Thread(target=doThread, args=(pathes, imgList, fileIndex))
    t.start()
    time.sleep(2)
    fileIndex += 1

if __name__ == '__main__':
  pathes = ["Background","Fur", "Face", "Hand"]
  coverImg(pathes)