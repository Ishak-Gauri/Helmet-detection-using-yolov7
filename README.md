# Helmet-detection-using-yolov7
Deep Learning Project to detect whether a person is wearing a Helmet or not in an Image using two websites Roboflow and Googlecolab and implementing yolov7 on roboflow website.using pycharm to run the project by fetching api key from roboflow website.i have provided the google collab as helmet detection.ipynb and the link of the dataset i have used is extracted from kaggle here's the link https://www.kaggle.com/datasets/andrewmvd/helmet-detection and i have also added the python folder used in pycharm as Helmet detection folder and the python file as helmet detection .py file .you have to add a 
jpg file instead of the current jpg file or replace it with the jpg file inside your pycharm folder 
# infer on a local image
print(model.predict("000083_jpg.rf.cb7a594501b4c44e2069aa15212024c4.jpg", confidence=40, overlap=30).json())

# visualize your prediction
model.predict("000083_jpg.rf.cb7a594501b4c44e2069aa15212024c4.jpg", confidence=40, overlap=30).save("prediction.jpg")

then the predicted output will be saved in predection.jpg file which is also uploaded




