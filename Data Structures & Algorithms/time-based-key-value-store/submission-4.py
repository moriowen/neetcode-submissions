class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        user = self.store.get(key)

        if not user:
            return ""

        low, high = 0, len(user)-1

        while low <= high: 
            mid = (low+high)//2

            if user[mid][1] > timestamp:
                high = mid - 1
            elif user[mid][1] < timestamp:
                low = mid + 1
            else:
                return user[mid][0]
        
        return user[high][0] if high >= 0 else ""
