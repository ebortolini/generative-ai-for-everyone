from llm import get_response
from collections import Counter

all_reviews = [
    'The mochi is excellent!',
    'Best soup dumplings I have ever eaten.',
    'Not worth the 3 month wait for a reservation.',
    'The colorful tablecloths made me smile!',
    'The pasta was cold.'
]

all_sentiments = []
for review in all_reviews:
    prompt = f'''
        Classify the following review 
        as having either a positive or
        negative sentiment. State your answer
        as a single word, either "positive" or
        "negative":

        {review}
        '''
    response = get_response(prompt)
    all_sentiments.append(response)

sentiment_counts = Counter(all_sentiments)


print(f"There are {sentiment_counts['positive']} positive and {sentiment_counts['negative']} negative reviews.")