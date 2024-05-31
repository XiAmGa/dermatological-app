import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import imgaug.augmenters as iaa
from sklearn import svm
import joblib

seq = iaa.Sequential(
    [
        iaa.Fliplr(0.5),
        iaa.Affine(rotate=(-30, 30)),
        iaa.GaussianBlur(sigma=(0, 2.0)),
        iaa.AdditiveGaussianNoise(scale=(0, 0.05 * 255)),
    ]
)

image_data = []
labels = []

disease_folders = ["PSORIASIS", "ROSACEA", "SARPULLIDO", "VITILIGIO"]
for i, folder in enumerate(disease_folders):
    for filename in os.listdir("./DATA_SET/" + folder):
        img = cv2.imread(os.path.join("DATA_SET", folder, filename))
        img = cv2.resize(img, (256, 256))
        augmented_images = []
        for _ in range(10):
            augmented_image = seq.augment_image(img)
            flattened_image = augmented_image.reshape(-1)
            augmented_images.append(flattened_image)
        image_data.extend(augmented_images)
        labels.extend([i] * len(augmented_images))

image_data = np.array(image_data)
labels = np.array(labels)

X_train, X_test, y_train, y_test = train_test_split(
    image_data, labels, test_size=0.2, random_state=42
)

svm_model = svm.SVC(kernel="linear", C=1)
svm_model.fit(X_train, y_train)

y_pred = svm_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy}")

model_filename = "svm_model.joblib"
joblib.dump(svm_model, model_filename)

print(f"Modelo SVM guardado en {model_filename}")
