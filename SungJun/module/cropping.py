# !pip install pyyaml==5.1
# !pip install Pillow==5.3.0
# !pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.7/index.html

import torch, torchvision, cv2, detectron2
import numpy as np
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog

cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"))
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
cfg.MODEL.WEIGHTS = "/content/drive/MyDrive/Colab Notebooks/dl_project/model_final.pkl"

predictor = DefaultPredictor(cfg)
im = cv2.imread("/content/drive/MyDrive/Colab Notebooks/dl_project/room.jpg")
outputs = predictor(im)
n = 0

for cls, xy in zip(outputs["instances"].pred_classes, outputs["instances"].pred_boxes):
    obj = MetadataCatalog.get(cfg.DATASETS.TRAIN[0]).thing_classes[cls]
    if obj in ['chair', 'couch', 'clock']:
        n += 1
        xy = list(map(round, xy.tolist()))
        dst = im[xy[1]:xy[3], xy[0]:xy[2]].copy()
        cv2.imwrite("/content/drive/MyDrive/Colab Notebooks/dl_project/{}_{}.jpg".format(obj, n), dst)
