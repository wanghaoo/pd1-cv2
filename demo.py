import cv2

def coverImg():
  overlay("test-png/_0012_sky1.png", "test-png/_0006_cityBG.png")
  overlay("demo.png", "test-png/_0004_building2.png")
  overlay("demo.png", "test-png/_0003_light.png")
  overlay("demo.png", "test-png/_0000_c3.png")

def overlay(bgImgPath, overPath): 
  img1 = cv2.imread(bgImgPath)
  img2 = cv2.imread(overPath)

  rows,cols,_ = img2.shape
  roi = img1[0:rows, 0:cols ]
  
  img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
  
  # cv2.imshow('img2gray',img2gray)
  # cv2.waitKey(0)
  _, mask = cv2.threshold(img2gray, 250, 255, cv2.THRESH_BINARY)
  
  # cv2.imshow('mask',mask)
  # cv2.waitKey(0)
  
  mask_inv = cv2.bitwise_not(mask)
  
  # cv2.imshow('mask_inv',mask_inv)
  # cv2.waitKey(0)
  
  img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
  
  # cv2.imshow('img1_bg',img1_bg)
  # cv2.waitKey(0)
  
  img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)
  # cv2.imshow('img2_fg',img2_fg)
  # cv2.waitKey(0)
  
  dst = cv2.add(img1_bg,img2_fg)
  img1[0:rows, 0:cols ] = dst
  
  # cv2.imshow('res',img1)
  # cv2.waitKey(0)
  # cv2.destroyAllWindows()
  
  cv2.imwrite("demo.png", img1)

def overlay2(bgImg, overImg):
  img1 = cv2.imread(bgImg)
  img2 = cv2.imread(overImg)

  # 把logo放在左上角，所以我们只关心这一块区域
  rows, cols, _ = img2.shape
  roi = img1[0:rows, 0:cols]

  # 创建掩膜
  img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
  ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
  mask_inv = cv2.bitwise_not(mask)

  # 保留除logo外的背景
  img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
  cv2.imshow("img1_bg", img1_bg)
  cv2.waitKey(0)
  dst = cv2.add(img1_bg, img2) # 进行融合
  cv2.imshow("dst", dst)
  cv2.waitKey(0)
  img1[:rows, :cols] = dst # 融合后放在原图上

  cv2.imshow('res',img1)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__ == '__main__':
    coverImg()