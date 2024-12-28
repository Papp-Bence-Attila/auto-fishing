import cv2
import numpy
import pyautogui
import time
import pytesseract
import PIL
import keyboard

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"
run = True

def right_click():
    pyautogui.mouseDown(button='right')
    time.sleep(0.1)
    pyautogui.mouseUp(button='right')

def main():
    global run
    while run:
        # if "minecraft" in str(pyautogui.getActiveWindowTitle()).lower():
        img = PIL.ImageGrab.grab(bbox=(1650, 920, 1914, 960))
        
        np_img = numpy.array(img)
        cv2.imshow("normal", np_img)

        # idk wtf is here but it just work it just works over priced...
        grey_scale = cv2.cvtColor(np_img, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("grey scale", grey_scale)
        thresh1 = cv2.threshold(grey_scale, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
        dilation = cv2.dilate(thresh1[1], rect_kernel, iterations = 1)
        contours = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        im2 = np_img
        for cnt in contours[0]:
            x, y, w, h = cv2.boundingRect(cnt)
            cropped = im2[y:y + h, x:x + w]
            text = pytesseract.image_to_string(cropped)
            if "Fishing Bobber splashes" in text:
                right_click()
                time.sleep(3)
                right_click()
        key = cv2.waitKey(20)
        if key == 27 or keyboard.is_pressed("k"):
            run = False

    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()
