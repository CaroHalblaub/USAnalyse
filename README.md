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



## Usage
1. Daten vorbereiten  
   Die Rohdaten (Videos) werden im Ordner /USVideos abgelegt.

2. Frames extrahieren  
   Mit dem Skript frames.py können einzelne Frames aus Videos extrahiert und für die Annotation        genutzt werden. Speichern unter dataset/images/train, dataset/images/val und dataset/test/images.

3. Bilder segmentieren  
   Mithilfe eines geeigneten Programms (z.B. CVAT) Bilder segmentieren und in dataset/labels/train,    dataset/labels/val und dataset/test/labels speichern. 

5. Training starten und Evaluation  
   Das skript us_segmentierung.py öffnen.
   
   

## Konfigurationsparameter

```python
# Trainingsparameter
epochs = 200
imgsz = 640
overlap_mask = False
mask_ratio = 1
batch = 32
patience = 200
aug = strong_aug / weak_aug / no_aug

# Strong Augmentation
strong_aug = {
    "dropout": 0.4,
    "hsv_h": 0,
    "hsv_s": 0,
    "hsv_v": 0.5,
    "degrees": 30.0,
    "translate": 0.1,
    "scale": 0.3,
    "shear": 5,
    "perspective": 0.0001,
    "flipud": 0.5,
    "fliplr": 0.7,
    "bgr": 0,
    "mosaic": 0,
    "mixup": 0,
    "cutmix": 0,
    "erasing": 0,
}

# No Augmentation
no_aug = {
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
}

# Weak Augmentation
weak_aug = {
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
}
