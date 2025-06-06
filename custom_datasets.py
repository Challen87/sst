from utils import open_file
import numpy as np

CUSTOM_DATASETS_CONFIG = {
    "DFC2018_HSI": {
        "img": "2018_IEEE_GRSS_DFC_HSI_TR.HDR",
        "gt": "2018_IEEE_GRSS_DFC_GT_TR.tif",
        "download": False,
        "loader": lambda folder: dfc2018_loader(folder),
    },
    #添加自己数据集
    "tomato": {
        "img": "tomato.mat",
        "gt": "tomato_label.mat",
        "download": False,
        "loader": lambda folder: tomato_loader(folder),
    }
}


def dfc2018_loader(folder):
    img = open_file(folder + "2018_IEEE_GRSS_DFC_HSI_TR.HDR")[:, :, :-2]
    gt = open_file(folder + "2018_IEEE_GRSS_DFC_GT_TR.tif")
    gt = gt.astype("uint8")

    rgb_bands = (47, 31, 15)

    label_values = [
        "Unclassified",
        "Healthy grass",
        "Stressed grass",
        "Artificial turf",
        "Evergreen trees",
        "Deciduous trees",
        "Bare earth",
        "Water",
        "Residential buildings",
        "Non-residential buildings",
        "Roads",
        "Sidewalks",
        "Crosswalks",
        "Major thoroughfares",
        "Highways",
        "Railways",
        "Paved parking lots",
        "Unpaved parking lots",
        "Cars",
        "Trains",
        "Stadium seats",
    ]
    ignored_labels = [0]
    palette = None
    return img, gt, rgb_bands, ignored_labels, label_values, palette

#添加自己的数据集
def tomato_loader(folder):
    # 加载高光谱影像和标签
    img = open_file(folder + "2311271-1img.mat")["image"]    # 路径和变量名请根据实际情况调整
    gt = open_file(folder + "2311271-1label.mat")["label"]
    rgb_bands = (13,30,55)  # 你可以指定3个可视化波段的索引，如(10, 20, 30)，否则用None
    label_values = [
        "background",   # 假设0为背景
        "leaf",
        "stem"
    ]
    ignored_labels = [0]  # 如果0是背景
    palette = None        # 可选：自定义可视化调色板
    return img, gt, rgb_bands, ignored_labels, label_values, palette
