import detection
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from skimage import measure

label_image = measure.label(detection.binary_car_image)
fig, (axis_1) = plt.subplots(1)
axis_1.imshow(detection.gray_car_image, cmap="gray");

for region in measure.regionprops(label_image):
    # if region.area < 50:
    #     # likely not a license plate
    #     continue
    # bounding box coordinates
    if region.area >= 50 :
        min_row, min_col, max_row, max_col = region.bbox
        rect_border = patches.Rectangle((min_col, min_row), max_col - min_col, max_row - min_row, 
            edgecolor="blue",
            linewidth=2,
            fill=False
            )
        axis_1.add_patch(rect_border)
plt.show()