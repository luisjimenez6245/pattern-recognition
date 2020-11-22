from models import Class, Data

C1 = [(200, 160, 120), (210, 170, 130), (215, 172, 133),
      (210, 165, 134), (198, 177, 138)]
C2 = [(90, 130, 60), (92, 138, 54), (87, 128, 66),
      (91, 134, 60), (85, 123, 55)]
C3 = [(30, 44, 178), (20, 40, 180), (24, 42, 184),
      (28, 50, 176), (22, 46, 181)]
color_classes = [C1, C2, C3]
classes = []
i = 1

for c in color_classes:
    items = []
    helper = Class(name="c" + str(i))
    for item in c:
        items.append(
                Data(
                    name="",
                    characteristics={"r": item[0], 'b': item[1], 'g': item[2]}
                )
            )
    helper.load_items(items)
    i += 1
    classes.append(
            helper
        )
