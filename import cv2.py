import cv2
import os

image_folder = "path/to/images"

video_name = "video_album.avi"

images = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]

frame_width = 640
frame_height = 480

video = cv2.VideoWriter(video_name, 0, 30, (frame_width, frame_height))

image_index = 0

while image_index < 10:
    image = cv2.imread(os.path.join(image_folder, images[image_index]))

    image = cv2.resize(image, (frame_width, frame_height))

    video.write(image)

    image_index += 1

video.release()

cv2.destroyAllWindows()