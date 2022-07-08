import os

images_to_segment = "images2seg"

for file in os.listdir(images_to_segment):
    os.system(
        "pipenv run python fast_seg.py -i {}".format(
            os.path.join(images_to_segment, file)
        )
    )
