# 📧 Spam Email Classifier

## 🚀 Project Overview
This project is an **email spam classifier** that predicts whether a given email is **spam** or **ham** (not spam). The model is trained on a **Kaggle dataset** using the **Naïve Bayes algorithm**. A web application is built using **Flask**, allowing users to input email text and get predictions from the trained model.

The project is also **deployed on Render** and utilizes **GitHub Actions for CI/CD** to automate deployment and testing.



## 📊 Dataset
- **Source:** Kaggle
- **Contains:** Emails labeled as `spam` or `ham`
- **Features:**
  - `text`: The email content
  - `label`: `spam` or `ham`

---

## 🤖 Model Training
The model follows these preprocessing steps:
1. **Convert text to lowercase**
2. **Tokenization** (using NLTK’s `word_tokenize`)
3. **Removing stopwords and punctuation**
4. **Stemming** (using `PorterStemmer`)
5. **TF-IDF Vectorization**
6. **Training with Naïve Bayes Classifier**



---

## 🌐 Web App (Flask)
The web application allows users to input an email, and the trained model classifies it as spam or ham.

### **Run the Flask App Locally**
```sh
pip install -r requirements.txt
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

---

## ☁️ Deployment on Render
This project is **deployed on Render**, allowing public access.

### **Steps to Deploy**
1. Push code to **GitHub**
2. Connect GitHub repo to **Render**
3. Add **Build Command** in `deploy.yaml`
4. Deploy 🚀

---

## 🔄 CI/CD with GitHub Actions
GitHub Actions is used to automate:
- **Testing the model** before deployment
- **Auto-deployment** when pushing to the `main` branch

### **GitHub Actions Workflow (`.github/workflows/ci-cd.yml`)**
```yaml
name: Deploy to Render

on:
  push:
    branches:
      - main  # Change this to your deployment branch

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Install Dependencies
        run: |
          pip install -r requirements.txt  # Install required dependencies


      - name: Deploy to Render
        env:
          RENDER_SERVICE_ID: ${{ secrets.RENDER_SERVICE_ID }}
          RENDER_API_KEY: ${{ secrets.RENDER_API_KEY }}
        run: |
          curl -X POST "https://api.render.com/v1/services/$RENDER_SERVICE_ID/deploys" \
          -H "Authorization: Bearer $RENDER_API_KEY" \
          -H "Accept: application/json" \
          -d ''

```

---

## 🛠 Technologies Used
- **Python** (Flask, Sklearn, NLTK, Pandas)
- **Machine Learning** (Naïve Bayes, TF-IDF)
- **Frontend** (HTML, CSS, Bootstrap)
- **Deployment** (Render)
- **CI/CD** (GitHub Actions)

---

## 🏆 Results
✅ **Accuracy:** 98.35%  
✅ **Precision:** 99.18%

---

## 🎯 Future Improvements
- ✅ Enhance UI with **better design**
- ✅ Train on **larger datasets**
- ✅ Integrate **real-time email classification via API**

---

## 📜 License
This project is **open-source** under the **MIT License**.

---

## 📩 Contact
For any queries, feel free to reach out!

📧 **Email:** (mailto:alokthakur609@gmail.com)  
💻 **GitHub:** (https://github.com/)

---

