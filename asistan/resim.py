from PIL import Image
import google.generativeai as genai  # 'genai' olarak import etmeniz gerekebilir

# API anahtarını doğru şekilde girin
genai.configure(api_key="AIzaSyCAXB_dpcnWNSmyQYtrnwh1dopd_wFUP20")

image = Image.open("/path/to/organ.png")

# Modeli ve içerikleri doğru bir şekilde kullanın
response = genai.generate_content(
    model="gemini-2.0-flash", 
    contents=[image, "Tell me about this instrument"]
)

print(response.text)
