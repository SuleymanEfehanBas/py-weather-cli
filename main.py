import requests

API_KEY = ("66ca246726b250aef5d590c5df783e7e")

def hava_durumu_getir(sehir):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={API_KEY}&units=metric&lang=tr"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        print("Şehir bulunamadı, lütfen doğru isim giriniz.")
    else:
        print(f"{data['name']} için hava durumu:")
        print(f"Sıcaklık: {data['main']['temp']} °C")
        print(f"Durum: {data['weather'][0]['description']}")
        print(f"Nem: {data['main']['humidity']}%")

def main():
    sehir = input("Hava durumunu öğrenmek istediğiniz şehir: ")
    hava_durumu_getir(sehir)

if __name__ == "__main__":
    main()
