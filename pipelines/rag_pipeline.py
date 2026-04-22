
from core.retriever import Retriever
from core.generator import Generator
from core.agent import Agent
from core.critic import Critic
from core.web_loader import WebLoader


class RAGPipeline:
    def __init__(self, documents):
        self.retriever = Retriever(documents)
        self.generator = Generator()
        self.agent = Agent(self.generator.llm)
        self.critic = Critic(self.generator.llm)
        self.web_loader = WebLoader()   # ✅ NEW

    def run(self, query, max_iterations=3):
        print(f"\n🔍 Query: {query}")

        for i in range(max_iterations):
            print(f"\n🔁 Iteration {i+1}")

            # 🧠 Step 1: Decide
            if self.agent.should_retrieve(query):
                print("✅ Retrieval needed")

                # ✏️ Step 2: Rewrite query
                query = self.agent.rewrite_query(query)
                print(f"✏️ Improved Query: {query}")

                # 🌐 Step 3: Load Wikipedia data
                web_docs = self.web_loader.load(query)
                print(f"🌐 Loaded {len(web_docs)} web docs")

                # 📚 Step 4: Retrieve from vector DB
                docs = self.retriever.get_docs(query)

                # 🔗 Step 5: Combine contexts
                vector_context = [d.page_content for d in docs]
                all_context = vector_context + web_docs

                context = "\n".join(all_context)

                # 🤖 Step 6: Generate answer
                answer = self.generator.generate(query, context)

            else:
                print("❌ No retrieval needed")
                answer = self.generator.simple_generate(query)
                context = ""

            print(f"🧠 Answer: {answer}")

            # 🔍 Step 7: Critic evaluation
            if self.critic.evaluate(query, answer, context):
                print("✅ Final Answer Approved")
                return answer

            # 🔁 Step 8: Refinement
            print("❌ Answer not good → refining...")
            query = self.agent.rewrite_query(query)

        return answer