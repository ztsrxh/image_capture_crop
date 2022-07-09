# MIT License

# Copyright (c) 2022 Tong Zhao

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
    - this script crops the original image(size: 1080*1920) into patches(size: 360*240)
    - 'corner_points' are the (x, y) coordinates of the left-up point for each patch
    - the given 'corner_points' below is just an example
    - the obtained image patches containing only the road surface area are then annotated manually
'''

import os
import cv2
import datetime
import time

image_dir = './image'
save_path = './image_cropped/'

corner_points = [            [600, 1],   [840, 1],   [1080, 1],
                 [360, 361], [600, 361], [840, 361], [1080, 361], [1320, 361],
                 [360, 721], [600, 721], [840, 721], [1080, 721], [1320, 721]]


file_list = os.listdir(image_dir)

save_index = 1

for file_name in file_list:
    if '.jpg' in file_name:
        image = cv2.imread(image_dir + file_name)
        for i in range(len(corner_points)):
            y = corner_points[i, 1]
            x = corner_points[i, 0]
            im_crop = image[y : y + 360, x : x + 240, :]

            save_name = save_path + time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time())) + str(save_index) + '.jpg'
            cv2.imwrite(save_name, im_crop)
            save_index += 1
