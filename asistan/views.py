# import google.generativeai as genai
# import PIL.Image
# import base64
# import threading
# import queue
# import requests
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# # Google API Anahtarını Tanımla
# API_KEY = "AIzaSyCAXB_dpcnWNSmyQYtrnwh1dopd_wFUP20"
# genai.configure(api_key=API_KEY)

# def text_to_speech(ai_response, audio_queue):
#     """AI yanıtını ResponsiveVoice API ile ses dosyasına çevir ve Base64 olarak kuyruğa ekle"""
#     url = "https://code.responsivevoice.org/responsivevoice.js?key=dMVIIAvc"
#     params = {"t": ai_response, "tl": "tr", "sv": "Google Türkçe", "vn": "tr", "engine": "responsive"}
#     response = requests.get(url, params=params)
    
#     if response.status_code == 200:
#         audio_base64 = base64.b64encode(response.content).decode("utf-8")
#         audio_queue.put(audio_base64)
#     else:
#         audio_queue.put(None)


# @csrf_exempt
# def speech_to_text(request):
#     """Kullanıcının metin, ses veya resim girişine göre AI yanıtını döndür"""
#     user_text = request.POST.get("input_girdisi", "").strip()
#     image_file = request.FILES.get("imageUpload")

#     if user_text:  # Kullanıcı metin girdiyse
#         model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # AI Modeli
#         response = model.generate_content(user_text)
#         ai_response = response.text
#         return JsonResponse({"text": ai_response})
    
#     elif image_file:  # Kullanıcı resim yüklediyse
#         try:
#             image = PIL.Image.open(image_file)
#             model = genai.GenerativeModel(model_name="gemini-1.5-pro")  # Modeli "gemini-1.5-pro" olarak belirledik
#             response = model.generate_content(["Resimde ne olduğunu anlat", image])
#             return JsonResponse({"text": response.text})
#         except Exception as e:
#             return JsonResponse({"error": f"Resim işlenirken hata oluştu: {str(e)}"})
    
#     else:  # Kullanıcı ses girdisi yaptıysa
#         import speech_recognition as sr
#         recognizer = sr.Recognizer()
#         with sr.Microphone() as source:
#             recognizer.adjust_for_ambient_noise(source)
#             print("Konuşmayı dinliyorum...")
#             audio = recognizer.listen(source)
        
#         try:
#             user_text = recognizer.recognize_google(audio, language="tr-TR")
#             model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # AI Modeli
#             response = model.generate_content(user_text)
#             ai_response = response.text
            
#             # Yanıtı sesli formata dönüştür
#             audio_queue = queue.Queue()
#             thread = threading.Thread(target=text_to_speech, args=(ai_response, audio_queue))
#             thread.start()
#             thread.join()
            
#             audio_base64 = audio_queue.get()
#             return JsonResponse({"text": ai_response, "audio": audio_base64})
        
#         except sr.UnknownValueError:
#             return JsonResponse({"error": "Ses anlaşılamadı."})
#         except sr.RequestError:
#             return JsonResponse({"error": "Google servislerine erişilemiyor."})








# import google.generativeai as genai
# import PIL.Image
# import base64
# import threading
# import queue
# import requests
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# from google import genai
# from google.genai import types

# # Google API Anahtarını Tanımla
# client = genai.Client(api_key="AIzaSyCAXB_dpcnWNSmyQYtrnwh1dopd_wFUP20") 
# API_KEY = "AIzaSyCAXB_dpcnWNSmyQYtrnwh1dopd_wFUP20"

# client = genai.Client(api_key="AIzaSyCAXB_dpcnWNSmyQYtrnwh1dopd_wFUP20") 
# def text_to_speech(ai_response, audio_queue):
#     """AI yanıtını ResponsiveVoice API ile ses dosyasına çevir ve Base64 olarak kuyruğa ekle"""
#     url = "https://code.responsivevoice.org/responsivevoice.js?key=dMVIIAvc"
#     params = {"t": ai_response, "tl": "tr", "sv": "Google Türkçe", "vn": "tr", "engine": "responsive"}
#     response = requests.get(url, params=params)
    
