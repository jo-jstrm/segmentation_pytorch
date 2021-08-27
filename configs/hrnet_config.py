from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from yacs.config import CfgNode as CN


config = CN()

config.NAME = 'hrnet_w48train_512x1024_sgd_lr1e-2_wd5e-4_bs_12_epoch484'
config.OUTPUT_DIR = 'outputs'
config.LOG_DIR = 'logs'


config.DATASET = CN()
config.DATASET.NAME = 'cityscapes'
config.DATASET.DATA_DIR = 'data/cityscapes'
config.DATASET.INPUT_PATTERN = '*_leftImg8bit.png'
config.DATASET.ANNOT_PATTERN = '*_gtFine_labelIds.png'
config.DATASET.IMAGE_DIR = 'leftImg8bit'
config.DATASET.LABEL_DIR = 'gtFine'
config.DATASET.NUM_CLASSES = 19
config.DATASET.IGNORE_LABEL = 255
config.DATASET.MEAN = [0.485, 0.456, 0.406]
config.DATASET.STD = [0.229, 0.224, 0.225]
config.DATASET.BASE_SIZE = (1024, 2048)
config.DATASET.CROP_SIZE = (512, 1024)

config.TRAIN = CN()
config.TRAIN.EPOCHS = 484
config.TRAIN.DECAY_STEPS = 120000
config.TRAIN.BATCH_SIZE = 12

config.TRAIN.BASE_LR = 1e-2
config.TRAIN.END_LR = 1e-5
config.TRAIN.OPTIMIZER = 'sgd'
config.TRAIN.WD = 0.0005
config.TRAIN.MOMENTUM = 0.9

config.MODEL = CN()
config.MODEL.NAME = 'hrnet_w48'
config.MODEL.PRETRAINED = 'weights/HRNet_W48_C_pretrained.pth'