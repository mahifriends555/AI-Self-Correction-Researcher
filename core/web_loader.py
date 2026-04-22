
import wikipedia


class WebLoader:
    def __init__(self, max_chars=2000):
        self.max_chars = max_chars

    def load(self, query):
        try:
            print(f"\n🌐 Searching Wikipedia for: {query}")

            # 🔍 Step 1: Search results
            results = wikipedia.search(query)
            print(f"🔍 Results: {results}")

            if not results:
                print("❌ No Wikipedia results found")
                return []

            # 🔁 Step 2: Try multiple results (robust)
            for title in results[:5]:
                try:
                    print(f"➡️ Trying page: {title}")

                    page = wikipedia.page(title, auto_suggest=False)

                    content = page.content[:self.max_chars]

                    print(f"✅ Loaded page: {title}")

                    return [content]

                # ⚠️ Handle disambiguation (VERY COMMON)
                except wikipedia.exceptions.DisambiguationError as e:
                    print(f"⚠️ Disambiguation error for {title}")
                    print(f"👉 Options: {e.options[:3]}")

                    # Try first option from disambiguation
                    try:
                        page = wikipedia.page(e.options[0])
                        content = page.content[:self.max_chars]
                        print(f"✅ Loaded disambiguated page: {e.options[0]}")
                        return [content]
                    except Exception:
                        continue

                except wikipedia.exceptions.PageError:
                    print(f"⚠️ Page not found: {title}")
                    continue

                except Exception as e:
                    print(f"⚠️ Skipping {title}: {e}")
                    continue

            print("❌ Could not load any Wikipedia page")
            return []

        except Exception as e:
            print(f"❌ Wikipedia global error: {e}")
            return []
        
        