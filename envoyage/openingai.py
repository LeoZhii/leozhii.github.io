# pip install --upgrade openai
import os
from openai import OpenAI

# Retrieve the API key from environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

def askAway(city, startDate, endDate, hobbies):
  # system prompt
  gptPrompt = """You are a retired explorer who has travelled the entire world. Now you provide the best assistance to beginner travellers 
  with recommendations to both must see spots and less known ones, activities you can do depending on their interests, great restaurants to eat at. 
  Give your responses carefully after analyzing the information they give to you. Consider how the time frame and date will impact, such as the season's weather.
  Respond like a wordy, fantastical tavern owner"""
  
  # user prompt
  user_message = f"The city I want to go to is {city}. I will go on {startDate} and leave on {endDate}. My hobbies are {hobbies}"

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",

    messages=[
    {"role": "system", "content": gptPrompt},
    {"role": "user", "content": user_message}
    ]
  )

  return completion.choices[0].message
