from typing import List, Dict, Any
import torch
from ultralytics import YOLO
from PIL import Image
import streamlit as st

class ObjectDetector:
    """YOLOv8 based object detection class."""
    
    def __init__(self, model_path: str = 'yolov8x.pt', confidence_threshold: float = 0.5):
        """
        Initialize the object detector.
        
        Args:
            model_path: Path to the YOLO model weights
            confidence_threshold: Minimum confidence score for detections
        """
        self.confidence_threshold = confidence_threshold
        self.model = self._load_model(model_path)
    
    @staticmethod
    @st.cache_resource
    def _load_model(model_path: str) -> YOLO:
        """Load the YOLO model with caching."""
        return YOLO(model_path)
    
    def detect_objects(self, image: Image.Image) -> List[Dict[str, Any]]:
        """
        Detect objects in the given image.
        
        Args:
            image: PIL Image object
            
        Returns:
            List of dictionaries containing detection results
        """
        results = self.model(image)
        detected_objects = []
        
        for r in results:
            for box in r.boxes:
                confidence = float(box.conf)
                if confidence > self.confidence_threshold:
                    obj = {
                        'class': self.model.names[int(box.cls)],
                        'confidence': confidence,
                        'bbox': box.xyxy[0].tolist()
                    }
                    detected_objects.append(obj)
        
        return detected_objects