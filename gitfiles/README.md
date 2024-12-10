# Yoga Trainer


## This project will help you with your yoga poses, with voice instructions.
Yoga Trainer, this project kills the need of a yoga trainer as it helps you to do your yoga poses correctly. This was passible with the help of 2 models
* Fine tuned - MobileNetV2 (YES I TRAINED IT).
* MediaPipe.


## How To Use 
  ### The Yoga Trainer
     step 1 - go to the live_cam_test.py file run it.
     step 2 - you show the pic of a pose you want to perform.
     from there the trainer will instruct you 🎉
  ### The Finetuner 
  #### You can train your model with this project as well
      step 1 - Load your the dataset and make sure to pass it correctly.
      step 2 - _data_sampling.py Use this program to make sure your data is correctly loaded.
      step 3 - _synthatic_data_prodection.py If you have shortage of data.
      step 4 - _pre_processing_data.py Use this for data pre-processing, it processes  data for MobileNetV2 model as we are fine tuning it.
      step 5 - _fine_tuneing.py This will fine tune the cnn model = MobileNetV2  (i have used 5 epochs as it was enough).
      now the model is saved as a .h5 file 🎉


## Working
    * Live_cam_test.py loads a finetuned model (.h5) which you can find in the same dir.
    * It will return the detected pose.
    * The godness_checks.py will instruct you how to do the pose (it uses mediapipe).
    * The godness_checks.py uses auio_conv.py to instruct you vocally.
    * Auio_conv.py uses a tts model pyttsx3.


## Additional Requirements
    * You will be needing python 3.10.11 to run this repo.
    * All libraries version must be followed strictly.


## Known Issues 
    * The project is not compatible with up to date python. recommended version is 3.10.11.


## Personal Notes
    🔴🔴🔴py -3.10 -m venv myenv🔴🔴🔴
    Never flip a image upside down only flip horizontal.

