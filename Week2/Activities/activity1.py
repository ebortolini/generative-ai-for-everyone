from llm import get_response

prompt = '''
    Classify the following review 
    as having either a positive or
    negative sentiment:

    The banana pudding was really tasty!
'''

response = get_response(prompt)
print(response)