from app.main import app
from collections import Counter

route_identifiers = []
for route in app.routes:
    methods = sorted(list(getattr(route, 'methods', [])))
    for method in methods:
        route_identifiers.append((route.path, method))

counts = Counter(route_identifiers)

print("ACTUAL DUPLICATE (PATH, METHOD) COMBINATIONS:")
found_duplicates = False
for (path, method), count in counts.items():
    if count > 1:
