# python autocrop.py --input_dir d:\development\AutoCropper\input\ --output_dir D:\development\AutoCropper\output\ --expand_factor 0.5
import cv2
import os
import numpy as np
import argparse
from tqdm import tqdm

def detect_and_crop_faces(image_path, output_dir, expand_factor=0.3):
    # Load the pre-trained face detection model
    face_detector = cv2.dnn.readNetFromCaffe("deploy.prototxt", "res10_300x300_ssd_iter_140000.caffemodel")

    # Load the input image
    image = cv2.imread(image_path)

    # Get the image dimensions
    (h, w) = image.shape[:2]

    # Construct an input blob for the image
    image_blob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)), 1.0, (300, 300),
        (104.0, 177.0, 123.0), swapRB=False, crop=False)

    # Apply face detection
    face_detector.setInput(image_blob)
    detections = face_detector.forward()

    # Process each detected face
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        # Filter out weak detections
        if confidence > 0.5:
            # Compute the (x, y)-coordinates of the bounding box for the face
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # Expand the bounding box coordinates
            expandX = int((endX - startX) * expand_factor)
            expandY = int((endY - startY) * expand_factor)
            startX = max(0, startX - expandX)
            startY = max(0, startY - expandY)
            endX = min(w, endX + expandX)
            endY = min(h, endY + expandY)

            # Extract the expanded face ROI
            face = image[startY:endY, startX:endX]

            # Check if the face is empty
            if face.size == 0:
                print(f"Skipping empty face detection for {os.path.basename(image_path)}")
                continue

            # Save the cropped face to a file
            output_path = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(image_path))[0]}_face_{i}.jpg")
            cv2.imwrite(output_path, face)

def process_images(input_dir, output_dir, expand_factor=0.3):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Get a list of all image files in the input directory
    image_files = [file for file in os.listdir(input_dir) if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff'))]
    total_images = len(image_files)
    print(f"Total images loaded: {total_images}")

    # Process each image file with a progress bar
    with tqdm(total=total_images, desc="Processing images", unit="image") as pbar:
        for filename in image_files:
            image_path = os.path.join(input_dir, filename)
            detect_and_crop_faces(image_path, output_dir, expand_factor)
            pbar.update(1)

# Parse command line arguments
parser = argparse.ArgumentParser(description='Detect and crop faces from images.')
parser.add_argument('--input_dir', type=str, required=True, help='Path to the input directory containing images.')
parser.add_argument('--output_dir', type=str, required=True, help='Path to the output directory for saving cropped faces.')
parser.add_argument('--expand_factor', type=float, default=0.3, help='Factor by which to expand the crop region.')
args = parser.parse_args()

# Process the images
process_images(args.input_dir, args.output_dir, args.expand_factor)