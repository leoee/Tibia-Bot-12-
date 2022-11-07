import cv2

class PixelConfiguration:
  def count_pix_color(self, image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filtered_img = cv2.inRange(img_gray, 85, 100)
    gray_value = cv2.countNonZero(filtered_img)

    return gray_value