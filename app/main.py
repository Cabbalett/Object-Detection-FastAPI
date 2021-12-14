from fastapi import FastAPI, UploadFile, File
from fastapi.param_functions import Depends
from fastapi.responses import FileResponse, Response
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import List, Union, Optional, Dict, Any
import uvicorn
from datetime import datetime
from starlette.responses import StreamingResponse
import io
import sys

from mmdet.apis import init_detector, inference_detector

from PIL import Image
import cv2
import numpy as np
from fastapi.encoders import jsonable_encoder
import json
import base64


app = FastAPI()

orders = []


@app.get("/")
def hello_world():
    return {"hello": "world"}


@app.post("/order", description="주문을 요청합니다")
async def make_order(files: List[UploadFile] = File(...)):
    config_file = './mmdetection/configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
    checkpoint_file = 'faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
    model = init_detector(config_file, checkpoint_file, device='cpu')
    for file in files:
        print("hello")
        image_bytes = await file.read()
        image_test = Image.open(io.BytesIO(image_bytes))
        image = np.asarray(image_test)
        try:
            result = inference_detector(model , image)
            result = model.show_result(image, result)
        except:
            return Response("No object detected", media_type = "string")
        # import pdb;pdb.set_trace()
         
    res, im_png = cv2.imencode(".png", result)
    return StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True,)