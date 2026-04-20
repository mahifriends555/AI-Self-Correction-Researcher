
from app.core.core.retriever import Retriever
from app.core.core.generator import Generator
from app.core.core.agent import Agent
from app.core.core.critic import Critic


class RAGPipeline:
    def __init__(self, documents):
        self.retriever = Retriever(documents)
        self.generator = Generator()
        self.agent = Agent(self.generator.llm)
        self.critic = Critic(self.generator.llm)

    def run(self, query, max_iterations=3):
        print(f"\n🔍 Query: {query}")

        for i in range(max_iterations):
            print(f"\n🔁 Iteration {i+1}")

            if self.agent.should_retrieve(query):
                query = self.agent.rewrite_query(query)
                docs = self.retriever.get_docs(query)
                context = "\n".join([d.page_content for d in docs])
                answer = self.generator.generate(query, context)
            else:
                answer = self.generator.simple_generate(query)
                context = ""

            print(f"🧠 Answer: {answer}")

            if self.critic.evaluate(query, answer, context):
                print("✅ Final Answer Approved")
                return answer

            print("❌ Refining query...")
            query = self.agent.rewrite_query(query)

        return answer
    