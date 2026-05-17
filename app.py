# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import random
# import time
# import re

# app = Flask(__name__)
# CORS(app)

# # -----------------------------
# # MEMORY (ChatGPT-style)
# # -----------------------------
# memory = {
#     "name": None,
#     "last_message": None
# }

# # -----------------------------
# # "LEARNING DATABASE" (FAKE LLM TRAINING)
# # -----------------------------
# qa_memory = {
#     "what is python": "Python is a programming language used for AI, web, and automation.",
#     "what is flask": "Flask is a Python web framework."
# }

# # -----------------------------
# # LEARNING FUNCTION
# # -----------------------------
# def learn(question, answer):
#     qa_memory[question.lower()] = answer


# def find_answer(message):
#     message = message.lower().strip()

#     for q in qa_memory:
#         if q in message:
#             return qa_memory[q]

#     return None


# # -----------------------------
# # CHATBOT ENGINE
# # -----------------------------
# def chatbot(message):

#     message = message.lower().strip()
#     memory["last_message"] = message

#     # -------------------------
#     # LEARN COMMAND
#     # -------------------------
#     learn_match = re.search(r"learn (.*) = (.*)", message)
#     if learn_match:
#         q = learn_match.group(1).strip()
#         a = learn_match.group(2).strip()
#         learn(q, a)
#         return f"I learned: '{q}' ✅"

#     # -------------------------
#     # NAME MEMORY
#     # -------------------------
#     name_match = re.search(r"my name is (.*)", message)
#     if name_match:
#         name = name_match.group(1).strip()
#         memory["name"] = name
#         return f"Nice to meet you {name} 😊"

#     if "what is my name" in message:
#         return memory["name"] or "I don't know your name yet."

#     # -------------------------
#     # CHECK LEARNED DATA
#     # -------------------------
#     answer = find_answer(message)
#     if answer:
#         return answer

#     # -------------------------
#     # GREETINGS
#     # -------------------------
#     if any(x in message for x in ["hi", "hello", "hey", "hy"]):
#         return random.choice([
#             "Hey 👋",
#             "Hello 😊",
#             "Hi there!"
#         ])

#     # -------------------------
#     # DEFAULT (ASK TO TEACH)
#     # -------------------------
#     return "I don't know this yet 🤔 but you can teach me: learn question = answer"


# # -----------------------------
# # API
# # -----------------------------
# @app.route("/chat", methods=["POST"])
# def chat():

#     data = request.get_json()
#     user_message = data.get("message", "")

#     time.sleep(0.3)

#     reply = chatbot(user_message)

#     return jsonify({
#         "reply": reply
#     })


# if __name__ == "__main__":
#     app.run(debug=True)



# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import time
# import re
# import random

# app = Flask(__name__)
# CORS(app)

# # -----------------------------
# # MEMORY SYSTEM (LIKE CHATGPT)
# # -----------------------------
# chat_history = []

# user_memory = {
#     "name": None,
#     "facts": {}
# }

# # -----------------------------
# # KNOWLEDGE BASE (LOCAL MINI BRAIN)
# # -----------------------------
# knowledge_base = {
#     "what is python": "Python is a programming language used for AI, web development, and automation.",
#     "what is flask": "Flask is a lightweight Python web framework.",
#     "what is ai": "AI stands for Artificial Intelligence where machines simulate human intelligence.",
#     "what is machine learning": "Machine learning is a subset of AI where systems learn from data.",
#     "what is chatgpt": "ChatGPT is an AI language model developed to generate human-like responses."
# }

# # -----------------------------
# # CONTEXT BUILDER (CORE OF CHATGPT FEEL)
# # -----------------------------
# def build_context():

#     # last 10 messages only (like real LLM context window)
#     return chat_history[-10:]


# # -----------------------------
# # SMART KNOWLEDGE SEARCH
# # -----------------------------
# def search_knowledge(message):

#     message = message.lower()

#     for q in knowledge_base:
#         if q in message:
#             return knowledge_base[q]

#     return None


# # -----------------------------
# # LEARNING SYSTEM
# # -----------------------------
# def learn_from_user(message):

#     match = re.search(r"remember that (.*) is (.*)", message)

#     if match:
#         key = match.group(1).strip().lower()
#         value = match.group(2).strip()

#         knowledge_base[key] = value
#         return f"I learned that {key} = {value} ✅"

#     return None


# # -----------------------------
# # CORE AI ENGINE (SIMULATED LLM)
# # -----------------------------
# def generate_response(message):

#     message = message.lower().strip()

#     # -------------------------
#     # MEMORY: NAME
#     # -------------------------
#     name_match = re.search(r"my name is (.*)", message)
#     if name_match:
#         name = name_match.group(1).strip()
#         user_memory["name"] = name
#         return f"Nice to meet you {name} 😊"

#     if "what is my name" in message:
#         return user_memory["name"] or "I don't know your name yet."

#     # -------------------------
#     # LEARNING MODE
#     # -------------------------
#     learned = learn_from_user(message)
#     if learned:
#         return learned

#     # -------------------------
#     # KNOWLEDGE BASE SEARCH
#     # -------------------------
#     kb_answer = search_knowledge(message)
#     if kb_answer:
#         return kb_answer

