import os
import re
import google.generativeai as genai
from dotenv import load_dotenv
from sqlalchemy import text
from backend.database import engine

load_dotenv()

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    print("Warning: GEMINI_API_KEY not found in environment.")

class SQLEngine:
    def __init__(self):
        # Using the advanced preview model confirmed available for your key
        self.model = genai.GenerativeModel('gemini-3.5-flash')
        self.schema_info = self._get_schema_info()

    def _get_schema_info(self):
        return """
        Table: Customers (id, name, email, country)
        Table: Products (id, name, category, price, stock)
        Table: Orders (id, customer_id, date, total)
        Table: OrderItems (id, order_id, product_id, quantity)
        """

    def generate_sql(self, natural_query):
        prompt = f"""
        You are a highly intelligent and versatile AI Assistant. You can answer ANY question, whether it's about the database OR general knowledge, creative writing, coding, or just chatting.

        HOW TO RESPOND:
        1. If the user asks about data in the database (products, prices, orders, customers, etc.), return:
           SQL: <sqlite_query>

        2. For ALL other questions (general knowledge, greetings, jokes, etc.), return:
           TEXT: <your_answer>

        Rules:
        - Only return ONE of the formats (SQL: ... or TEXT: ...).
        - Use TEXT mode for anything that isn't a direct database query.
        - Be professional, engaging, and helpful.

        User Request: "{natural_query}"
        Response:"""
        
        response = self.model.generate_content(prompt)
        raw_text = response.text.strip()
        
        # Clean formatting
        raw_text = re.sub(r'```[a-z]*\n?|```', '', raw_text).strip()
        return raw_text

    def validate_sql(self, sql):
        # Forbidden keywords for safety
        forbidden = ["DROP", "DELETE", "TRUNCATE", "ALTER", "GRANT", "REVOKE", "UPDATE", "INSERT"]
        for word in forbidden:
            if re.search(rf"\b{word}\b", sql, re.IGNORECASE):
                return False, f"Safety Violation: '{word}' command is restricted."
        return True, "Success"

    def execute_sql(self, sql):
        try:
            with engine.connect() as connection:
                result = connection.execute(text(sql))
                # For SELECT queries
                if result.returns_rows:
                    columns = result.keys()
                    rows = [dict(zip(columns, row)) for row in result]
                    return {"status": "success", "data": rows, "sql": sql}
                else:
                    connection.commit()
                    return {"status": "success", "message": "Command executed successfully", "sql": sql}
        except Exception as e:
            return {"status": "error", "message": str(e), "sql": sql}
