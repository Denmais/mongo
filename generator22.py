from pymongo import MongoClient
import os
import random
import uuid
from datetime import datetime, timedelta
from faker import Faker


client = MongoClient("mongodb://user:user@mongo:27017")
mong = client['mongodb']
fake = Faker()
action = ['open', 'close']
start = fake.date_time_this_year().isoformat()
status = ["approved", "rejected"]
user_id = [x for x in range(1000)]
product_id = [x for x in range(500)]

# TODO Models
def UserSessions(count):
    """UserSessions, сессии пользователей"""
    
    
    return [{
        "session_id": str(uuid.uuid4()), #uuid
        "user_id": random.choice(user_id),
        "start_time": start,
        "end_time": (start + timedelta(minutes=60)).isoformat(),
        "pages_visited": [fake.uri for _ in range(5)],
        "device": fake.user_agent(),
        "actions": random.choice(action)
    } for _ in range(count)]

def ProductPriceHistory(count):
    """ProductPriceHistory, история изменения цен"""
    return [{
        "product_id": random.choice(product_id),
        "price_changes": [{
            "date": fake.date_time_this_year().isoformat(),
            "price": random.randint(1,1000)
        } for _ in range(random.randint(1, 10))],
        "current_price": random.randint(1,1000),
        "currency": "RUB"
    } for _ in range(n)]EventLogs

def EventLogs(count):
    """EventLogs, логи событий."""
    return [{
        "event_id": str(uuid.uuid4()),
        "timestamp": fake.date_time_this_year().isoformat(),
        "event_type": random.choice(action),
        "details": 'some_details'
    } for _ in range(n)]




def SupportTickets(count):
    return [{"ticket_id": str(uuid.uuid4()), "user_id": random.choice(user_id), 
             "status": random.choice(status), "issue_type": 'issue', 
             "messages": ['message1', 'message2'], "created_at": fake.date_time_this_year().isoformat(), 
             "updated_at": fake.date_time_this_year().isoformat() } for _ in range(count)]


def UserRecommendations(count):
    return [{
        "user_id": random.choice(user_id),
        "recommended_products": [random.choice(product_id) for _ in range(3)],
        "last_updated": fake.date_time_this_year().isoformat()
    } for _ in range(count)]

def ModerationQueue(count):
    return [{
        "review_id": str(uuid.uuid4()),
        "user_id": random.choice(user_id),
        "product_id": random.choice(product_id),
        "review_text": fake.text(),
        "rating": random.randint(1, 5),
        "moderation_status": random.choice(status),
        "flags": [fake.word() for _ in range(random.randint(0, 3))],
        "submitted_at": fake.date_time_this_year().isoformat()
    } for _ in range(count)]

def SearchQueries(count):
    return [{
        "query_id": str(uuid.uuid4()), "user_id": random.choice(user_id),
        "query_text": fake.sentence(), "timestamp": fake.date_time_this_year().isoformat(),
        "filters": [fake.word() for _ in range(random.randint(0, 3))],
        "results_count": random.randint(0, 50)
    } for _ in range(count)]




mong.user_sessions.insert_many(UserSessions(100))
mong.product_price_history.insert_many(ProductPriceHistory(100))
mong.event_logs.insert_many(EventLogs(100))

mong.support_tickets.insert_many(SupportTickets(100))

user_recommendations = get_count("USER_RECOMMENDATIONS_COUNT", 1000)
mong.user_recommendations.insert_many(generate_user_recommendations(user_recommendations))

moderation_queues = get_count("MODERATION_QUEUE_COUNT", 500)
db.moderation_queue.insert_many(generate_moderation_queue(moderation_queues))
print("Очередь модерации загружена в MongoDB: ", moderation_queues)

search_queries = get_count("SEARCH_QUERIES_COUNT", 1000)
db.search_queries.insert_many(generate_search_queries(search_queries))
print("Поисковые запросы загружены в MongoDB: ", search_queries)

print("Все данные успешно загружены в MongoDB")