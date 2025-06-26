# 🌱 Soil Fertility Prediction Using Machine Learning

This project uses the **Gaussian Naïve Bayes (GNB)** algorithm to predict soil fertility levels (High, Medium, Low) based on parameters such as pH, N, P, K, moisture, and temperature. It aims to support sustainable agriculture by providing farmers with a fast, accurate, and cost-effective way to assess soil health.

## 📘 Overview

Traditional soil testing methods are time-consuming and expensive. This system automates fertility analysis using machine learning, delivering instant predictions and fertilizer recommendations via a Flask web interface.

## 🚀 Features

- Predicts soil fertility (High, Medium, Low)
- Supports real-time user input or CSV upload
- Gives fertilizer recommendations & soil improvement tips
- Web-based interface using Flask
- Accuracy: **97.5%**

## ⚙️ Technologies Used

- **Python**  
- **Flask** – for the web application  
- **scikit-learn** – for Gaussian Naïve Bayes  
- **pandas**, **numpy** – for data handling  
- **matplotlib**, **seaborn** – for optional visualizations  

## 📂 Project Structure

```
soil-fertility-ml/
├── app.py                  # Flask backend
├── naivebayes.py           # Model logic
├── dataset.csv             # Training data
├── templates/
│   └── index.html          # Frontend UI
├── static/                 # Optional CSS/JS
└── README.md
```

## 🧠 ML Model: Gaussian Naïve Bayes (GNB)

- **Input Parameters**:  
  - pH  
  - Nitrogen (N)  
  - Phosphorus (P)  
  - Potassium (K)  
  - Moisture  
  - Temperature  

- **Output**: Fertility → `High`, `Medium`, `Low`

- **Performance**:  
  - Accuracy: 97.5%  
  - Confusion Matrix:
    ```
    [[19 0 0]
     [ 0 19 0]
     [ 0 0 20]]
    ```

## 🔧 How to Run

### 📦 Installation

```bash
pip install flask pandas scikit-learn
```

### ▶️ Start the App

```bash
python app.py
```

Then open `http://localhost:5000` in your browser.

## 📊 Sample Input

```csv
pH,Nitrogen,Phosphorus,Potassium,Moisture,Temperature
6.7,50,18,180,27,29
```

### Output:
```
Predicted Fertility: Medium
Suggested Action: Use compost or NPK 10:26:26
```

## 📈 Comparison with Other Models

| Algorithm       | Accuracy |
|----------------|----------|
| KNN            | 88.3%    |
| SVM            | 90.6%    |
| CNN            | 94.1%    |
| Random Forest  | 95.8%    |
| **GNB (Proposed)** | **97.5%** |

## ✅ Advantages

- High accuracy for continuous data
- Low resource requirement
- Real-time web predictions
- Easy to use for non-technical users
- Supports sustainable agriculture

## ⚠️ Limitations

- Assumes feature independence
- Less effective with correlated or imbalanced data
- Limited insight into feature importance
- Preprocessing required for missing or noisy values

## 📚 Dataset

- Source: [Kaggle Soil Dataset](https://github.com/PoojaChippa/soil-dataset)
- Features: `pH, N, P, K, moisture, temperature, target`

## 📲 Future Scope

- IoT integration for live data collection
- Mobile app development
- Crop & fertilizer recommendation engine
- Integration with government schemes
- Multilingual & voice-enabled support
- Weather-based fertility prediction

## 📖 References

- Ahmed et al. (2023) – ANN for soil prediction  
- Karthika & Priya (2019) – Naïve Bayes in agriculture  
- Patle et al. (2018) – GNB for environmental prediction  
- Delgado-Baquerizo et al. (2018) – Global soil microbiome atlas  
