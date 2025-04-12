# Title - SafeScan: Securing Digital Payments
This project aims to address the challenge "Proactive Fraud Detection in Digital Payments Using QR Code and UPI ID Verification".

## Introduction
This project ensures secure UPI transactions by verifying recipient legitimacy through QR codes and UPI IDs. A machine learning model analyzes transaction patterns, classifying recipients as legitimate or fraudulent. Integrated with payment APIs, it blocks suspicious transactions, enhancing trust, reducing fraud, and creating a safer digital payment ecosystem.

## Features
- Scanning a QR code on a webpage to detect the associated UPI ID.
- Retrieving relevant bank statements based on the detected UPI ID.
- Using a machine learning model to analyze the statements and classify the UPI ID as fraudulent, suspicious, or genuine.

## Technology Used
- Python 3.12.4
- Machine Learning
- Flask
- HTML/CSS/JavaScript

## Installation Steps
- You can use any IDE. We highly recommend VS Code
- Install PIP : python -m pip install pip==24.3.1
- Install Python Virtual Environment : pip install virtualenv
- Create Virtual Environment : virtualenv env [HERE 'env' is Environment Name]
- Activate Environment : .\env\Scripts\activate.ps1 [HERE 'env' is Environment Name]
    (If you encounter an error while activating the environment, ensure to set the execution policy to Unrestricted)
- Install Libraries in Environment : 
    python -m pip install -r .\requirements.txt
- Run Server :
    py app.py runserver

## Dataset
- https://www.kaggle.com/datasets/jainilcoder/online-payment-fraud-detection?resource=download 

## Libraries Used
    Flask, numpy, pandas, openpyxl, joblib, scikit-learn