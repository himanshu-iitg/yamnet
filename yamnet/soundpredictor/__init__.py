import os
import sys

sys.path.append(os.path.dirname(__file__))

import time

from yamnet.config.constants import MODEL_PATH, CLASS_MAP_PATH, FS, HOP_SECONDS
from yamnet.soundpredictor import params as yamnet_params, yamnet_model

x = time.time()
params = yamnet_params.Params(sample_rate=FS, patch_hop_seconds=HOP_SECONDS)
class_names = yamnet_model.class_names(CLASS_MAP_PATH)
yamnet_predictor = yamnet_model.yamnet_frames_model(params)
yamnet_predictor.load_weights(MODEL_PATH)

print('time taken to load', time.time() - x)