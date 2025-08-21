# Study data

In diesem Ordner liegen die **finalen Trainings-, Test- und Validierungsdaten**.  
Die Daten wurden in **CVAT** annotiert/segmentiert und anschließend in **Bilder und Labels** exportiert.  
Diese Bilder und Labels wurden in Trainings-, Validierungs- und Testdatensätze aufgeteilt.  

Die Daten liegen im **YOLO-Format** vor (Bilder + Labels + YAML-Dateien).  

Die Struktur ist wie folgt:

images
|---train
|---val

labels
|---train
|---val

test
|--images
  |---train
  |---val
|--labels
  |---train
  |---val

|--- data.yaml # YAML-Datei für Training (enthält Klassen & Pfade)
|...data_test.yaml # YAML-Datei für Test 