#     if response.status_code == 200:
#         audio_base64 = base64.b64encode(response.content).decode("utf-8")
#         audio_queue.put(audio_base64)
#     else:
#         audio_queue.put(None)
# @csrf_exempt
# def speech_to_text(request):
#     """Kullanıcının metin, ses, resim veya dosya girişine göre AI yanıtını döndür"""
#     user_text = request.POST.get("input_girdisi", "").strip()
#     image_file = request.FILES.get("imageUpload")
#     file_file = request.FILES.get("fileUpload")  # Yeni eklenen dosya

#     if user_text:  # Kullanıcı metin girdiyse
#         model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # AI Modeli
#         response = model.generate_content(user_text)
#         ai_response = response.text
#         return JsonResponse({"text": ai_response})
    
#     elif image_file:  # Kullanıcı resim yüklediyse
#         try:
#             image = PIL.Image.open(image_file)
#             model = genai.GenerativeModel(model_name="gemini-1.5-pro")  # Modeli "gemini-1.5-pro" olarak belirledik
#             response = model.generate_content(["Resimde ne olduğunu anlat", image])
#             return JsonResponse({"text": response.text})
#         except Exception as e:
#             return JsonResponse({"error": f"Resim işlenirken hata oluştu: {str(e)}"})
    
#     elif file_file:  # Kullanıcı dosya yüklediyse
#         try:
#             file_name = file_file.name
#             file_extension = file_name.split('.')[-1].lower()
#             file_content = file_file.read()

#             # Dosya tipine göre işlem yap
#             if file_extension == 'pdf':  # PDF dosyasını işliyoruz
#                 # PDF dosyasını bayt olarak okuyoruz
#                 doc_data = file_content

#                 # AI modeline PDF dosyasını ve promptu gönderiyoruz
#                 prompt = "Pdf'te ne olduğunu anlat..."
#                 response = client.models.generate_content(
#                     model="gemini-1.5-flash",
#                     contents=[
#                         types.Part.from_bytes(
#                             data=doc_data,
#                             mime_type='application/pdf',
#                         ),
#                         prompt
#                     ]
#                 )

#                 ai_response = response.text
#                 return JsonResponse({"text": ai_response})

#             else:
#                 return JsonResponse({"error": "Desteklenmeyen dosya türü."})

#         except Exception as e:
#             return JsonResponse({"error": f"Dosya işlenirken hata oluştu: {str(e)}"})
    
#     else:  # Kullanıcı ses girdisi yaptıysa
#         import speech_recognition as sr
#         recognizer = sr.Recognizer()
#         with sr.Microphone() as source:
#             recognizer.adjust_for_ambient_noise(source)
#             print("Konuşmayı dinliyorum...")
#             audio = recognizer.listen(source)
        
#         try:
#             user_text = recognizer.recognize_google(audio, language="tr-TR")
#             model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # AI Modeli
#             response = model.generate_content(user_text)
#             ai_response = response.text
            
#             # Yanıtı sesli formata dönüştür
#             audio_queue = queue.Queue()
#             thread = threading.Thread(target=text_to_speech, args=(ai_response, audio_queue))
#             thread.start()
#             thread.join()
            
#             audio_base64 = audio_queue.get()
#             return JsonResponse({"text": ai_response, "audio": audio_base64})
        
#         except sr.UnknownValueError:
#             return JsonResponse({"error": "Ses anlaşılamadı."})
#         except sr.RequestError:
#             return JsonResponse({"error": "Google servislerine erişilemiyor."})


import re
from django.shortcuts import render
import google.generativeai as genai
import PIL.Image
import base64
import threading
import queue
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from google import genai
from google.genai import types
import requests

# def process(request):
#     if request.method == 'POST':
#         user_text = request.POST.get("input_girdisi", "").strip()
#         client = genai.Client(api_key="AIzaSyCAXB_dpcnWNSmyQYtrnwh1dopd_wFUP20")
#         response = client.models.generate_content(
#             model="gemini-1.5-flash",
#             contents=user_text,
#         )
#         print(response.text)
#         return JsonResponse({'message': 'Mesaj gönderildi!', 'response': response.text})
#     else:
#         return JsonResponse({'error': 'Geçersiz istek'}, status=400)
    


