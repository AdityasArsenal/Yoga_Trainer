# Yoga Trainer


## This project will help you with your yoga poses, with voice instructions.
Yoga Trainer, this project kills the need of a yoga trainer as it helps you to do your yoga poses correctly. This was passible with the help of 2 models
* Fine tuned - MobileNetV2 (YES I TRAINED IT).
* MediaPipe.


## How To Use 
  ### The Yoga Trainer
     just run the main.py
  
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
    * It will return the detected pose to specific trainer.
    * let's assume you have choosen goddess pose
    * The godness_main.py will instruct you how to do the pose (it uses mediapipe).
    * The godness_main.py uses auio_conv.py to instruct you vocally.
    * Auio_conv.py uses a tts model pyttsx3.
    * similarly any the poses you choose the code will respond accordingly.

## Dataset Used (https://www.kaggle.com/datasets/niharika41298/yoga-poses-dataset)
    * I have picked this dataset from kaggle.
    * Then cleaned it as it was having diffrent versions of same pose under same label.
    * Added more synthatic data to increase the dataset weightage and help the model understand better.
    * The code used for synthatic data generation can be found under tran_n_test folder.

## Model Architecture
    * This project uses mobilenetv2 as it's base architecture, which intern uses Neural Networks below the hood.
    * This model trained on imagenet dataset, hence has greate understanding of curves and borders.
    * Particularly choose this model because it's light-weight for mobile usage.
    * InPut images size required 224 x 224.
    * Even though it is a robust model it needs to be fine tuned for specific useage like Yoga Pose detection.

## Fine-Tuned Model
    * My model retains the initial weights of MobileNetV2, replaces the classifier layer, and adds a custom layer for pose detection.
    * Accuracy 98%.
  #### Performance
                  Epoch = 5
    Epoch 1/5 - loss: 0.8835 - acc: 0.6875
    Epoch 2/5 - loss: 0.2899 - acc: 0.9394
    Epoch 3/5 - loss: 0.1832 - acc: 0.9631
    Epoch 4/5 - loss: 0.1329 - acc: 0.9781
    Epoch 5/5 - loss: 0.1037 - acc: 0.9887

## Ux
    * Project has a built in voice instructions.
    * As it is dependent on the finetuned-mobilenetV2 model it can smoothly run on any phone.
    * The camera can be set at a distance and the user can perform yoga with ease, while lestening to the instructions.

## Additional Requirements
    * You will be needing python 3.10.11 to run this repo.
    * All libraries version must be followed strictly.


## Known Issues 
    * The project is not compatible with up to date python. recommended version is 3.10.11.


## Personal Notes
    🔴🔴🔴py -3.10 -m venv myenv🔴🔴🔴
    Never flip a image upside down only flip horizontal.

