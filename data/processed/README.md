# Study data

In diesem Ordner liegen die finalen Trainings- Test- und Validierungsdaten. Die Daten liegen im YOLO-Format vor (Bilder + Labels + YAML-Dateien).  

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

Die Daten können hier heruntergeladen werden: https://drive.google.com/drive/folders/1pw_nrsHszTiF70gPaf-rnBl7g_RudiFZ?usp=sharing
