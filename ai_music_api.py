import json
import time
import requests


class api:
    def __init__(self):
        self.res_json = {}
        self.api_url = "https://udioapi.pro/api/generate" 
        self.prompt_json = {
            "title": "",
            "prompt": "",
            "gpt_description_prompt": "pop",
            "custom_mode": 'false',  
            "make_instrumental": 'false',
            "model": "chirp-v3.0", 
            "continue_clip_id": "",             
            "continue_at": "", 
            "callback_url":"",  
            "token":"aXVWQ6NBbpv7s8zOCyd94"         
        }
         
    def create(self,
        title = '',
        prompt = '',
        custom_mode = False,
        make_instrumental = False,
        model = 'chirp-v3.0',    
        continue_clip_id = '',
        continue_at = '', 
        callback_url = ''          
    ):

        self.prompt_json['title'] = title
        self.prompt_json['prompt'] = prompt
        self.prompt_json['custom_mode'] = custom_mode
        self.prompt_json['make_instrumental'] = make_instrumental
        self.prompt_json['model'] = model 
        self.prompt_json['continue_clip_id'] = continue_clip_id
        self.prompt_json['continue_at'] = continue_at
        self.prompt_json['callback_url'] = callback_url

    def token(self,):
        email_json = {"userEmail":"hamzatganukae@gmail.com"}
        token_rec = requests.post(url="https://udioapi.pro/api/token-g", json=email_json).json()
        self.prompt_json['token'] = token_rec['token']
        print(self.prompt_json['token'])
        
            # self.prompt_json['token'] = token
            # print(11)

    def gpt_prompt(self, gpt_description_prompt):
        self.prompt_json['gpt_description_prompt'] = gpt_description_prompt

        print(
            self.prompt_json['gpt_description_prompt']
        )

    def ai_requsts(self):                
        res = requests.post(url=self.api_url, json = self.prompt_json)

        if res.json() == {'message': 'prompt too long'}:
            print('Длина промпта привышает норму')
            pass
        else:
            self.res_json = res.json() 
            print(self.res_json)           
        
     
    def res_music(self):
        # time.sleep(90)
        print("запрос")
                
        res_api_url = 'https://udioapi.pro/api/feed?workId='

        while True:
            res_api_json = requests.post(url=f'{ res_api_url }{ self.res_json['workId'] }').json()
            # res_api_json = requests.post(url=f'{ res_api_url }KNH2b7uhXT7lvrZnxPRWG').json()
            
            try:
                if json.loads(res_api_json['data'][-1]['info'])['data']['data'][0]['audio_url'] != '':
                    
                    info =  json.loads(res_api_json['data'][-1]['info'])['data']['data'][0]  
                    audio_url_0 = info['audio_url']
                    audio_url_1 = info['audio_url']
                    image_url = info['image_url']
            
                    return {
                           'title': info['title'],
                           'audio_url_0': audio_url_0,
                           'audio_url_1': audio_url_1,
                           'image_url': image_url,
                            }
                else:
                    time.sleep(60)
            except KeyError:
                time.sleep(60)            
                    
        # info = json.loa(res_api_json.json()['data']['1']['info'])['data']['data']
               
        # print(info['audio_url'])

def test():
    ap = api()
    ap.token()
    ap.create('заголовак' ,input("Введи текст песни  ") )
    ap.ai_requsts()
    print(ap.res_music())
    
    
if __name__ == "__main__":
    test()
