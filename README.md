# MLNEM-Python

This is a python implementation of Yolo and Tiny-Yolo that uses [darkflow](https://github.com/thtrieu/darkflow)'s tensorflow implementation to make it easier to use and integrate with other apps and services.



## Sample Video

[![MLNEM Sample](https://img.youtube.com/vi/Z7j2CJb1BBc/0.jpg)](https://www.youtube.com/watch?v=Z7j2CJb1BBc)



## Name

*MLNEM* stands for "Man lebt nur einmal" in German, which is the equivelant of Yolo in English.



## Requirements

* Python 3
* pip3
* git
* MediaInfo



## Installation

```bash
pip3 install Cython
git clone --recurse-submodules https://github.com/freemanrepo/mlnem-python
cd mlnem-python
pip3 install -r requirements.txt
python3 setup.py install
```

After installing MLNEM with the instructions above, you need to download the following file from [here](http://cloud.alfhaily.me/qY0T) and extract the bin folder to the *mlnem-python* directory.


## Usage

```shell
usage: mlnem [-h] [-p PATH] [-u URL] [-o OUTPUT] [-V] [-d] [-t]

yolo network implementation in a ready-to-use python app.

optional arguments:
  -h, --help            		  show this help message and exit
  -p PATH, --path PATH  		  path to image/video file
  -u URL, --url URL     		  url of a video stream to pass to the network
  -o OUTPUT, --output OUTPUT              write network result(s) as image/video to specified path
  -V, --version         		  show current version
  -d, --debug           		  set logging level to debug
  -t, --use-tiny        		  use tiny-yolo instead of full-yolo network
```



## Author

*MLNEM* was made by [Majd Alfhaily](https://github.com/freemanrepo) and the AI-on-Mobile team as part of the first semester project for [CODE Unverisity](http://code.berlin).



## License

This project is licensed under the terms of the GNU General Public License v3.0.
