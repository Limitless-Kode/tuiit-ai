from decouple import config
import openai
class OpenAI:
    def __init__(self, api_key=config('OPENAI_API_KEY')):
      openai.api_key = api_key
    
    def get_completion(self, prompt, model='text-davinci-003', max_tokens=2000, temperature=0.9):
      response = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
      )
      return response.choices[0]
    
    def get_search(self, query, model='text-davinci-003', max_tokens=2000, temperature=0.9):
      response = openai.Completion.create(
        model=model,
        prompt=query,
        max_tokens=max_tokens,
        temperature=temperature,
      )
      return response.choices[0]