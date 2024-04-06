import cv2
import json
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
import easyocr

# Global variables to store coordinates and labels
coordinates = []
labels = []

# Function to collect coordinates
def onselect(eclick, erelease):
    global coordinates
    coordinates.append((eclick.xdata, eclick.ydata, erelease.xdata, erelease.ydata))

# Function to get label from user
def get_label():
    return input("Enter label for the bounding box: ")

# Function to perform OCR on the specified region of interest (ROI)
def perform_ocr(image, coord):
    reader = easyocr.Reader(['en'])  # Initialize the OCR reader
    roi = image[int(coord[1]):int(coord[3]), int(coord[0]):int(coord[2])]  # Extract ROI
    result = reader.readtext(roi)  # Perform OCR on ROI
    text = " ".join([entry[1] for entry in result])  # Concatenate OCR results into a single string
    return text

def main():
    json_data = {}
    # Load the image file
    image_path = input("Enter the path to the image file: ")
    image = cv2.imread(image_path)

    # Prompt the user to enter field names
    print("Enter field names. Enter 'done' to finish.")
    while True:
        field = input("Enter field name: ")
        if field.lower() == 'done':
            break

        # Display the image with scrollbars
        fig, ax = plt.subplots()
        ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        def release(event):
            if event.key == 'enter':
                plt.close()
        rs = RectangleSelector(ax, onselect ,useblit=True,
                               button=[1], minspanx=5, minspany=5, spancoords='pixels')
        plt.connect('key_release_event', release)
        plt.show()

        # Get label for each bounding box
        global labels
        labels = [get_label() for _ in range(len(coordinates))]

        # Create JSON structure
        json_data[field] = []
        for coord, label in zip(coordinates, labels):
            # Extract text using OCR
            text = perform_ocr(image, coord)
            json_data[field].append({
                "coordinates": list(map(int,coord)),
                "label": label,
                "text": text
            })

        coordinates.clear()

    # Save the data to a JSON file
    output_file = "bounding_boxes.json"
    with open(output_file, "a") as f:
        json.dump(json_data, f, indent=4)
        f.write("\n")  # Separate each field's data
    print(f"Data for field '{field}' saved to:", output_file)

if __name__ == "__main__":
    main()
