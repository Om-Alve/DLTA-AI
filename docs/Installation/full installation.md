---
label: full installation ⚡
order: 3
---

# Full Installation
## Create a Virtual Environment
It is highly recommended to install DTLA-AI within a virtual environment using conda. This will ensure a clean and isolated environment for the installation process. use `python=3.8`
```
conda create -n DLTA-AI python=3.8
conda activate DLTA-AI
```


## Install Pytorch

install [pytorch](https://pytorch.org/get-started/locally/) according to your device and your OS, if you have GPU, choose CUDA version, otherwise choose CPU version

Example:
```
conda install pytorch torchvision torchaudio .... -c pytorch>
```

## 1. Using pip
```
pip install DLTA-AI
```
then run it from anywhere using
```
DLTA-AI
```
note that first time running DLTA-AI, it will download a required module, it may take some time

### Update

```
pip install DLTA-AI -U
```

## 2. Manual Installation
Download the lastest release from [here](https://github.com/0ssamaak0/DLTA-AI/releases)

install requirements

```
pip install -r requirements.txt
mim install mmcv-full==1.7.0
```
then 
Run the tool from `DLTA_AI_app` directory
```
cd DLTA_AI_app
python __main__.py
```





