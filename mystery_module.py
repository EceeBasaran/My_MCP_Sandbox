import math

def calculate_circle_area(radius):
    """
    Verilen yariçapa göre bir dairenin alanini hesaplar.
    Formül: pi * r^2
    
    Args:
        radius (float): Dairenin yariçapi.
        
    Returns:
        float: Dairenin toplam alani.
    """
    if radius < 0:
        return "Hata: Yariçap negatif olamaz!"
        
    area = math.pi * (radius ** 2)
    return area

# Test edelim
print(f"Yariçapi 5 olan dairenin alani: {calculate_circle_area(5)}")