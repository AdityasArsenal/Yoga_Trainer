import pathlib
import PIL.Image 

data_dir=r"C:\Users\24adi\OneDrive\Desktop\for yoga\Yoga_Trainer\dataset"
data_dir = pathlib.Path(data_dir)
print(data_dir)

ll = list(data_dir.glob('*/*.jpg'))[:5]

for i in ll:
    print(i)

image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)

TT = list(data_dir.glob('tree/*'))
TT[:5]

img = PIL.Image.open(str(TT[1]))

img.show()