import JSON
import random
import time

events ["login", "page_view", "page_view"]
users ["email", "email"]

for i in range(5):
  event = {
    "eventType": random.choice(events),
    "userId": random.choice(users),
    "timestampe": time.time()
  }

print(json.dumps(events))
