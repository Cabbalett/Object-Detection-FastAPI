import streamlit as st
import io
import os
import requests

from PIL import Image
import numpy as np

st.set_page_config(layout="wide")


def main():
    st.title("My CV Project")

    st.subheader("Object Detection task with Faster RCNN model pretrained with COCO Dataset")

    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg","png"])

    if uploaded_file:
        image_bytes = uploaded_file.getvalue()
        image = Image.open(io.BytesIO(image_bytes))
        image = np.asarray(image)
        st.image(image, caption='Uploaded Image')

        if st.button("Click to Start Inference!"):
            with st.spinner("Inferencing..."):
                files = [
                    ('files', (uploaded_file.name, image_bytes,
                               uploaded_file.type))
                ]
                response = requests.post("http://localhost:8001/order", files=files)
            try:
                result = Image.open(io.BytesIO(response.content))    
            except:
                st.error("No object was detected!")
                return
            st.image(result)
            st.success("Success!")


if __name__ == '__main__':
    main()