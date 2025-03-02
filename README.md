## Below is the script for our presentation for Codefest, but it can also double as a short description.
We know our recycling system isn't perfect, but you don't need to feel like a waste of space for trying to recycle! Our software B.A.G.S which stands for Basic Artificial Garbage Sorter is designed to detect plastic bags to help with sorting recycling to prevent the loss of reusable materials. We're using OpenCV as our API and YOLO for object detection, writing our backend in Python. Using our custom trained model, we were able to train our model to detect different types of plastic bags with confidence between 70 and 90 percent. With more time, we can improve detection with plastic bags and implement detection with other forms of non-recyclables, like bubble wrap and plastic straws.

### Website build instructions:

Options when building website:
* -i or --ip: IP address of the device (required) 
* -o or --port: Port number of the server (required)
* -f or --frame_count: # of frames used to construct the background model (default = 32)
* -m or --model: Model to use. Current options are katy_perry.pt and paty_kerry.pt. (default = katy_perry.pt)
* -b of --backend: Backend to use. Current options are cuda and cpu. (default is cuda if it is available, otherwise default to cpu)

Example: `python app.py --ip 0.0.0.0 --port 8000 -m paty_kerry.pt`

### Attributions

[OpenCV](https://opencv.org/) - © 2000-2025 OpenCV.org. Licensed under Apache-v2.0

[Ultralytics](https://github.com/ultralytics/ultralytics) - © 2023-2025 Ultralytics. Licensed under AGPL-v3.0
