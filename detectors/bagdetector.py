import numpy as np
import imutils
from ultralytics import YOLO
import cv2
class BagDetector:
	
	def __init__(self, model, accumWeight=0.5):
		# store the accumulated weight factor
		self.accumWeight = accumWeight
		# initialize the background model
		self.bg = None   
		self.yolo = YOLO(model)

	def update(self, image):
		# if the background model is None, initialize it
		if self.bg is None:
			self.bg = image.copy().astype("float")
			return
		# update the background model by accumulating the weighted
		# average
		cv2.accumulateWeighted(image, self.bg, self.accumWeight)

	def detect(self, image):
		return self.yolo.track(image, stream=True) 
	# Function to get class colors
	def getColours(self, cls_num):
		base_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
		color_index = cls_num % len(base_colors)
		increments = [(1, -2, 1), (-2, 1, -1), (1, -1, 2)]
		color = [base_colors[color_index][i] + increments[color_index][i] * 
		(cls_num // len(base_colors)) % 256 for i in range(3)]
		return tuple(color)