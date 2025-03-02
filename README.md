## Below is the script for our presentation for Codefest, but it can also double as a short description.
We know our recycling system isn't perfect, but you don't need to feel like a waste of space for trying to recycle! Our software B.A.G.S which stands for Basic Artificial Garbage Sorter is designed to detect plastic bags to help with sorting recycling to prevent the loss of reusable materials. We're using OpenCV as our API and YOLO for object detection, writing our backend in Python.

### Website build instructions:

Options when building website:
* -i or --ip: IP address of the device (required) 
* -o or --port: Port number of the server (required)
* -f or --frame_count: # of frames used to construct the background model (default = 32)
* -m or --model: Model to use. Current options are katy_perry.pt and paty_kerry.pt. (default = katy_perry.pt)

Example: `python app.py --ip 0.0.0.0 --port 8000 -m paty_kerry.pt`