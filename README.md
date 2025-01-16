#  SmartTrashClassifier 
An AI-powered waste sorting tool to help you sort your waste correctly and sustainably! 🌿✨  

---

## 📋 Overview  
SmartTrashClassifier is a machine learning-based tool that uses **image recognition** to classify waste into three categories:  
- ♻️ **Organic**  
- 📄 **Paper**  
- 🧴 **Plastic**  

By using this tool, you can:  
- Reduce contamination in recycling streams.  
- Promote proper waste management practices.  
- Support a cleaner, greener planet. 🌍💚  

---

## 🚀 Features  
- 🤖 **AI-Powered Classification**: Utilizes a trained neural network for  waste classification.  
- 🌱 **Eco-Friendly**: Encourages sustainable waste management practices.  
- 🖼️ **Visual Feedback**: Displays uploaded images and predictions.  
- 🛠️ **Easy Setup**: Minimal configuration required.  

---

## 🛠️ How It Works  

1. **Train a Model**:  
   - Use [Teachable Machine by Google](https://teachablemachine.withgoogle.com/) to train a custom image recognition model with at least two classes (e.g., Organic, Paper, Plastic).  
   - Export the trained model in **TensorFlow format** (`keras_model.h5` and `labels.txt`).  

2. **Add Test Images**:  
   - Include your test images in the project directory (e.g., `test.jpg`, `test2.jpg`, `test3.png`).  

3. **Run the Script**:  
   - The script will preprocess the images, run them through the model, and output the classification result along with a confidence score.

---


## 🛠️ Setup Instructions  
To ensure the script works correctly, install the necessary Python libraries !

---

## 📂 Code
The full source code for this project can be found in the file [`main.py`](./main.py).

---

## 📝 License
This project is open-source and licensed under the [MIT License](LICENSE).

---

## 👤 Author
Created by Jood. Feel free to contribute or suggest improvements to the project!
