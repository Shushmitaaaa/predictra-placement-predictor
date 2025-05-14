# 🎓 Placement Prediction Web App

## 📌 About the Project

This project aims to help students predict their **placement eligibility** based on their academic performance and skillset. By entering a few key details such as CGPA, project experience, certifications, and soft skills, students can get real-time insights into their chances of being placed.

---
### Final Result
![home](https://github.com/user-attachments/assets/58a34374-06fd-41c9-b691-604b72a6cd3b)

![2nd](https://github.com/user-attachments/assets/971e3ffa-acc2-45bf-86e5-68db88b0bf5c)

![3rd](https://github.com/user-attachments/assets/ab7c43e4-24b3-4ae4-8eaf-8f9b945e75f7)

Try the live app here: https://predictra-placement-predictor.onrender.com


---

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Shushmitaaaa/predictra-placement-predictor.git
   ```


2. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```


---

## 📁 Project Structure

```
placement-pred/
│
├── myenv/                      # Virtual environment directory (not uploaded to GitHub)
│
├── static/
│   ├── images/                 # Folder containing images used in the UI
│   │   ├── 2nd.png
│   │   ├── 3rd.png
│   │   └── home.png
│   └── style.css               # Main stylesheet for the web app
│
├── templates/
│   └── index.html              # HTML template for the frontend
│
├── app.py                      # Main Flask application
├── prediction_model.ipynb      # Jupyter Notebook for model training/analysis
├── prediction_model.pkl        # Serialized ML model
├── requirements.txt            # List of dependencies
└── .gitignore                  # Files/folders to ignore in version control
```


---

## 🧭 Step-by-Step Workflow

### Step 1: Dataset Collection

I began by finding a well-structured dataset (from Kaggle) containing faetures related to academic performance and skill development that will help in determining if a student will get placed or not.


---

### Step 2: Data Cleaning

* Checked for **null values**, duplicates, and **inconsistencies**
* Cleaned data using `pandas` and `numpy`

---

### Step 3: Exploratory Data Analysis (EDA)

* Used **matplotlib**, **seaborn**, and **pandas profiling** to visualize data
* Analyzed feature relationships using:
  * Correlation matrix
* Dropped features that had **low correlation** with the target variable to improve model accuracy

---

### Step 4: Data Preprocessing

* Scaled numerical features
* Encoded categorical variables if present(converting yes/no to 0/1)

---

### Step 5: Model Building

* Split dataset into **training and testing** sets using `train_test_split`
* Since this was a **binary classification** problem, I tested multiple algorithms:

  * Logistic Regression
  * K-Nearest Neighbors
  * Support Vector Machines
  * Decision Tree
  * **Random Forest Classifier** (final choice)
* Evaluated models using:

  * **Accuracy Score**

>  **Final Model Chosen:** Random Forest Classifier
>  **Reason:** Best accuracy and generalization on test data

---

### Step 6: Model Saving

* Saved the trained model using `pickle` for later use in deployment.

```python
import pickle

pickle.dump(rf, open('prediction_model.pkl', 'wb'))
```

---

### Step 7: Deployment

Built the web app using HTML, CSS (frontend) and Flask (backend).
Integrated the trained model to predict placement based on user input.
Deployed the app on Render for public access.

## ⚙️ Technologies Used

* **Python**
* **NLTK (Natural Language Toolkit)**
* **Scikit-learn**
* **Flask**
* **HTML & CSS**
* **Pandas**
* **Matplotlib & Seaborn**
* **Render** *(for deployment)*

---

## 🤝 Contributions

Contributions to this project are welcome!
If you find any issues or have suggestions for improvement, feel free to:

*  Open an **Issue**
*  Submit a **Pull Request**

I’ll be happy to review and merge valuable contributions.

---




