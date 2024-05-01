FROM ros:noetic
SHELL ["/bin/bash", "-c"]
RUN apt-get update && apt-get install python3-virtualenv -y \
    && virtualenv sisyphus_env  \
    && source /sisyphus_env/bin/activate \
    && pip install opencv-python numpy imutils
