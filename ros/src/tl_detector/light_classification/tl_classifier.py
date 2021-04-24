from styx_msgs.msg import TrafficLight
import cv2
import numpy as np

class TLClassifier(object):
    def __init__(self):
        pass

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        img_blur = cv2.medianBlur(image,3)
        img_hsv = cv2.cvtColor(img_blur,cv2.COLOR_BGR2HSV)

        red_lower_range = cv2.inRange(hsv_image, np.array([0, 100, 100],np.uint8), np.array([10, 255, 255],np.uint8))
        red_upper_range = cv2.inRange(hsv_image, np.array([160, 100, 100],np.uint8), np.array([179, 255, 255],np.uint8))
        yellow_range = cv2.inRange(hsv_image, np.array([28, 120, 120],np.uint8), np.array([47, 255, 255],np.uint8))

        if cv2.countNonZero(red_lower_range) + cv2.countNonZero(red_upper_range) > 48 or cv2.countNonZero(yellow_range) > 48:
            return TrafficLight.RED
        else:
            return TrafficLight.GREEN

        # return TrafficLight.UNKNOWN
