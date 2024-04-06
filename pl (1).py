import cv2
import json
import matplotlib.pyplot as plt
data = json.load(open('./bounding_boxes.json', 'r'))
img = cv2.imread('images/filled_form_1.jpg')


for i in data.keys():
    img = cv2.rectangle(img, data[i][0]['coordinates'][:2], data[i][0]['coordinates'][2:], color=(255, 0, 0), thickness=2)
    img = cv2.rectangle(img, data[i][1]['coordinates'][:2], data[i][1]['coordinates'][2:], color=(0, 255, 0), thickness=2)

fig, ax = plt.subplots()
ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
