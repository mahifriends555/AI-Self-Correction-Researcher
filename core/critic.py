

class Critic:
    def __init__(self, llm):
        self.llm = llm

    def evaluate(self, query, answer, context):
        prompt = f"""
        Evaluate the answer based on the context.

        Question: {query}

        Context:
        {context}

        Answer: {answer}

        Reply only GOOD or BAD.
        """
        response = self.llm.invoke(prompt).content.lower()
        return "good" in response