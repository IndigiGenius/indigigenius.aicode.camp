# indigigenius.aicode.camp
IndigiGenius AI Code Camp curriculum repository.

## About IndigiGenius
[https://www.indigigenius.org](https://www.indigigenius.org)  
IndigiGenius is an Indigenous-led nonprofit working to increase the representation of Indigenous people in computer science through culturally informed curriculum, programs, and initiatives.

## About The Curriculum

The curriculum incorporated into this repository is derived from activities and lessons learned from the Lakota AI Code Camp (LAICC, [https://lakota.aicode.camp](https://lakota.aicode.camp)). The LAICC began in the summer of 2022 and has been annually hosted at the Black Hills State University campus.

The repository is split into units for supporting students in creating an application powered by a deep learning model, developed using the Python programming language, the fastai library, and Gradio Web Applications. The goal of the current version of this curriculum is to support students in developing an image recognition model that provides information about an object in the Indigenous language of the student participants. The LAICC has sought to support students in collecting image data and cultural knowledge about plants traditionally known to, and used by, the Lakota people, which they can then use to create an application to preserve, disseminate, and appropriately control that information.  

The approach of this curriculum was created using a backwards planning process, beginning with the goal of creating a web-based Computer Vision application. The process for creating a web-based application is grounded in created a Gradio application hosted on Hugging Face (huggingface.co) (Unit 03). In order to create such a web-based application, it is necessary that a .pkl model be created using deep learning techniques. The curriculum leverages the Fast.AI API to create such a model, and the jupyter notebooks necessary to accomplish this task are located in Unit 02. For learners to understand and work within the Fast.AI API, they must first be comfortable with the Python programming language, and so the first unit (Unit 01) is focused on developing the programming skills necessary to work with Python.

## The Process
1. Learners work with activities to develop competency with the Python programming language and jupyter notebooks.
1. Learners use Docker containers, jupyter notebooks, and the fastai library to create a computer vision deep learning model.
1. Learners leverage the computer vision model they created to build a web-based Gradio application hosted on Hugging Face to deploy a tool that educates and disseminates cultural knowledge.

## Getting Started
1. [Create a fork of this repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)
1. Clone the fork of the repository in your GitHub.com repo to run locally (we suggest you use GitHub Desktop)
1. For each unit, follow the instructions in the associated Readme.md file to appropriately run the Jupyter Notebook, or Docker container, environment 
1. Follow the Readme.md for each unit

## Schedule

### Week 1 - Python & Data Science
| Time/Day   | Monday (0)                            | Tuesday (1)           | Wednesday (2)     | Thursday (3)     | Friday (4)                 |
|------------|---------------------------------------|-----------------------|-------------------|------------------|----------------------------|
| Module 0   | Installs & Intro to Jupyter Notebooks | Variables             | Lists             | OOP              | Data Science Final Project |
| Module 1   | Intro to Programming                  | Data Types            | Dictionaries      | Extending Turtle | Data Science Final Project |
| Module 2   | Intro to Turtle                       | Loops & Turtle        | Functions         | Extending Turtle | Data Science Final Project |
| Module 3   | Intro to Artificial Intelligence      | Conditionals & Turtle | Custom Functions  | Pandas           | Data Science Presentations |
| Extensions | Robot Game                            |                       | Turtle Challenges | Hangman          |                            |
| Evening    |                                       | Language Class        |                   | Language Class   |                            |

### Week 2 - Deep Learning - Computer Vision
| Time/Day   | Monday (0)                     | Tuesday (1)       | Wednesday (2)     | Thursday (3)                     | Friday (4)                     |
|------------|--------------------------------|-------------------|-------------------|----------------------------------|--------------------------------|
| Module 0   | Installs                       | Collecting Data   | Collecting Data   | Accessing Data                   | Computer Vision Model Training |
| Module 1   | Installs                       | Collecting Data   | Collecting Data   | DataBlocks & DataLoaders         | Computer Vision Model Training |
| Module 2   | Is it a Zintkala?              | Organizing Data 1 | Organizing Data 2 | Learner, Fine Tuning, & Cleaning | What is a CNN?                 |
| Module 3   | Data Collection Best Practices | Organizing Data 1 | Preparing Data    | Learner, Fine Tuning, & Cleaning | Computer Vision Model Training |
| Extensions |                                |                   |                   | Cleaning Student Data            |                                |
| Evening    |                                | Language Class    |                   | Language Class                   |                                |

### Week 3 - Model Driven Web Applications
| Time/Day   | Monday (0)             | Tuesday (1)            | Wednesday (2)          | Thursday (3)           | Friday (4)               |
|------------|------------------------|------------------------|------------------------|------------------------|--------------------------|
| Module 0   | Intro to HuggingFace   | Gradio Blocks          | Customizing Gradio App | Customizing Gradio App | Presentation Preparation |
| Module 1   | Creating Gradio App    | Speaker                | Speaker                | Speaker                | Presentation Preparation |
| Module 2   | Remapping Model Output | Gradio CSS             | College Applications   | Resumes & LinkedIn     | Presentation Preparation |
| Module 3   | Gradio Themes          | Customizing Gradio App | Customizing Gradio App | Customizing Gradio App | Presentations & Closing  |
| Extensions |                        |                        |                        |                        |                          |
| Evening    |                        | Language Class         |                        | Language Class         |                          |

## About the Schedule
- This curriculum is designed to run with four modules per day
- Each module is 1.5 hours, with 15 minute breaks in between, and lunch betwen modules 1 and 2
- We suggest that language classes be incorporated into evening activities at least twice a week
- **Each day should begin with a 'stand up' protocol where everyone stands in a circle and is individually asked and responds to the following questions:**
    - **What went well?**
    - **What didn't go well?**
    - **What would you change or improve?**
- ***We highly suggest that these 'stand up' questions be asked in the Indigenous language of the student participants***

## About the Language Classes
The curriculum is derived from activities leveraged by the Lakota AI Code Camp (LAICC, [https://lakota.aicode.camp](https://lakota.aicode.camp)). During the LAICC, students are provided instruction in Lakota twice a week during the evenings. These classes are typically grounded in developing conversational skills in the students' Indigenous language, as well as to prepare them to introduce themselves in that Indigenous language during the Closing event if they choose to do so.
