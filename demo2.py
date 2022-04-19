import cv2
import numpy as np
import os
 
 
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
 
 
def put_png_to_jpg(img_jpg, img_png):
    img_png = cv2.imread(img_png, cv2.IMREAD_UNCHANGED)
    img_jpg = Resize_cv2(img_jpg, img_png)  # 变换大小跟透明图一样
    res_img = merge_img(img_jpg, img_png, 0, img_png.shape[0], 0, img_png.shape[1])
    cv2.imwrite("output.png", res_img)
 
def coverImg():
  imgList = ["test-png/_0012_sky1.png", 
  "test-png/_0006_cityBG.png", 
  "test-png/_0004_building2.png",
  "test-png/_0003_light.png",
  "test-png/_0001_c2.png"]
  i = 0
  for img in imgList:
    if os.path.exists("output.png"):
      put_png_to_jpg("output.png", img)
    else:
      if i == 0:
        i = 1
        continue
      else:
        put_png_to_jpg(imgList[0], img)


if __name__ == '__main__':
    coverImg()