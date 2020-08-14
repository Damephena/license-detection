import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from skimage import measure

import cca2

license_plate = np.invert(cca2.plate_like_objects[2])
labelled_plate = measure.label(license_plate)

fig, (axis_1) = plt.subplots(1)
axis_1.imshow(license_plate, cmap="gray")

# ASSUMPTIONS: license plate width between 5% and 15%
# plate height between 35% and 60%
character_dimensions = (
    0.35*license_plate.shape[0],
    0.6*license_plate.shape[0],
    0.05*license_plate.shape[1],
    0.15*license_plate.shape[1],
)
