# question_data = [
# {"text": "A slug's blood is green.", "answer": "True"},

import requests


url = "https://opentdb.com/api.php"
params = {
    'amount': 10,
    'category': 9,
    'type': 'boolean'
}
response = requests.get(url, params)
data = response.json()

question_data =[]

for numbers in range(len(data["results"])):
    q_dict = {}
    text=data["results"][numbers]['question']
    answer = data["results"][numbers]['correct_answer']
    q_dict["text"] = text
    q_dict["answer"] = answer
    question_data.append(q_dict)

