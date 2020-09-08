# Odin

#### 3161's scouting app "server" for collating data collected by Muninn


## Installation / Setup

### Create A Virtual Environment

Make sure you use python 3.7, as OpenCV does not support 3.8 yet
`python -m venv <virtualenv name>`

### Install the Dependencies

On Windows:
`pip install -r requirements_windows.txt`

Otherwise:
`pip install -r requirements.txt`

Coming Soon: a script that installs the correct dependencies based on the platform you're using

## Usage 
To run the script, switch to the virutal environment you created and run `python main.py`

### Arguments
Currently, the only argument supported is `--image`, to scan a code from an image. It's usage is as follows:
```
python main.py -- --image <image_name>
```

The `--` at the beginning is important because Kivy will intercept the args otherwise
