# stratosync_engine.py

import random
import json

class StratoSyncEngine:
    def __init__(self, product_catalog=None):
        self.product_catalog = product_catalog or []
        self.chat_history = []

    def load_products(self, filepath):
        try:
            with open(filepath, 'r') as file:
                self.product_catalog = json.load(file)
            print(f"[INFO] Loaded {len(self.product_catalog)} products.")
        except Exception as e:
            print(f"[ERROR] Failed to load products: {e}")

    def recommend_product(self):
        if not self.product_catalog:
            return "I'm sorry, I couldn't find any products to recommend right now."
        product = random.choice(self.product_catalog)
        return f"May I recommend: {product['name']} - {product['description']} (${product['price']})"

    def handle_query(self, user_input):
        user_input_lower = user_input.lower()
        self.chat_history.append({"user": user_input})

        if "recommend" in user_input_lower or "suggest" in user_input_lower:
            response = self.recommend_product()
        elif "hello" in user_input_lower or "hi" in user_input_lower:
            response = "Hello! I'm StratoSync, your assistant. How can I help you today?"
        elif "help" in user_input_lower:
            response = "I can recommend products, answer questions, and assist you with your needs. Just ask!"
        else:
            response = "I'm still learning! Please try asking for a product recommendation or say 'help'."

        self.chat_history.append({"stratosync": response})
        return response

    def save_chat_history(self, filepath):
        try:
            with open(filepath, 'w') as file:
                json.dump(self.chat_history, file, indent=4)
            print(f"[INFO] Chat history saved to {filepath}.")
        except Exception as e:
            print(f"[ERROR] Failed to save chat history: {e}")

# Example usage
if __name__ == "__main__":
    assistant = StratoSyncEngine()
    assistant.load_products('products.json')  # Your product catalog file

    print("Welcome to StratoSync Starter! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            assistant.save_chat_history('chat_history.json')
            print("Goodbye! Chat history saved.")
            break

        response = assistant.handle_query(user_input)
        print(f"StratoSync: {response}")
