import torch, torchvision
assert torch.__version__.startswith("1.7")
import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()
import numpy as np
import cv2
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog

cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"))
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
cfg.MODEL.WEIGHTS = "model_final.pkl"

predictor = DefaultPredictor(cfg)
im = cv2.imread("pics/input.jpg")
outputs = predictor(im)

for cls, xy in zip(outputs["instances"].pred_classes, outputs["instances"].pred_boxes):
    if cls == 56:
        xy = list(map(round, xy.tolist()))
        dst = im[xy[1]:xy[3], xy[0]:xy[2]].copy()
        obj = MetadataCatalog.get(cfg.DATASETS.TRAIN[0]).thing_classes[cls]
        cv2.imwrite("pics/input.jpg".format(obj), dst)
