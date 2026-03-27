def divide_numbers(numbers):
    result = []
    for i in range(len(numbers)):
        # Sıfıra bölme hatasını kontrol ediyoruz
        if numbers[i] == 0:
            result.append("Hata: Sifira bolunemez")
        else:
            res = 100 / numbers[i]
            result.append(res)
    return result

# Test ediyoruz
print(divide_numbers([10, 5, 0]))