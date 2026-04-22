
import wikipedia

class WebLoader:
    def __init__(self, max_chars=2000):
        self.max_chars = max_chars

    def load(self, query):
        try:
            # Search Wikipedia
            results = wikipedia.search(query)
            
            if not results:
                return []

            # Take top result
            page = wikipedia.page(results[0])
            
            content = page.content[:self.max_chars]

            return [content]

        except Exception as e:
            print(f"Error loading Wikipedia: {e}")
            return []