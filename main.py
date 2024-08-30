from deep_translator import GoogleTranslator
def translateFunc(text, targetLanguage):
    try:
        translator = GoogleTranslator(source='auto', target=targetLanguage)
        translatedText = translator.translate(text)
        return translatedText
    except Exception as e:
        return f"Çeviri işlemi sırasında bir hata oluştu: {e}"
def main():
    print("Basit çeviri uygulamasına hoşgeldiniz!")
    originText = input("Çevirmek istediğiniz metni giriniz: ")
    targetLanguage = input("Hedef dilin kodunu girin (örn. İngilizce için 'en', Çince için 'zh-CN'): ")
    translatedText = translateFunc(originText, targetLanguage)
    print(f"Çevrilmiş metin: {translatedText}")
if __name__ == "__main__":
    main()