from django.http import JsonResponse
from django.shortcuts import render
from google import genai
# API istemcisini başlat
API_KEY = "AIzaSyDsUwQdKaXHs06fLsgwXVz70QEaDL7vD3E"
client = genai.Client(api_key=API_KEY)
def process(request):
    if request.method == 'POST':
        user_text = request.POST.get('exampleFormControlTextarea', '').strip()
        image_file = request.FILES.get("imageUpload")
        file_file = request.FILES.get("fileUpload")
        client = genai.Client(api_key="AIzaSyDsUwQdKaXHs06fLsgwXVz70QEaDL7vD3E")

        if user_text:
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=user_text,
                )
                ai_result = re.sub(r"(\*|\*\*)", "", response.text)  # Gelen cevabı temizle
                print(ai_result)
                return JsonResponse({'ai_result': ai_result})
            except Exception as e:
                error_message = f'API isteği başarısız oldu: {str(e)}'
                print(error_message)
                return JsonResponse({'error': error_message}, status=500)

        elif image_file:
            try:
                image = PIL.Image.open(image_file)
                client = genai.Client(api_key="AIzaSyDsUwQdKaXHs06fLsgwXVz70QEaDL7vD3E")
                response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=["Resimde ne olduğunu anlat", image])
                
                # Görsel işleme kodunu buraya ekleyebilirsin
                return JsonResponse({"ai_result": response.text})
               # return JsonResponse({'message': f'{image_name} resmi başarıyla yüklendi.'})
            except Exception as e:
                return JsonResponse({'error': f'Görsel işlenirken hata oluştu: {str(e)}'}, status=500)

        elif file_file:
            try:
                client = genai.Client(api_key="AIzaSyDsUwQdKaXHs06fLsgwXVz70QEaDL7vD3E")  # Replace with your actual API key

                # Dosya işleme kodunu buraya ekleyebilirsin
                file_name = file_file.name
                file_extension = file_name.split('.')[-1].lower()
                file_content = file_file.read()

                # Dosya tipine göre işlem yap
                if file_extension == 'pdf':  # PDF dosyasını işliyoruz
                    # PDF dosyasını bayt olarak okuyoruz
                    doc_data = file_content

                    # AI modeline PDF dosyasını ve promptu gönderiyoruz
                    prompt = "Pdf'te ne olduğunu anlat..."
                    response = client.models.generate_content(
                        model="gemini-2.0-flash",
                        contents=[
                            types.Part.from_bytes(
                                data=doc_data,
                                mime_type='application/pdf',
                            ),
                            prompt
                        ]
                    )
                    ai_result = re.sub(r"(\*|\*\*)", "", response.text)  # Gelen cevabı temizle
                return JsonResponse({"ai_result": ai_result})
                
            except Exception as e:
                return JsonResponse({'error': f'Dosya işlenirken hata oluştu: {str(e)}'}, status=500)

        else:
            return JsonResponse({'error': 'Girdi verisi bulunamadı.'}, status=400)

    return render(request, 'chat_user_profil/chat_user_profil.html')



import re
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)

@csrf_exempt  # Eğer CSRF token kullanılmıyorsa bunu ekleyebilirsiniz
def process2(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Yalnızca POST isteği kabul edilir!'}, status=405)

    try:
        user_text = request.POST['exampleFormControlTextarea'].strip()
        if not user_text:
            return JsonResponse({'error': 'Boş metin gönderildi!'}, status=400)

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_text,
        )
        if not hasattr(response, "text"):
            return JsonResponse({'error': 'API yanıtı beklenen formatta değil!'}, status=500)

        ai_result = re.sub(r"(\*|\*\*)", "", response.text)  # Gelen cevabı temizle
        return JsonResponse({'ai_result': ai_result})

    except KeyError:
        return JsonResponse({'error': 'Eksik parametre: exampleFormControlTextarea'}, status=400)

    except Exception as e:
        logger.error(f"API isteği başarısız oldu: {str(e)}", exc_info=True)
        return JsonResponse({'error': 'Sunucu hatası oluştu, lütfen tekrar deneyin.'}, status=500)
