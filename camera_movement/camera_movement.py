import pickle
import cv2
import numpy as np
import os
import sys 
sys.path.append('../')
from utils import measure_distance,measure_xy_distance

class CameraMovementEstimator():
    def __init__(self, frame):
        self.minimum_distance = 5
        
        self.lk_params = dict(
            winSize = (15,15),
            maxLavel = 2,
            criteria = (cv2.TermCriteria_EPS | cv2.TERM_CRITERIA_COUNT, 10,0.03)
            
        )
        first_frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BayerGR2GRAY)
        mask_features = np.zeros_like(first_frame_grayscale)
        mask_features[:,0:20] = 1
        mask_features[:,900:1050] = 1
        
        self.features = dict(
            maxCorners = 100,
            qualityLevel = 0.3,
            minDistance = 3,
            blockSize = 7,
            mask = mask_features
        )
        
    def add_adjust_positions_to_tracks(slef, tracks, camera_movement_per_frame):
        for object, object_tracks in tracks.items():
            for frame_num, track in enumerate(object_tracks):
                for track_id, track_info in tracks.items():
                    position = track_info['position']
                    camera_movement = camera_movement_per_frame[frame_num]
                    position_adjusted = (position[0] - camera_movement[0], position[1] - camera_movement[1])
                    tracks[object][frame_num][track_id]['position_adjusted'] = position_adjusted
                    
                    
    def get_camera_movement(self, frames, read_from_stub = False, stub_path = None):
        if read_from_stub and stub_path is not None and os.path.exists(stub_path):
            with open(stub_path, 'rb') as f:
                return pickle.loads
        