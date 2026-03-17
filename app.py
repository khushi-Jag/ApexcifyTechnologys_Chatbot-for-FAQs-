from flask import Flask, render_template, request, jsonify
import math
import re

app = Flask(__name__)

faqs = [
    {"question": "what is artificial intelligence", "answer": "Artificial Intelligence (AI) is the simulation of human intelligence by machines. It allows systems to perform tasks such as reasoning, learning, decision-making, and problem solving."},
    {"question": "how does artificial intelligence work", "answer": "Artificial Intelligence works by using algorithms, training data, and computational models to identify patterns, make predictions, and automate intelligent decisions."},
    {"question": "what is machine learning", "answer": "Machine Learning is a branch of Artificial Intelligence that enables systems to learn from data and improve performance without being explicitly programmed for every task."},
    {"question": "what is deep learning", "answer": "Deep Learning is a subset of Machine Learning that uses multi-layered neural networks to process and learn complex data patterns."},
    {"question": "what is natural language processing", "answer": "Natural Language Processing (NLP) is a branch of AI that enables machines to understand, process, and generate human language."},
    {"question": "what is computer vision", "answer": "Computer Vision is a branch of AI that enables computers to analyze, interpret, and understand images and videos."},
    {"question": "what is data science", "answer": "Data Science is the field of extracting meaningful insights and knowledge from data using statistics, programming, and machine learning techniques."},
    {"question": "what is python used for", "answer": "Python is widely used for web development, automation, data analysis, artificial intelligence, machine learning, and scientific computing."},
    {"question": "what is a chatbot", "answer": "A chatbot is a software system that interacts with users through text or voice and provides automated responses using rules or AI models."},
    {"question": "what is a neural network", "answer": "A neural network is a computational model inspired by the human brain. It consists of interconnected nodes that learn patterns from data."},
    {"question": "what is supervised learning", "answer": "Supervised learning is a machine learning approach in which a model is trained on labeled data, where the correct output is already known."},
    {"question": "what is unsupervised learning", "answer": "Unsupervised learning is a machine learning approach where a model discovers hidden patterns and structures in unlabeled data."},
    {"question": "what is reinforcement learning", "answer": "Reinforcement Learning is a type of machine learning where an agent learns through trial and error by receiving rewards and penalties."},
    {"question": "difference between ai and machine learning", "answer": "Artificial Intelligence is the broader concept of intelligent systems, while Machine Learning is a subset of AI that focuses on learning patterns from data."},
    {"question": "difference between machine learning and deep learning", "answer": "Machine Learning includes a variety of algorithms, while Deep Learning specifically uses layered neural networks for more complex tasks."},
    {"question": "what is overfitting", "answer": "Overfitting happens when a model learns training data too well, including noise and details, and performs poorly on new unseen data."},
    {"question": "what is underfitting", "answer": "Underfitting occurs when a model is too simple to capture the underlying structure of the data, resulting in poor performance."},
    {"question": "what is a dataset", "answer": "A dataset is a structured collection of data used for analysis, training machine learning models, or generating insights."},
    {"question": "what is training data", "answer": "Training data is the dataset used to teach a machine learning model how to recognize patterns and make predictions."},
    {"question": "what is test data", "answer": "Test data is used to evaluate the performance of a trained machine learning model on unseen examples."},
    {"question": "what is validation data", "answer": "Validation data is used during model training to tune parameters and reduce overfitting before final testing."},
    {"question": "what is an algorithm", "answer": "An algorithm is a step-by-step procedure or set of rules designed to perform a task or solve a problem."},
    {"question": "what is tensorflow", "answer": "TensorFlow is an open-source machine learning framework developed by Google for building and deploying AI models."},
    {"question": "what is pytorch", "answer": "PyTorch is an open-source deep learning framework widely used for research and production applications in AI."},
    {"question": "what is scikit learn", "answer": "Scikit-learn is a popular Python library for machine learning that provides tools for classification, regression, clustering, and preprocessing."},
    {"question": "what is feature engineering", "answer": "Feature engineering is the process of selecting, transforming, and creating input variables that improve machine learning model performance."},
    {"question": "what is feature scaling", "answer": "Feature scaling is the process of normalizing or standardizing numerical data so that features are on a similar scale."},
    {"question": "what is classification", "answer": "Classification is a machine learning task where the goal is to predict a category or class label."},
    {"question": "what is regression", "answer": "Regression is a machine learning task used to predict continuous numerical values."},
    {"question": "what is clustering", "answer": "Clustering is an unsupervised learning technique that groups similar data points together based on patterns."},
    {"question": "what is dimensionality reduction", "answer": "Dimensionality reduction reduces the number of input features while preserving important information in the dataset."},
    {"question": "what is pca", "answer": "PCA, or Principal Component Analysis, is a dimensionality reduction technique used to simplify data while preserving variance."},
    {"question": "what is accuracy in machine learning", "answer": "Accuracy is the percentage of correct predictions made by a machine learning model out of all predictions."},
    {"question": "what is precision in machine learning", "answer": "Precision measures how many of the predicted positive cases were actually positive."},
    {"question": "what is recall in machine learning", "answer": "Recall measures how many of the actual positive cases were correctly identified by the model."},
    {"question": "what is f1 score", "answer": "F1-score is the harmonic mean of precision and recall, used to balance both metrics in classification tasks."},
    {"question": "what is confusion matrix", "answer": "A confusion matrix is a table used to evaluate classification models by comparing predicted and actual labels."},
    {"question": "what is cross validation", "answer": "Cross-validation is a model evaluation technique that splits data into multiple parts to test the model’s stability and performance."},
    {"question": "what is hyperparameter tuning", "answer": "Hyperparameter tuning is the process of selecting the best configuration values for a machine learning model to improve performance."},
    {"question": "what is linear regression", "answer": "Linear Regression is a supervised learning algorithm used to model the relationship between variables and predict continuous values."},
    {"question": "what is logistic regression", "answer": "Logistic Regression is a classification algorithm used to predict binary outcomes such as yes or no."},
    {"question": "what is decision tree", "answer": "A Decision Tree is a model that makes predictions by splitting data into branches based on feature conditions."},
    {"question": "what is random forest", "answer": "Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting."},
    {"question": "what is support vector machine", "answer": "Support Vector Machine is a supervised learning algorithm used for classification and regression by finding the best separating boundary."},
    {"question": "what is knn", "answer": "KNN, or K-Nearest Neighbors, is a simple algorithm that classifies data points based on their nearest neighbors."},
    {"question": "what is naive bayes", "answer": "Naive Bayes is a probabilistic classification algorithm based on Bayes’ theorem with an assumption of feature independence."},
    {"question": "what is model deployment", "answer": "Model deployment is the process of integrating a trained machine learning model into a real application so that it can make predictions on new data."},
    {"question": "what is big data", "answer": "Big Data refers to extremely large and complex datasets that require advanced tools and technologies for storage, processing, and analysis."},
    {"question": "what is cloud computing", "answer": "Cloud computing is the delivery of computing services such as storage, servers, and software over the internet."},
    {"question": "what is cybersecurity", "answer": "Cybersecurity is the practice of protecting systems, networks, and data from cyber attacks, unauthorized access, and digital threats."},
    {"question": "what is web development", "answer": "Web development is the process of building and maintaining websites and web applications using frontend and backend technologies."},
    {"question": "what is frontend development", "answer": "Frontend development focuses on building the visible part of websites and applications that users interact with directly."},
    {"question": "what is backend development", "answer": "Backend development focuses on server-side logic, databases, APIs, and application functionality behind the user interface."},
    {"question": "what is api", "answer": "An API, or Application Programming Interface, allows different software systems to communicate and exchange data with each other."},
    {"question": "what is flask", "answer": "Flask is a lightweight Python web framework used for building web applications and APIs quickly and efficiently."},
    {"question": "what is django", "answer": "Django is a high-level Python web framework that helps developers build secure and scalable web applications."},
    {"question": "what is html", "answer": "HTML, or HyperText Markup Language, is the standard language used to structure content on web pages."},
    {"question": "what is css", "answer": "CSS, or Cascading Style Sheets, is used to style and design the appearance of HTML elements on web pages."},
    {"question": "what is javascript", "answer": "JavaScript is a programming language used to create dynamic, interactive, and responsive web pages."}
]

