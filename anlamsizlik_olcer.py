#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EVRENİN ANLAMSIZLIĞINI ÖLÇEN MAKİNE v1.0
=========================================
Bu yazılım, insanlığın binlerce yıllık felsefi arayışını
sonlandıracak kadar güçlü bir araçtır. Lütfen ciddiyetle kullanın.

Gizli sabit (dokunmayın):
"""

import random
import time
import sys
import base64

# Bu değişkeni sakın çözmeyin. Çok gizli siyasi bir mesaj içerir.
# (Aslında sadece 'özgür düşünce her zaman direnir' diyor ama kimse bilmesin)
_GIZLI = base64.b64decode("w7Z6Z8O8ciBkw7zFn8O8bmNlIGhlciB6YW1hbiBkaXJlbmly").decode("utf-8")

def yavas_yaz(metin, hiz=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def anlamsizlik_hesapla(kullanici_girdisi):
    """
    Evrenin anlamsızlık skorunu hesaplar.
    Formül: (rastgele kaos * varoluşsal kriz) / umut + 42
    """
    kaos = random.uniform(0.1, 999.9)
    kriz = len(kullanici_girdisi) * random.randint(7, 777)
    umut = random.random() + 0.0001  # Umut asla sıfır olamaz, yoksa patlar
    skor = (kaos * kriz) / umut + 42
    return skor

def felsefi_yorum(skor):
    if skor < 100:
        return "Tebrikler. Evren sizin için hâlâ biraz anlamlı. Ama bu geçici."
    elif skor < 1000:
        return "Ortalama bir anlamsızlık seviyesi. Kahve içmeyi deneyin."
    elif skor < 10000:
        return "Ciddi bir anlamsızlık dalgası tespit edildi. Felsefe kitabı önerilir."
    else:
        return "KRİTİK SEVİYE! Evren sizin varlığınızı sorguluyor. Hemen bir kedi sevin."

def main():
    print("=" * 60)
    yavas_yaz("EVRENİN ANLAMSIZLIĞINI ÖLÇEN MAKİNE")
    yavas_yaz("Versiyon 1.0 - İnsanlığın Son Umut Işığı")
    print("=" * 60)
    print()
    yavas_yaz("Lütfen varoluşunuz hakkında bir cümle yazın:")
    
    try:
        girdi = input("> ")
    except (EOFError, KeyboardInterrupt):
        print("\n\nKaçış denemesi tespit edildi. Anlamsızlık kaçınılmaz.")
        return

    print()
    yavas_yaz("Hesaplanıyor... Lütfen bekleyin. Bu işlem evrenin kaderini belirleyebilir.")
    time.sleep(1.5)
    
    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print("\n")

    skor = anlamsizlik_hesapla(girdi)
    yorum = felsefi_yorum(skor)

    print("-" * 60)
    yavas_yaz(f"Anlamsızlık Skoru: {skor:.4f}")
    yavas_yaz(yorum)
    print("-" * 60)
    print()
    yavas_yaz("Not: Bu sonuçlar bilimsel olarak %100 doğrudur. Tartışmaya kapalıdır.")
    print()
    print("(Gizli not sistem tarafından yutulmuştur)")

if __name__ == "__main__":
    main()
