import os
from dotenv import load_dotenv
import openai
from slugify import slugify

load_dotenv()

openai.api_key = os.environ.get('OPEN_AI_KEY')
completion = openai.ChatCompletion()

f = open("./ideas.md", "r")

folder = ''
subfolder = ''

responses = 0

for line in f:
    if (line.startswith("## ")):
        folder = line[3:line.find("[http")]

    if (line.startswith("#### ")):
        subfolder = line[5:line.find("[http")]

    if (line.startswith("- ")):
        prompt = line[2:line.find("[http")]
        chat_log = [{
            'role': 'system',
            'content': 'You are a programmer. You do not return any text except for python code.'
        }, {
            'role': 'user',
            'content': '''
                Create a python script that ''' + prompt + '''\n
                You may use any existing python libraries necessary to write the script. 
                Make sure to comment your code, and make sure that it is of a high quality, and works well.
                Every single program should be runnable using the command "python task.py".
                It should not need any arguments, and if user input is necessary, get it by asking the user in the script.
            '''
        }]

        response = completion.create(model="gpt-3.5-turbo", messages=chat_log)
        answer = response.choices[0]['message']['content']

        path = slugify(folder) + '/' + slugify(subfolder)
        print(path)
        if not os.path.exists('rerun/' + folder + '/' + subfolder):
            os.makedirs('rerun/' + path, exist_ok=True)

        new_f = open('rerun/' + path + '/' + slugify(prompt[:60]) + ".py", "w")
        new_f.write(answer)
        responses += 1
        print(responses)
        new_f.close()

f.close()
