
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
        self.web_loader = WebLoader()

    def run(self, query, max_iterations=2):
        print(f"\n🔍 Query: {query}")

        for i in range(max_iterations):
            print(f"\n🔁 Iteration {i+1}")

            # 🧠 Step 1: Decide
            if self.agent.should_retrieve(query):
                print("✅ Retrieval needed")

                # ✏️ Step 2: Rewrite query
                query = self.agent.rewrite_query(query)
                print(f"✏️ Improved Query: {query}")

                # 📚 Step 3: Try FAISS (internal docs)
                docs = self.retriever.get_docs(query)
                vector_context = [d.page_content for d in docs]

                print(f"📚 Vector docs: {len(vector_context)}")

                # 🌐 Step 4: Try Wikipedia
                web_docs = self.web_loader.load(query)
                print(f"🌐 Web docs: {len(web_docs)}")

                # 🧠 Step 5: Build context
                all_context = vector_context + web_docs

                # ❗ IMPORTANT: fallback if no context
                if not all_context:
                    print("⚠️ No context → using LLM fallback")
                    return self.generator.simple_generate(query)

                context = "\n".join(all_context)[:3000]  # limit size

                # 🤖 Step 6: Generate answer
                answer = self.generator.generate(query, context)

            else:
                print("❌ No retrieval needed")
                return self.generator.simple_generate(query)

            print(f"🧠 Answer: {answer}")

            # 🔍 Step 7: Critic check
            if self.critic.evaluate(query, answer, context):
                print("✅ Final Answer Approved")
                return answer

            # 🔁 Step 8: Retry
            print("❌ Answer not good → refining...")
            query = self.agent.rewrite_query(query)

        return answer