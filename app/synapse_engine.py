from pytrends.request import TrendReq
import json
import random
import time

def fetch_trending_topics():
    pytrends = TrendReq()
    trending_searches = pytrends.trending_searches(pn='united_states')
    topics = trending_searches[0].tolist()
    return topics

def generate_products_from_trends(topics, filename='app/products.json'):
    try:
        with open(filename, 'r') as f:
            products = json.load(f)
    except FileNotFoundError:
        products = []

    for topic in topics[:5]:  # Limit to top 5 topics for now
        product_id = f"prod_{topic.replace(' ', '_').replace('/', '_')}_{random.randint(1000,9999)}"
        new_product = {
            "id": product_id,
            "name": f"AI Solution for {topic}",
            "description": f"Automated script designed to address emerging market needs around {topic}.",
            "price_cents": random.choice([49900, 59900, 99900])  # Random attractive pricing
        }

        # Check for duplicate products
        if not any(prod["name"] == new_product["name"] for prod in products):
            products.append(new_product)

    with open(filename, 'w') as f:
        json.dump(products, f, indent=4)
    print(f"[Synapse Engine] {len(topics[:5])} new products generated and added to products.json.")

if __name__ == "__main__":
    topics = fetch_trending_topics()
    generate_products_from_trends(topics)
