# Object-Detection-FastAPI

## Installation

1. Install pypoetry

    [poetry link](https://python-poetry.org/docs/)

2. Pyproject.toml install

        $ poetry shell

        $ poetry install

3. Install requirements

        $ pip install torch==1.8.0+cpu torchvision==0.9.0+cpu torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html
        
        $ pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cpu/torch1.8.0/index.html

        $ pip install streamlit

        $ pip install python-multipart

4. Clone mmdetection github

        $ git clone https://github.com/open-mmlab/mmdetection.git

        $ cd mmdetection

        $ pip install -v -e .

5. Run Streamlit and FastAPI

        $ make -j 2 run_app