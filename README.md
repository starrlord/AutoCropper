# AutoCropper

AutoCropper is a Python script that automatically detects and crops faces from images in a specified input directory and saves the cropped faces to an output directory. It utilizes the OpenCV library and a pre-trained face detection model to accurately locate and extract faces from the images.

## Features

- Detects and crops faces from images
- Supports various image formats (JPG, JPEG, PNG, BMP, TIFF)
- Adjustable crop region expansion factor
- Progress bar to track the processing of images
- Command line arguments for input directory, output directory, and expansion factor

## Prerequisites

- Python 3.x
- OpenCV
- NumPy
- tqdm
- argparse

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/AutoCropper.git
   cd AutoCropper
   ```

2. Create a virtual environment (optional but recommended):

   - For Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```

   - For Linux/Mac:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install the required packages:

   ```
   pip install opencv-python numpy tqdm argparse
   ```

## Usage

1. Place the images you want to process in the input directory.

2. Run the script with the desired command line arguments:

   ```
   python autocropper.py --input_dir path/to/input/directory --output_dir path/to/output/directory [--expand_factor 0.3]
   ```

   - `--input_dir`: Path to the input directory containing the images (required).
   - `--output_dir`: Path to the output directory where the cropped faces will be saved (required).
   - `--expand_factor`: Factor by which to expand the crop region (optional, default: 0.3).

3. The script will process the images, detect faces, crop them, and save the cropped faces to the output directory.

## Example

```
python autocropper.py --input_dir D:\images\input --output_dir D:\images\output --expand_factor 0.5
```

This command will process the images in the `D:\images\input` directory, crop the detected faces with an expansion factor of 0.5, and save the cropped faces to the `D:\images\output` directory.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The face detection model used in this script is based on the Caffe framework and the pre-trained model provided by OpenCV.
- The script utilizes the OpenCV library for image processing and face detection.

Feel free to contribute to this project by submitting pull requests or reporting issues on the GitHub repository.