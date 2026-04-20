

class Agent:
    def __init__(self, llm):
        self.llm = llm

    def should_retrieve(self, query):
        prompt = f"""
        Decide if the question requires external knowledge retrieval.

        Question: {query}

        Answer only YES or NO.
        """
        response = self.llm.invoke(prompt).content.lower()
        return "yes" in response

    def rewrite_query(self, query):
        prompt = f"""
        Improve the following query to make it more precise:

        Query: {query}
        """
        return self.llm.invoke(prompt).content
    