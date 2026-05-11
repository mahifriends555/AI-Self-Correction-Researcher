
class Agent:
    def __init__(self, llm):
        self.llm = llm

    def should_retrieve(self, query):
        prompt = f"""
        You are an assistant with access to a private document database.
        Always retrieve from the database before answering any factual question.
        
        Question: {query}
        
        Should we search the document database to answer this?
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
    