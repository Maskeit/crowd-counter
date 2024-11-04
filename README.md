# Crowd-Counter

Crowd counter is a system that uses Ultralitycs YOLOv8 model for object detection, these objects are counted and published to a broker as a topic.
Then with an API with Flask you can subscribe to this topic and view the data, in addition to storing it in an SQLite database.

## Create a new venv

<pre><code>python -m venv /path/to/new/virtual/name_of_my_environment</code></pre>

## Activate virtual env

<pre><code>source name_of_my_environment/bin/activate</pre></code>

## Install dependencies from requirements.txt

<pre><code>pip install requirements.txt</code></pre>

## Activate software

python3 main.py or ./dist/main for executable

## View Details with `yolo checks`:

- **Ultralytics YOLOv8.2.63 🚀**
- **Python**: 3.12.6
- **torch**: 2.4.0
- **Environment**: CPU (Apple M1)
- **OS**: macOS-15.0-arm64-arm-64bit
- **Python Environment**: Darwin
- **Install method**: git
- **RAM**: 8.00 GB
- **CPU**: Apple M1
    **Installed Packages**:
- numpy: ✅ 1.26.4 (version compatible)
- matplotlib: ✅ 3.9.1 (version compatible)
- opencv-python: ✅ 4.10.0.84 (version compatible)
- pillow: ✅ 10.4.0 (version compatible)
- pyyaml: ✅ 6.0.1 (version compatible)
- requests: ✅ 2.32.3 (version compatible)
- scipy: ✅ 1.14.0 (version compatible)
- torch: ✅ 2.4.0 (version compatible)
- torchvision: ✅ 0.19.0 (version compatible)
- tqdm: ✅ 4.66.4 (version compatible)
- psutil: ✅ 6.0.0
- py-cpuinfo: ✅ 9.0.0
- pandas: ✅ 2.2.2 (version compatible)
- seaborn: ✅ 0.13.2 (version compatible)
- ultralytics-thop: ✅ 2.0.0 (version compatible)

Everything appears to be set up correctly for running YOLOv8.
