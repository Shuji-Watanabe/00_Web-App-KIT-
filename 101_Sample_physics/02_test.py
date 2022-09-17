import time

import numpy as np
import streamlit as st
from matplotlib import pyplot as plt

video = np.random.randn(100, 10, 3)

x = []
y = []
z = []


fig = plt.figure(figsize=(10, 10))
ax = plt.axes(projection="3d")
graph = ax.scatter([], [], [], s=50, color="orange")  # s argument here

placeholder = st.empty()

for i in range(len(video)):
    frame = video[i]
    for num in range(0, len(frame) - 1):
        dx, dy, dz = frame[num]
        dx_n, dy_n, dz_n = frame[num + 1]
        # Visualize 3D scatter plot
        x.append(dx)
        y.append(dy)
        z.append(dz)
        if i + 1 == len(frame) - 1:
            x.append(dx_n)
            y.append(dy_n)
            z.append(dz_n)
        # Give labels
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_ylabel("z")
    graph._offsets3d = (x, y, z)

    placeholder.pyplot(fig)

    time.sleep(0.01)