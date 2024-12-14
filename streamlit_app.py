import streamlit as st
from setup import prepare_images,make_date_3d
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="True"
st.title("InstantMesh")
st.write("Pass the multiview images")
image1 = st.file_uploader("image 1", type=["jpg", "png", "jpeg"])
image2 = st.file_uploader("image 2", type=["jpg", "png", "jpeg"])
image3 = st.file_uploader("image 3", type=["jpg", "png", "jpeg"])
image4 = st.file_uploader("image 4", type=["jpg", "png", "jpeg"])

images=[image1,image2,image3,image4]

images=prepare_images(images)
st.write(images.shape)