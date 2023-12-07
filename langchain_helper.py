from openapi_key import apiKey, organization
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import os
from langchain.llms import openai

os.environ["OPENAI_API_KEY"] = apiKey

llm = openai.OpenAI(temperature=0.6)


def generateRestaurant(cuisine):
    # chain 1: get restaurant name
    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want ot open a restaurant fro {cuisine} food. Suggest a good name. Return only one name.",
    )

    name_chain = LLMChain(
        llm=llm, prompt=prompt_template_name, output_key="restaurant_name"
    )
    # chain 2: Menu item

    prompt_template_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template=""" Suggest some menu items for  {restaurant_name}. Return it as comma separted list """,
    )
    food_item_chain = LLMChain(
        llm=llm, prompt=prompt_template_items, output_key="menu_items"
    )

    chain = SequentialChain(
        chains=[name_chain, food_item_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"],
    )

    response = chain({"cuisine": cuisine})
    return response


if __name__ == "__main__":
    # Call your method with a specific cuisine (e.g., "Indian")
    result = generateRestaurant("Indian")
    print(result)
