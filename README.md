

# Harumanis Mango Grading Web Application
## Overview
This Django web application is designed to predict the grade of Harumanis Mango based on its physical measurements, including weight, length, and circumference. The application utilizes a pre-trained Random Forest model for the prediction. Users can input the mango's physical attributes, and the application will provide a predicted grade.

## Features
Input form for weight, length, and circumference of a Harumanis Mango.
Pre-trained Random Forest model for grade prediction.
Display of the predicted mango grade (Grade A, Grade B, or Grade C).
A user-friendly web interface for easy interaction.

## Getting Started
To run the application locally, follow these steps:

1. Clone the repository.
2. Install the required dependencies from requirement.txt.
3. Run the Django development server.
4. Access the web application via your browser.

## Usage
1. Input the weight, length, and circumference of a Harumanis Mango in the provided form.
2. Click the "Submit" button.
3. The application will display the predicted grade of the mango.
   
## Deployment
The application is designed for local deployment. For production deployment, you may need to adapt it for a web server and database setup.

## Model
The application uses a pre-trained Random Forest model to classify mangoes into three grades: Grade A, Grade B, or Grade C. The model is loaded from the 'rf_model.pkl' file located in the 'saveModel' directory.

## Technologies Used
* Django
* Python
* Pandas
* Joblib
* HTML/CSS for the user interface (Bootstrap 5)
  
## Project Status
This project is actively maintained and welcomes contributions from the open-source community.


## Support
If you encounter issues or have questions, please open an issue in this repository. We appreciate your feedback.
