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



## Usage

```shell
usage: mlnem [-h] [-p PATH] [-u URL] [-o OUTPUT] [-V] [-d] [-t]

yolo network implementation in a ready-to-use python app.

optional arguments:
  -h, --help            		  show this help message and exit
  -p PATH, --path PATH  		  Path to image/video file
  -u URL, --url URL     		  A url of a video stream to pass to the network
  -o OUTPUT, --output OUTPUT              Write network result(s) as image/video to specified path
  -V, --version         		  Show current version
  -d, --debug           		  Set logging level to debug
  -t, --use-tiny        		  Use tiny-yolo instead of full-yolo network
```



## Author

*MLNEM* was made by [Majd Alfhaily](https://github.com/freemanrepo) and the AI-on-Mobile team as part of the first semester project for [CODE Unverisity](http://code.berlin).



## License

This project is licensed under the terms of the GNU General Public License v3.0.
