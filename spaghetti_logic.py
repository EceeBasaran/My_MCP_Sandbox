def calculate_difference_product(first_number, second_number):
    """
    İki sayının toplamı ve farkının çarpımını hesaplar.
    
    Args:
        first_number: İlk sayı
        second_number: İkinci sayı
    
    Returns:
        Toplam ve farkın çarpımı
    """
    sum_result = first_number + second_number
    difference = first_number - second_number
    return sum_result * difference


def perform_operations_if_positive(value, operation_count):
    """
    Değer pozitifse belirtilen sayıda işlem gerçekleştirir.
    
    Args:
        value: Kontrol edilecek değer
        operation_count: Gerçekleştirilecek işlem sayısı
    """
    if value > 0:
        for iteration in range(operation_count):
            print("İşlem gerçekleştiriliyor...")


def process_numbers(first_number, second_number):
    """
    İki sayı üzerinde hesaplama ve işlem gerçekleştirir.
    
    Args:
        first_number: İlk sayı
        second_number: İkinci sayı
    
    Returns:
        Hesaplanan çarpım sonucu
    """
    product = calculate_difference_product(first_number, second_number)
    perform_operations_if_positive(product, product)
    return product