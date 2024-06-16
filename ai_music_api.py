import json
import requests


class api:
    def __init__(self):
        self.res_json = {}
        self.api_url = "https://udioapi.pro/api/generate" 
        self.prompt_json = {
            "title": "",
            "prompt": "",
            "gpt_description_prompt": "",
            "custom_mode": 'false',  
            "make_instrumental": 'false',
            "model": "chirp-v3.0", 
            "continue_clip_id": "",             
            "continue_at": "", 
            "callback_url":"",  
            "token":"w3DQCckfZ_G8Z36bXez5u"         
        }
         
    def create(self,
        title = '',
        prompt = '',
        gpt_description_prompt = 'pop',
        custom_mode = False,
        make_instrumental = False,
        model = 'chirp-v3.0',    
        continue_clip_id = '',
        continue_at = '', 
        callback_url = ''          
    ):

        self.prompt_json['title'] = title
        self.prompt_json['prompt'] = prompt
        self.prompt_json['gpt_description_prompt'] = gpt_description_prompt
        self.prompt_json['custom_mode'] = custom_mode
        self.prompt_json['make_instrumental'] = make_instrumental
        self.prompt_json['model'] = model 
        self.prompt_json['continue_clip_id'] = continue_clip_id
        self.prompt_json['continue_at'] = continue_at
        self.prompt_json['callback_url'] = callback_url

    def token(self, token):
        self.prompt_json['token'] = token

    def ai_requsts(self):
                
        res = requests.post(url=self.api_url, json = self.prompt_json)

        if res.json() == {'message': 'prompt too long'}:
            print('Длина промпта привышает норму')
            pass
        else:
            self.res_json = res.json() 
            print(self.res_json)           
        
     
    def res_music(self):
        res_api_url = 'https://udioapi.pro/api/feed?workId='
        
        
        res_api_json = requests.post(url=f'{ res_api_url }{ self.res_json['workId'] }')
        # res_api_json = requests.post(url=f'{ res_api_url }RSKUs3mqZ8X2YPz0IHTw-')

        print(res_api_json.json())
        
        info = json.loads(res_api_json.json()['data']['1']['info'])['data']['data']

        
        audio_url_0 = info[0]['audio_url']
        audio_url_1 = info[1]['audio_url']
        
        return {
            'title': info[0]['title'],
            'audio_url_0': audio_url_0,
            'audio_url_1': audio_url_1,
        }
        
        # print(info['audio_url'])

def test():
    ap = api()
    # ap.create('заголовак' , 'Открытыйкод,чтосияетсветом,Ты-моямечта,мойидеальныйсвет.')
    
    ap.res_music()
    # ap.ai_requsts()
    # print(ap.prompt_json)

if __name__ == "__main__":
    test()
