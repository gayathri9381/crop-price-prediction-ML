# crop-price-prediction-ML

##  Overview
This project focuses on predicting crop prices using Machine Learning techniques.  
The model analyzes historical agricultural data such as crop type, market trends, rainfall, and seasonal factors to estimate future crop prices accurately.

The main objective of this project is to help farmers and agricultural businesses make better decisions regarding crop sales and market planning.

---

##  Features
- Predicts crop prices using Machine Learning algorithms
- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Model training and evaluation
- Visualization of crop market trends
- User-friendly prediction workflow

---

##  Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- scikit-learn
- Jupyter Notebook

---

##  Project Structure
``` id="8q1m3z"
Crop-Price-Prediction/
│
├── dataset/
│   └── crop_price_dataset.csv
│
├── notebooks/
│   └── Crop_Price_Prediction.ipynb
│
├── models/
│   └── trained_model.pkl
│
├── images/
│   └── output_graphs.png
│
├── requirements.txt
├── README.md
└── app.py
```

---

##  Machine Learning Workflow
1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Exploratory Data Analysis
5. Model Training
6. Performance Evaluation
7. Prediction Generation

---

##  Algorithms Used
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

---

##  Model Performance
The model was evaluated using:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

The Random Forest model provided the best prediction accuracy among the tested algorithms.

---

##  How to Run the Project

### Step 1: Clone the Repository
```bash id="m2v7kc"
git clone https://github.com/your-username/crop-price-prediction.git
```

### Step 2: Navigate to Project Folder
```bash id="wy1j2d"
cd crop-price-prediction
```

### Step 3: Install Dependencies
```bash id="n9x0pa"
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash id="h3q9re"
python app.py
```


##  Future Improvements
- Deploying the model using Flask or Streamlit
- Real-time market price integration
- Weather-based prediction enhancement
- Mobile application support

---

##  Conclusion
This project demonstrates the practical implementation of Machine Learning in agriculture by helping predict crop prices efficiently. It highlights skills in data preprocessing, model building, visualization, and predictive analytics.
