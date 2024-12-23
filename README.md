# Object-Detection-with-Beverages
This is a term project conducted in team of Machine Learning Course in NTHU.

# Result Reproduction & Prediction
You can reference the training model to generate the predicting result by the following directory path: ./runs/detect/train9 to predict the images and videos as well. 

The venv environment in python used here is not uploaded here due to the file size limit(exceeding the 2GB limit of Github).

For example, you can run the following command to train and predict using the training model:

**yolo detect train data=datasets/labeled_images/data.yaml model = yolo11n.pt epochs=30 imgsz=640**  
**yolo predict source=datasets/test model = runs/detect/train9/weights/best.pt data=datasets/labeled_images/data.yaml**


# Detection Details:
## Image Detection
![alt text](timeline_20241125_205718.jpg)
![alt text](7B01B6C8-9F92-43E2-A64F-5E3311BC1EC5.jpg)
![alt text](03AC45C6-175C-4B68-BF78-0C35FA5F4878.jpg)

## Video Detection Screenshot
![alt text](image.png)
![alt text](image-1.png)

## Number of Classes: 26
names: ['ChaLiWong_BlackTea', 'ChaLiWong_BritainBlackTea', 'ChaLiWong_TsingXinOolong', 'ChaLiWong_WhiteOolong', 'Known_ChocoMilkTea', 'Known_MilkGreenTea', 'Known_MilkTea', 'MeiChou_BlackTea', 'MeiChou_GreenTea', 'RiYue_BlackTea', 'RuiSui_AppleMilk', 'RuiSui_ChocoMilk', 'RuiSui_MaltedMilk', 'RuiSui_Milk', 'TongYi_LowSugarHighFiberSoyMilk', 'TongYi_SoyMilk', 'TongYi_UnsweetenedBlackSoyMilk', 'TongYi_UnsweetenedHighFiberSoyMilk', 'YinBinShi_MilkGreenTea', 'YinBinShi_MilkTea', 'YinBinShi_WuLongMilkTea', 'YuanTsui_BlackTea', 'YuanTsui_GreenTea', 'YuanTsui_MeiRen', 'YuanTsui_TieGuanYing', 'ZaoTsan_BlackTea']

## Roboflow Website Related:
  workspace: personal-workspace-kusbp
  project: nthu-final-project-beveragedetec
  version: 6
  license: CC BY 4.0
  url: https://universe.roboflow.com/personal-workspace-kusbp/nthu-final-project-beveragedetec/dataset/6
