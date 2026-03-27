import os

def get_connection():
    api_key = os.getenv("MY_API_KEY")
    if not api_key:
        return "Hata: API anahtari bulunamadi! Lütfen ortam degiskenlerini kontrol edin."
    return f"Baglanti basarili: {api_key[:4]}***"

print(get_connection())