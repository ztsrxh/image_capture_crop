# MIT License

# Copyright (c) 2022 ztsrxh

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

'''
    - this script captures and saves the images

'''

import cv2
import datetime
import time

# open the USB camera
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

save_index = 0
try:
    while True:
        # sleep for 180ms, 5 frames are collected per second
        time.sleep(0.18)
        # get one frame
        ret, img = cap.read()

        curr_time = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        save_index += 1
        name = curr_time + '-' + str(save_index) + ".jpg"
        cv2.imwrite(name, img, [cv2.IMWRITE_JPEG_QUALITY, 80])
except KeyboardInterrupt:
    cap.release()
