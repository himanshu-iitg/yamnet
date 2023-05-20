import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), '../soundpredictor/yamnet.h5')
CLASS_MAP_PATH = os.path.join(os.path.dirname(__file__), '../soundpredictor/yamnet_class_map.csv')
FS = 16000
HOP_SECONDS = 0.1
