import tkinter as tk
from tkinter import messagebox
import random
import copy
import sys
from PIL import Image, ImageTk 

# --- Dosyaları Import Etme ---

try:
    from ulkeler import ULKE_ARALIKLARI
    from sorular import TUM_SORULAR
except ImportError as e:
    print(f"Hata: Gerekli dosya bulunamadı. Lütfen ulkeler.py ve sorular.py dosyalarının bu klasörde olduğundan emin olun. Hata: {e}")
    # Eğer dosyalar bulunamazsa uygulamayı durdur
    sys.exit()


# --- Temel Ayarlar ---
SECILEN_SORU_SAYISI = 10

class UlkeKarakterTesti(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hangi Ülke Karakterisin?")
        self.geometry("600x600") # Görsel için pencere boyutu artırıldı
        
        # Tkinter'ın çöp toplamasını engellemek için görsel referansını tutar
        self.flag_photo = None 
        
        # --- Buton Stili: Beyaz Zemin, Siyah Yazı ---
        self.BUTTON_STYLE = {
            'bg': 'white',
            'fg': 'black',
            'activebackground': '#ddd',
            'activeforeground': 'black',
            'font': ('Arial', 10, 'bold'),
            'width': 60, 
            'wraplength': 400 
        }
        
        self.reset_test()

    def hazirlik_yap(self, soru_havuzu):
        """
        1. 100 sorudan 10 tanesini rastgele seçer.
        2. Şıklarını (metin ve puan) birleştirip karıştırır.
        """
        if len(soru_havuzu) < SECILEN_SORU_SAYISI:
            messagebox.showerror("Hata", "Soru havuzunda yeterli soru yok!")
            sys.exit()

        # Rastgele 10 soru seç
        secilen_sorular = random.sample(soru_havuzu, SECILEN_SORU_SAYISI)
        hazir_test = []
        
        for soru_obj_original in secilen_sorular:
            soru_obj = copy.deepcopy(soru_obj_original)
            
            # Sorular.py formatından listeleri çıkar
            original_siklar = list(soru_obj["secenekler"].keys())
            original_puanlar = list(soru_obj["secenekler"].values())
            
            # Şıklar ve puanlar listesini birleştir, karıştır ve ayır
            birlesik_liste = list(zip(original_siklar, original_puanlar))
            random.shuffle(birlesik_liste)
            karismis_siklar, karismis_puanlar = zip(*birlesik_liste)
            
            hazir_test.append({
                "soru": soru_obj["soru"],
                "siklar": list(karismis_siklar),
                "puanlar": list(karismis_puanlar)
            })
            
        return hazir_test

    def reset_test(self):
        """Testi sıfırlar ve yeni bir 10 soruluk test başlatır."""
        self.mevcut_soru_index = 0
        self.toplam_puan = 0
        self.test_sorulari = self.hazirlik_yap(TUM_SORULAR)
        
        for widget in self.winfo_children():
            widget.destroy()
            
        self.create_widgets()

    def create_widgets(self):
        # Soru Metni
        self.soru_label = tk.Label(self, text="", wraplength=550, font=('Arial', 12))
        self.soru_label.pack(pady=20, padx=10)
        
        # Şıkların tutulacağı Frame
        self.siklar_frame = tk.Frame(self)
        self.siklar_frame.pack(pady=10)
        
        self.secenek_butonlari = []
        num_siklar = 5 
        if self.test_sorulari and self.test_sorulari[0].get("siklar"):
             num_siklar = len(self.test_sorulari[0]["siklar"])
             
        for i in range(num_siklar):
            # Beyaz/Siyah stil uygulandı
            btn = tk.Button(self.siklar_frame, text="", **self.BUTTON_STYLE, 
                            command=lambda i=i: self.cevap_secildi(i))
            btn.pack(pady=5)
            self.secenek_butonlari.append(btn)
            
        self.goster_soru()

    def goster_soru(self):
        """Mevcut soruyu ekranda gösterir."""
        if self.mevcut_soru_index < SECILEN_SORU_SAYISI:
            soru_obj = self.test_sorulari[self.mevcut_soru_index]
            
            self.soru_label.config(text=f"Soru {self.mevcut_soru_index + 1}/{SECILEN_SORU_SAYISI}: {soru_obj['soru']}")
            
            for i, text in enumerate(soru_obj['siklar']):
                self.secenek_butonlari[i].config(text=text)
                self.secenek_butonlari[i].puan_degeri = soru_obj['puanlar'][i] 
                
        else:
            self.sonuclari_goster()

    def cevap_secildi(self, secilen_buton_index):
        """Bir şık seçildiğinde çalışır."""
        secilen_puan = self.secenek_butonlari[secilen_buton_index].puan_degeri
        self.toplam_puan += secilen_puan
        
        self.mevcut_soru_index += 1
        self.goster_soru()

    def sonuclari_goster(self):
        """Test bittiğinde sonuçları hesaplar, görseli ve sonuçları gösterir."""
        for widget in self.winfo_children():
            widget.destroy()
            
        sonuc_ulke = None
        for min_puan, max_puan, ulke_ad, bayrak, aciklama, resim_yolu in ULKE_ARALIKLARI:
            if min_puan <= self.toplam_puan <= max_puan:
                sonuc_ulke = (ulke_ad, bayrak, aciklama, resim_yolu) 
                break
        
        if sonuc_ulke is None:
             sonuc_ulke = ("Bilinmeyen Karakter", "❓", f"Puanınız mevcut aralıklara denk gelmedi. (Puanınız: {self.toplam_puan})", "")

        ulke_ad, bayrak, aciklama, resim_yolu = sonuc_ulke
        
        # GÖRSEL YÜKLEME VE GÖSTERME KISMI (Pillow Kullanılarak)
        if resim_yolu:
            try:
                # Görseli yükle, boyutlandır (150x100) ve referansı tut
                img = Image.open(resim_yolu)
                img = img.resize((150, 100), Image.Resampling.LANCZOS)
                self.flag_photo = ImageTk.PhotoImage(img) 
                
                flag_label = tk.Label(self, image=self.flag_photo)
                flag_label.pack(pady=10)

            except FileNotFoundError:
                tk.Label(self, text=f"Hata: Görsel dosyası bulunamadı! Lütfen 'images' klasörünü kontrol edin.", fg="red", font=('Arial', 10)).pack(pady=5)
            except Exception as e:
                tk.Label(self, text=f"Görsel yüklenirken hata oluştu: {e}", fg="red", font=('Arial', 10)).pack(pady=5)

        # Sonuç Başlığı
        tk.Label(self, text=f"Tebrikler! Sonucunuz: {ulke_ad} {bayrak}", font=('Arial', 16, 'bold')).pack(pady=15)
        tk.Label(self, text=f"Toplam Puanınız: {self.toplam_puan}", font=('Arial', 12)).pack(pady=5)
        tk.Label(self, text=aciklama, wraplength=550, font=('Arial', 10)).pack(pady=10, padx=10)
        
        # Yeniden Başlat Butonu
        tk.Button(self, text="Yeniden Başla", **self.BUTTON_STYLE, command=self.reset_test).pack(pady=20)


if __name__ == "__main__":
    app = UlkeKarakterTesti()

    app.mainloop()
