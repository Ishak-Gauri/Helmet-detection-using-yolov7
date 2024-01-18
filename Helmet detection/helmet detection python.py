from roboflow import Roboflow

rf = Roboflow(api_key="add your api key from roboflow website")
project = rf.workspace().project("helmet-detecetion")
model = project.version(1).model

# infer on a local image
print(model.predict("000083_jpg.rf.cb7a594501b4c44e2069aa15212024c4.jpg", confidence=40, overlap=30).json())

# visualize your prediction
model.predict("000083_jpg.rf.cb7a594501b4c44e2069aa15212024c4.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
