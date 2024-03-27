import cv2
import numpy as np
import matplotlib.pyplot as plt 

img = cv2.imread("macos.jpg")
img = cv2.resize(img, (200, 200))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img_gray.shape)

# class bat dau bang chu in, khong co doi so
class Conv2d:
    # ham khoi tao
    def __init__(self, input, kernelSize):
        self.input = input 
        self.height, self.width = input.shape
        self.kernel = np.random.randn(kernelSize, kernelSize)
        # print(kernel)

        self.results = np.zeros((self.height - kernelSize + 1, self.width - kernelSize + 1))

    def getROI(self): # Lay vung du lieu quan tam 
        for row in range(self.height - self.kernel.shape[0] + 1):
            for col in range(self.width - self.kernel.shape[1] + 1):        
                roi = self.input[row : row + self.kernel.shape[0], col : col + self.kernel.shape[1]]
                yield row, col, roi
                # return toi la dung khong lien tuc duoc => yield 
    def operate(self):
        for row, col, roi in self.getROI():
            self.results[row, col] = np.sum(roi * self.kernel)
    
        return self.results

        # for row in range(height - kernelSize + 1):
        #     for col in range(width - kernelSize + 1):
        #         results[row, col] = np.sum(
        #             input[row : row + kernelSize, col : col + kernelSize] * kernel
        #         )
        # return results

conv2d = Conv2d(img_gray, 5)
img_gray_conv2d = conv2d.operate()

plt.imshow(img_gray_conv2d, cmap='gray')

plt.show()
