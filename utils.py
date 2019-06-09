import os
from gnewsclient import gnewsclient

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "mykey.json"

import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "newsbot-vpflwf"
client=gnewsclient.NewsClient(max_results=3)

print(client.topics)
def get_news(parameters):
    client.topic=parameters.get('news_type')
    client.language=parameters.get('language')
    client.location=parameters.get('geo_country',' ')
    #print(parameters)
    return client.get_news()



def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    print(text_input)
    query_input = dialogflow.types.QueryInput(text=text_input)
    print(query_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

def fetch_reply(msg,session_id):
    response=detect_intent_from_text(msg,session_id)
    
    if response.intent.display_name =='get_news':
        #return "Ok,I will show you news {} ".format(dict(response.parameters)) 
        news=get_news(dict(response.parameters))
        print(news)
        news_str='here is ur msg: '
        for row in news:
            news_str+="\n\n{}\n\n{}\n\n".format(row['title'],row['link'])
        return news_str

    else:
        return response.fulfillment_text    