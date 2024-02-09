from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

img = np.asarray(Image.open('./img/scann.png'))
print(repr(img))