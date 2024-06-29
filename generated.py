# Import the Python SDK
import google.generativeai as genai
# Used to securely store your API key
from google.colab import userdata

GOOGLE_API_KEY=userdata.get('Morningstar')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

domain = 'Algebra-Mathematics'

prompt = f"Generate a series of 20 questions for an MCQ test for high school students in the {domain} subject. Provide 4 options for each question and also label the difficulty of the questions into 5 categories from 1 being easiest to 5 being hardest. Order the questions in increasing order of difficulty. Provide the output as a python dataframe (print it using csv format)"

response = model.generate_content(prompt)
data_str = response.text[7:-4]
from io import StringIO
import pandas as pd

df = pd.read_csv(StringIO(data_str))

print(df)