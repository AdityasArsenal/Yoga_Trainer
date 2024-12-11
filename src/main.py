from pose import get_pose
from warrior2_main import instructor_for_warrior2_pose
from goddess_main import instructor_for_goddess_pose
from tree_main import instructor_for_tree_pose
from downdog_main import instructor_for_downdog_pose
from auio_conv import audd

labs = ['downdog', 'goddess', 'plank', 'tree', 'warrior2']

requestt = "please show me the pose you want to perform"

audd(requestt)
lab = get_pose()

pose = f"ok let's perform {lab} pose"
audd(pose)

if lab == "downdog" :
    print("ok in the coddddddddddddddd")
    instructor_for_downdog_pose(lab)

elif lab == "goddess" : 
    print("ok in the coddddddddddddddd")
    instructor_for_goddess_pose(lab)

elif lab == "plank" : 
    print("ok in the coddddddddddddddd")
    instructor_for_goddess_pose(lab)

elif lab == "tree" :
    print("ok in the coddddddddddddddd")
    instructor_for_tree_pose(lab)

elif lab == "warrior2":
    print("ok in the coddddddddddddddd")
    instructor_for_warrior2_pose(lab)

else :
    print("Really sorry the trainer is not capable of this pose")