stopwords = {
    "is", "a", "an", "the", "of", "for", "to", "and", "in", "on", "what",
    "are", "was", "were", "it", "this", "that", "with", "by", "about",
    "please", "tell", "me", "define", "explain", "can", "you", "how"
}

synonyms = {
    "ai": "artificial intelligence",
    "ml": "machine learning",
    "dl": "deep learning",
    "nlp": "natural language processing",
    "cv": "computer vision",
    "knn": "k nearest neighbors",
    "svm": "support vector machine",
    "api": "application programming interface"
}


def preprocess_text(text):
    text = text.lower().strip()

    for short_form, full_form in synonyms.items():
        text = re.sub(rf"\b{re.escape(short_form)}\b", full_form, text)

    text = re.sub(r"[^a-z0-9\s]", "", text)
    words = text.split()
    words = [word for word in words if word not in stopwords]
    return words


def build_vocabulary(faq_list):
    vocabulary = set()
    for item in faq_list:
        vocabulary.update(preprocess_text(item["question"]))
    return sorted(vocabulary)


def text_to_vector(text, vocabulary):
    words = preprocess_text(text)
    vector = [0] * len(vocabulary)
    for i, vocab_word in enumerate(vocabulary):
        vector[i] = words.count(vocab_word)
    return vector


