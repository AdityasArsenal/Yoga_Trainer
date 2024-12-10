# Yoga Trainer


## This project will help you with your yoga poses, with voice instructions.
Yoga Trainer, this project kills the need of a yoga trainer as it helps you to do your yoga poses correctly. This was passible with the help of 2 models
* - _[fine tuned - MobileNetV2] (YES I TRAINED IT)
* - _[MediaPipe]_


## How to use 
  ### The yoga trainer
     step 1 - go to the live_cam_test.py file run it.
     step 2 - you show the pic of a pose you want to perform.
     from there the trainer will instruct you 🎉
  ### the finetuner 
  #### You can train your model with this project as well
      step 1 - Load your the dataset and make sure to pass it correctly.
      step 2 - _data_sampling.py use this program to make sure your data is correctly loaded.
      step 3 - _synthatic_data_prodection.py if you have shortage of data.
      step 4 - _pre_processing_data.py use this fro data pre-processing it processes  data for MobileNetV2 model as we are fine tuning it/
      step 5 - _fine_tuneing.py this will fine tune the cnn model = MobileNetV2  (i have used 5 epcho as it was enough).
      now the model is saved as a .h5 file 🎉


## working
    * live_cam_test.py loads a finetuned model (.h5) which you can find in the same dir.
    * it will return the detected pose
    * the godness_checks.py will instruct you how to do the pose (it uses mediapipe)
    * The godness_checks.py uses auio_conv.py to instruct you voically.
    * auio_conv.py uses a tts model pyttsx3


## Additional requirements
    * You will be needing python 3.10.11 to run this repo.
    * All libraries version must be followed stricketly.


## known issues 
    * The project is not compatable with up to date python. recommented version is 3.10.11


## personal notes
    🔴🔴🔴py -3.10 -m venv myenv🔴🔴🔴
    never flip a image upside down only flip horizontal 

