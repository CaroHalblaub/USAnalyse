## Ultraschall zur automatischen Erkennung submentaler Muskeln und Bestimmung der Morphologie mittels KI
Das Projekt wurde mit der Intention entwickelt, ein Modell zur Bildsegmentierung zu erstellen, das die relevanten Strukturen im submentalen Bereich identifizieren kann.
Im Fokus stehen insbesondere die beiden Muskeln Musculus digastricus und Musculus geniohyoideus, deren automatische Detektion und morphologische Analyse mithilfe von Künstlicher Intelligenz unterstützt werden soll. Ziel ist es, durch die Kombination von Ultraschallaufnahmen und modernen Segmentierungsverfahren eine reproduzierbare, effiziente und objektive Auswertung der Muskelstrukturen zu ermöglichen.

YOLO Medical Segmentation: Dieses Projekt nutzt YOLOv8/YOLO11 für die Segmentierung medizinischer Bilder. Es umfasst Training, Validierung, Berechnung der IoU-Metrik und Inferenz auf Bildern und Videos.


## Installation

> Put your installation instructions here. This should include versions of all Programs and Tools used. The following example is for a python project with name `project_name`.

Getestet mit Python 3.9.
Wir empfehlen das virtuelles Environment venv.

```
git clone <repo>

cd <repo>

python -m venv .venv

Aktivieren (Windows PowerShell)
.venv\Scripts\activate

Abhängigkeiten installieren
pip install --upgrade pip
pip install -r requirements.txt
```

Beispiel für requirements.txt
ultralytics>=8.0.0
opencv-python
numpy
tqdm
pandas
matplotlib

Vorgefertigtes medizinisches Modell herunterladen:
wget https://github.com/sevdaimany/YOLOv8-Medical-Imaging/raw/master/runs/segment/train/weights/best.pt -O yolov8n-medicalImaging.pt

## Usage

> Put instructions on how to use your project code here. Best practice is to prepare a separate scripts for generating data and another script that creates plots and visualizations


## Konfigurationsparameter
    epochs=200,
    imgsz=640,
    overlap_mask=False,
    mask_ratio=1,
    batch=32,
    patience=200,
    **strong_aug/weak_aug/no_aug


    strong_aug = 
    "dropout": 0.4, #Dropout rate for regularization in classification tasks, preventing overfitting by randomly omitting units during training.
    "hsv_h": 0, #Adjusts the hue of the image
    "hsv_s": 0, #Alters the saturation of the image
    "hsv_v": 0.5, # Modifies the value (brightness) of the image
    "degrees": 30.0, # 30 Rotates the image randomly within the specified degree range
    "translate": 0.1, #Translates the image horizontally and vertically by a fraction of the image size
    "scale": 0.3, #Scales the image by a gain factor
    "shear": 5, #Shears the image by a specified degree
    "perspective": 0.0001, #Applies a random perspective transformation to the image
    "flipud": 0.5, #Flips the image upside down with the specified probability
    "fliplr": 0.7, # 0.5Flips the image left to right with the specified probability
    "bgr": 0, #Flips the image channels from RGB to BGR
    "mosaic": 0, #Combines four training images into one, simulating different scene compositions and object interactions. Highly effective for complex scene understanding.
    "mixup": 0, #Blends two images and their labels, creating a composite image. Enhances the model's ability to generalize by introducing label noise and visual variability.
    "cutmix": 0, #Combines portions of two images, creating a partial blend while maintaining distinct regions. Enhances model robustness by creating occlusion scenarios.
    "erasing": 0, #Classification only. Randomly erases regions of the image during training to encourage the model to focus on less obvious features.


no_aug = 
    "dropout": 0,
    "hsv_h": 0,
    "hsv_s": 0,
    "hsv_v": 0,
    "degrees": 0.0,
    "translate": 0.0,
    "scale": 0.0,
    "shear": 0,
    "perspective": 0,
    "flipud": 0.0,
    "fliplr": 0.0,
    "bgr": 0,
    "mosaic": 0,
    "mixup": 0,
    "cutmix": 0,
    "erasing": 0,


weak_aug = 
    "dropout": 0.2,
    "hsv_h": 0,
    "hsv_s": 0,
    "hsv_v": 0.1,
    "degrees": 10.0,
    "translate": 0.05,
    "scale": 0.3,
    "shear": 0,
    "perspective": 0,
    "flipud": 0,
    "fliplr": 0.5,
    "bgr": 0,
    "mosaic": 0,
    "mixup": 0,
    "cutmix": 0,
    "erasing": 0,
