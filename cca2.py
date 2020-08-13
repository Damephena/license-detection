import matplotlib.pyplot as plt
import matplotlib.patches as patches
from skimage import measure

import detection

label_image = measure.label(detection.binary_car_image)

# getting the maximum width, height and minimum width and height that a license plate can be
plate_dimensions = (
    0.08*label_image.shape[0],
    0.2*label_image.shape[0], 
    0.15*label_image.shape[1], 
    0.4*label_image.shape[1]
)
min_height, max_height, min_width, max_width = plate_dimensions
plate_objects_coordinates = list()
plate_like_objects = list()
fig, (axis_1) = plt.subplots(1)
axis_1.imshow(detection.gray_car_image, cmap="gray");

for region in measure.regionprops(label_image):
    if region.area > 50:
        min_row, min_col, max_row, max_col = region.bbox
        region_height = max_row - min_row
        region_width = max_col - min_col

        # ensure the region identified satisfies the condition of a typical license plate
        if region_height >= min_height and region_height <= max_height:
            if region_width >= min_width and region_width <= max_width:
                plate_like_objects.append(detection.binary_car_image[min_row:max_row,
                min_col:max_col])
                plate_objects_coordinates.append((
                    min_row,
                    min_col,
                    max_row,
                    max_col
                ))
                rect_border = patches.Rectangle(
                    (min_col, min_row),
                    max_col - min_col,
                    max_row - min_row
                )
                axis_1.add_patch(rect_border)
plt.show()
