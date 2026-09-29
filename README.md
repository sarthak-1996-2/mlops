# 🚗 Cars24 Used Car Price Prediction

A simple **Streamlit web application** that predicts the price of a used car based on selected car features.

The application uses a pre-trained machine learning regression model and provides an interactive UI where users can select car attributes and get an estimated price.

## 📌 Project Overview

This project demonstrates how to:

* Build an interactive ML application using **Streamlit**
* Load and display data using **Pandas**
* Load a pre-trained ML model using **Pickle**
* Accept user inputs through Streamlit widgets
* Encode categorical features into numerical values
* Generate a car price prediction

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Streamlit**
* **Scikit-learn** (for the trained model)
* **Pickle**
* **Excel Dataset**

## 📂 Project Structure

```text
.
├── main.py                    # Streamlit application
├── requirements.txt         # Python dependencies
├── cars24-car-price.xlsx    # Car price dataset
├── car_pred                 # Pre-trained ML model
└── README.md                # Project documentation
```

## ⚙️ Prerequisites

Make sure Python is installed on your system.

You can verify it using:

```bash
python --version
```

It is recommended to create a virtual environment before installing the dependencies.

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Linux / macOS:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

## 📦 Install Dependencies

Install all required Python packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run main.py
```

After starting the application, Streamlit will provide a local URL in the terminal. Open that URL in your browser to access the application.

## 🖥️ Application Features

### Data Preview

The application displays the first few rows of the Cars24 dataset using Streamlit's dataframe component.

### Car Configuration

Users can select:

* **Fuel Type**

  * Diesel
  * Petrol
  * CNG
  * LPG
  * Electric

* **Transmission Type**

  * Manual
  * Automatic

* **Engine Power**

  * Adjustable using a slider from **500 to 5000**

* **Number of Seats**

  * 2 to 10 seats

### Price Prediction

After selecting the required inputs, click the **Predict** button.

The application loads the pre-trained regression model and displays the predicted car price.

## 🔄 Prediction Flow

```text
User Input
    │
    ├── Fuel Type
    ├── Transmission Type
    ├── Engine Power
    └── Number of Seats
            │
            ▼
   Categorical Encoding
            │
            ▼
    Feature Preparation
            │
            ▼
    Pre-trained ML Model
            │
            ▼
     Price Prediction
```

## 🔢 Categorical Encoding

The application converts categorical values into numerical values before passing them to the ML model.

| Feature          | Encoding |
| ---------------- | -------- |
| Diesel           | 1        |
| Petrol           | 2        |
| CNG              | 3        |
| LPG              | 4        |
| Electric         | 5        |
| Dealer           | 1        |
| Individual       | 2        |
| Trustmark Dealer | 3        |
| Manual           | 1        |
| Automatic        | 2        |

## 📊 Model Input

The prediction model receives the following features:

```text
Year
Fuel Type
Kilometers Driven
Seller Type
Transmission Type
Mileage
Engine
Max Power
Seats
```

Some features currently use fixed/default values in the application, while the user can modify selected features through the Streamlit interface.

## ⚠️ Important

Make sure the following files are present in the same directory as `main.py`:

```text
cars24-car-price.xlsx
car_pred
```

The application will not work correctly if the dataset or trained model file is missing.

## 🚀 Quick Start

For a quick setup:

```bash
pip install -r requirements.txt
streamlit run main.py
```

That's it! The Cars24 Used Car Price Prediction application will start locally.
