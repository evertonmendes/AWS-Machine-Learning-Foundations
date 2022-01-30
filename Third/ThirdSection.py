'AI cost for using DeepRacer, Deep Composer in AWS'
''''
To get you started with AWS DeepRacer, you receive 10 free hours to train or evaluate models and 5GB of free storage 
during your first month. This offer is valid for 30 days after you have used the service for the first time

To get started, AWS DeepComposer provides a 12-month Free Tier for first-time users. With the Free Tier, you can 
perform up to 500 inference jobs translating to 500 pieces of music using the AWS DeepComposer Music studio.
'''

'machine learning with AWS'


#AWS Machine Learning offerings - AI services
'''
-Health AI: transcribe medical speech to text, in other words, the communication between health providers and
patients provide the foundation of patients diagnosis and treatment. In that way, the doctor dont need
to spend your time saving texts, just have to pass your time taking care of patients. 
-Industrial AI: Amazon Monitron can increase efficiency and cost-saving to a ride range of companies. As an example, a failure of machines can be predicted through
sensors and data analysis plataform.
-Anomaly detection: amazon lookout for metrics, detect and diagnosis anomalies in businesses and operational data, such as a sudden dip in sales revenue or costumer acquisition
rates.
-Chatbots: amazon lex enables you to publish your voice or text books for use on mobiles devices, web apps, and chat services  
-Personalization: Amazon Personalize deliver highly customized recommendations
-Forecasting: Amazon forecast helps you achieve higher accuracy forecasts that can be used for forecasting product demand, resource needs, or financial performance, and many more.
-Fraud: Amazon fraud detector 
-Code Development: amazon codeguru and devops guru improve code quality and indentify most expensive lines of code
-Vision: amazon rekognition
-Speech: amazon polly turns text into lifelike speech, allowing you to create aplications that talk
-Text: Amazon textract translate data by OCR
-Contact Centers: contact lens enables you analysis conversations between customer and agents. With that in mind, the system do sentiment analysis, detects issues, and enable you automatically categorize contacts
-Search: Amazon Kendra
'''

'Computer Vision'

'''
    -Image Classification: What's in this image? This type of task has applications in text detection or optical character recognition (OCR) and content moderation.
    -Object Detection: is closely related to image classification, but allows users to get more details in an image. As an example, we can know if there are multiples intances of the same object, or get objetcs from different classes.
    -Semantic Segmentation:  it tries to identify down the pixel level which part of the image is part of the object.
    -Activity recognition:  Video has the added dimension of time and, therefore, models are able to detect changes that occur over time.

    AWS DeepLens
        AWS DeepLens allows you to create and deploy end-to-end computer vision–based applications(ReadToMe,SodaThief, Poopinator, ...). 
        
    The AWS DeepLens device
        The AWS DeepLens camera is powered by an Intel® Atom processor, which can process 100 billion floating-point operations per second (GFLOPS). 

    First, you use the AWS console to create your project, store your data, and train your model.
Then, you use your trained model on the AWS DeepLens device. On the device, the video stream from the camera is processed, inference is performed, and the output from inference is passed into two output streams:
Device stream – The video stream passed through without processing.
Project stream – The results of the model's processing of the video frames.


Four key components are required for an AWS DeepLens–based project.
    Collect your data: Collect data and store it in an Amazon S3 bucket.
    Train your model: Use a Jupyter Notebook in Amazon SageMaker to train your model.
    Deploy your model: Use AWS Lambda to deploy the trained model to your AWS DeepLens device.
    View model output: Use Amazon IoT Greenrass to view your model's output after the model is deployed.

'''

'Reinforcement Learning'

'''
    -In reinforcement learning (RL), an agent is trained to achieve a goal based on the feedback it receives as it interacts with an environment.
    It collects a number as a reward for each action it takes.
    -RL is used in video games like as Go, Atari, Starcraft, video game level design, wind energy optimization, indutrial robotics, fraud detection, stock trading, autonomous driving. 
    -6 important terms or RL; agent, environment, state, action, reward, episode
    -The training algortihm is divided is two methods:
        -Soft actor critic (SAC) embraces exploration and is data-efficeint, but can lack stability
        -A proximal policy optimization  (PPO) is stable but data-hungry
    -An action space is the set of all valid actions
        -discrete action:PPO
        -continuous action:SAC, PPO
    -Exploitation means the car begins to exploit or use information from previous experiences to help it reach its goal. Different training algorithms utilize exploration and exploitation differently.
    -The deepRacer device have three type of tools. One camera of 120 degree field with 15fps, the second one stereo camera wich provides depht information and for last a LIDAR sensor which detects objetcs in surrounding

'''

'Generative AI'
'''
    A generative model aims to answer the question,"Have I seen data like this before?" 
    three popular types of generative models: 
            generative adversarial networks (GANs):
                Generative adversarial networks (GANs), are a machine learning model format that involves pitting two networks against each other to generate new content. 
            general autoregressive models
                (AR-CNNs) are used to study systems that evolve over time and assume that the likelihood of some data depends only on what has happened in the past
            and transformer-based models.
                Transformer-based models are most often used to study data with some sequential structure (such as the sequence of words in a sentence)
            
            Each AWS DeepComposer Music studio experience supports three different generative AI techniques
            Chartbusters is a global challenge where you can use AWS DeepComposer to create original compositions and compete in monthly challenges to showcase your machine learning and generative AI skills.


        A GAN is a type of generative machine learning model which pits two neural networks against each other to generate new content: a generator and a discriminator.
            A generator is a neural network that learns to create new data resembling the source data on which it was trained.
A           discriminator is another neural network trained to differentiate between real and synthetic data 
            Generator loss: Measures how far the output data deviates from the real data present in the training dataset.
Discriminator loss: Evaluates how well the discriminator differentiates between real and fake data.

        When a note is either added or removed from your input track during inference, we call it an edit event. To train the AR-CNN model to predict when notes need to be added or removed from your input track (edit event), the model iteratively updates the input track to sounds more like the training dataset. During training, the model is also challenged to detect differences between an original piano roll and a newly modified piano roll.
        AR-CNN makes the sound seems more like bach type or rock genre, GANs add accommaniments to create models and tranformers are used to extend the sound for more than 20 second, as an example.
'''

