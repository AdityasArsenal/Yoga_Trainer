data_dir = r"C:\Users\24adi\OneDrive\Desktop\for yoga\Yoga_Trainer\dataset"

yoga_poses_img_dict = {
    'downdog': list(data_dir.glob('downdog/*')),
    'goddess': list(data_dir.glob('goddess/*')),
    'plank': list(data_dir.glob('plank/*')),
    'tree': list(data_dir.glob('tree/*')),
    'warror2': list(data_dir.glob('warrior2/*')),
}

yoga_poses_lab_dict = {
    'downdog': 0,
    'goddess': 1,
    'plank':   2,
    'tree':    3,
    'warror2': 4,
}

ll = yoga_poses_img_dict['tree'][:5]

for i in ll:
    print(ll)