#     # -------------------------
#     # CONTEXT UNDERSTANDING (SIMULATION)
#     # -------------------------
#     context = build_context()

#     if len(context) > 0:
#         last_user_msg = context[-1]["user"]

#         if "?" in message:
#             return f"Earlier you mentioned '{last_user_msg}'. Based on that, I think you are asking about this new question."

#     # -------------------------
#     # GREETINGS
#     # -------------------------
#     if any(x in message for x in ["hi", "hello", "hey", "hy"]):
#         return random.choice([
#             "Hey 👋 I'm your AI assistant",
#             "Hello 😊 How can I help you?",
#             "Hi there! Ask me anything."
#         ])

#     # -------------------------
#     # FALLBACK (LLM STYLE RESPONSE)
#     # -------------------------
#     return random.choice([
#         "That's interesting 🤔 tell me more.",
#         "I'm thinking about that...",
#         "Can you explain differently?",
#         "I don't have exact info, but I can learn it if you teach me.",
#         "Good question 👍"
#     ])


# # -----------------------------
# # CHAT API
# # -----------------------------
# @app.route("/chat", methods=["POST"])
# def chat():

#     data = request.get_json()
#     user_message = data.get("message", "")

#     # store conversation (like ChatGPT memory)
#     chat_history.append({
#         "user": user_message,
#         "time": time.time()
#     })

#     # simulate thinking delay (ChatGPT feel)
#     time.sleep(0.4)

#     reply = generate_response(user_message)

#     # store bot reply
#     chat_history[-1]["bot"] = reply

#     return jsonify({
#         "reply": reply,
#         "history_length": len(chat_history)
#     })


# # -----------------------------
# # RUN SERVER
# # -----------------------------
# if __name__ == "__main__":
#     app.run(debug=True)




from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import re
import random
import requests   # for optional LLM mode

app = Flask(__name__)
CORS(app)

# -----------------------------
# MEMORY (ChatGPT STYLE)
# -----------------------------
chat_history = []

user_memory = {
    "name": None
}

# -----------------------------
# KNOWLEDGE BASE
# -----------------------------
knowledge_base = {
    "what is python": "Python is a programming language used for AI, web development, automation and data science.",
    "what is flask": "Flask is a lightweight Python web framework used to build APIs.",
    "what is ai": "AI is Artificial Intelligence where machines simulate human thinking.",
    "what is machine learning": "Machine learning is a field where systems learn from data."
}

# =========================================================
# 🔥 OPTIONAL REAL LLM (OLLAMA)
# =========================================================
USE_LLM = True   # 👈 change to True if you install Ollama

def ollama_reply(message):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": message,
                "stream": False
            }
        )
        return response.json()["response"]
    except:
        return "LLM not available. Using local brain."

# =========================================================
# SMART KNOWLEDGE SEARCH
# =========================================================
def search_kb(message):
    message = message.lower()
    for q in knowledge_base:
        if q in message:
            return knowledge_base[q]
    return None

# =========================================================
# LEARNING SYSTEM
# =========================================================
def learn(message):
    match = re.search(r"remember that (.*) is (.*)", message)
    if match:
        k = match.group(1).strip().lower()
        v = match.group(2).strip()
        knowledge_base[k] = v
        return f"I learned: {k} = {v} ✅"
    return None

# =========================================================
# CORE BRAIN (CHATGPT STYLE PIPELINE)
# =========================================================
def brain(message):

    message = message.lower().strip()

    # ---------------- NAME MEMORY ----------------
    name_match = re.search(r"my name is (.*)", message)
    if name_match:
        user_memory["name"] = name_match.group(1).strip()
        return f"Nice to meet you {user_memory['name']} 😊"

    if "what is my name" in message:
        return user_memory["name"] or "I don't know your name yet."

    # ---------------- LEARNING ----------------
    learned = learn(message)
    if learned:
        return learned

    # ---------------- KNOWLEDGE BASE ----------------
    kb = search_kb(message)
    if kb:
        return kb

    # ---------------- OPTIONAL REAL AI (OLLAMA) ----------------
    if USE_LLM:
        return ollama_reply(message)

    # ---------------- GREETING ----------------
    if any(x in message for x in ["hi", "hello", "hey"]):
        return random.choice([
            "Hey 👋",
            "Hello 😊",
            "Hi there!"
        ])

    # ---------------- FALLBACK INTELLIGENCE ----------------
    return random.choice([
        "That's interesting 🤔 tell me more.",
        "I'm thinking about that...",
        "Can you explain differently?",
        "I don't know this yet, but you can teach me.",
        "Good question 👍"
    ])

# =========================================================
# API ROUTE
# =========================================================
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    user_message = data.get("message", "")

    # store chat memory (LIKE CHATGPT)
    chat_history.append({"user": user_message})

    time.sleep(0.3)

    reply = brain(user_message)

    chat_history[-1]["bot"] = reply

    return jsonify({
        "reply": reply,
        "memory": len(chat_history)
    })

# =========================================================
# RUN
# =========================================================
if __name__ == "__main__":
    app.run(debug=True)