def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a * a for a in vec1))
    magnitude2 = math.sqrt(sum(b * b for b in vec2))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0

    return dot_product / (magnitude1 * magnitude2)


def keyword_overlap_score(user_words, faq_words):
    user_set = set(user_words)
    faq_set = set(faq_words)

    if not user_set or not faq_set:
        return 0.0

    common = user_set.intersection(faq_set)
    return len(common) / max(len(user_set), len(faq_set))


def classify_confidence(score):
    if score >= 0.78:
        return "High"
    if score >= 0.5:
        return "Medium"
    return "Low"


def get_suggestions():
    return [
        "What is AI?",
        "How does AI work?",
        "What is machine learning?",
        "Difference between AI and machine learning?",
        "What is NLP?",
        "What is Python used for?"
    ]


def find_best_answer(user_question, faq_list, vocabulary):
    user_vector = text_to_vector(user_question, vocabulary)
    user_words = preprocess_text(user_question)

    best_score = 0
    best_answer = None
    best_question = None

    for item in faq_list:
        faq_vector = text_to_vector(item["question"], vocabulary)
        faq_words = preprocess_text(item["question"])

        cosine_score = cosine_similarity(user_vector, faq_vector)
        overlap_score = keyword_overlap_score(user_words, faq_words)
        final_score = (0.65 * cosine_score) + (0.35 * overlap_score)

        if final_score > best_score:
            best_score = final_score
            best_answer = item["answer"]
            best_question = item["question"]

    return best_question, best_answer, best_score


vocabulary = build_vocabulary(faqs)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({
            "reply": "Please enter a valid question.",
            "matched_question": None,
            "confidence": "Low",
            "score": 0,
            "suggestions": get_suggestions()
        })

    best_question, best_answer, score = find_best_answer(user_message, faqs, vocabulary)
    confidence = classify_confidence(score)

    if score >= 0.18:
        return jsonify({
            "reply": best_answer,
            "matched_question": best_question.title(),
            "confidence": confidence,
            "score": round(score, 2),
            "suggestions": []
        })

    return jsonify({
        "reply": "I could not confidently match your question. Try rewriting it more clearly or use one of the suggested questions below.",
        "matched_question": None,
        "confidence": "Low",
        "score": round(score, 2),
        "suggestions": get_suggestions()
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)