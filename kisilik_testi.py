import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk

# --- Ülke bilgileri (bayrak, açıklama, görsel yolu) ---
ulke_araliklari = [
    (7, 9, "Norveç", "🇳🇴",
     "Sen sakin, doğayla uyumlu olan ve iç huzura önem veren birisin.\n"
     "Kendinle vakit geçirmekten keyif alıyorsun.\n"
     "Gösteriş meraklısı değilsin, minimalist olmak senin tarzın.\n"
     "İstikrar ve planlama senin için her daim önemlidir.",
     "images/norvec.png"),

    (10, 12, "Japonya", "🇯🇵",
     "Disiplinli, çalışkan ve detay odaklısın.\n"
     "Hatta o kadar detay odaklısın ki ara sıra kendini kaybedebiliyorsun.\n"
     "Planlı çalışmak senin doğanda var.\n"
     "Hedeflerine ulaşmada her daim kararlı ve sarsılmazsın.",
     "images/japonya.png"),

    (13, 15, "Almanya", "🇩🇪",
     "Planlı, sistematik ve güvenilir bir yapın var.\n"
     "Her zaman işleri zamanında bitirmeyi seversin.\n"
     "Yeni şeyler öğrenmekten keyif alırsın.\n"
     "Kendin kadar mükemmel birilerini bulmak zor olmalı.",
     "images/almanya.png"),

    (16, 18, "Fransa", "🇫🇷",
     "Bu zerafet... Bu şıklık... Bu gösteriş...\n"
     "Sen oldukça duygusal birisin.\n"
     "Sanat ve estetik senin hayatında önemli bir yer tutuyor.\n"
     "Romantik ve yaratıcı yönlerin her daim insanların dikkatini çekiyor.",
     "images/fransa.png"),

    (19, 21, "Türkiye", "🇹🇷",
     "Sıcakkanlı ve dayanıklısın.\n"
     "Bağlılık senin doğanda var.\n"
     "Arkadaşlarına ve ailene her zaman destek olursun.\n"
     "Hayata karşı esnek ama kararlı bir yaklaşımın vardır.\n"
     "Ah keşke kendindeki potansiyeli görebilsen...",
     "images/turkiye.png"),

    (22, 24, "İtalya", "🇮🇹",
     "Tutkulu, yaratıcı ve hayatı dolu dolu yaşayan birisin.\n"
     "Güzel anlar ve etkileyici deneyimler senin için çok önemli.\n"
     "Hayata renk katmayı seviyorsun.\n"
     "Bazen sadece anı yaşamak gerektiğini en iyi sen biliyorsun.",
     "images/italya.png"),

    (25, 27, "Hindistan", "🇮🇳",
     "Ruhani, sezgisel ve içsel uyuma önem veren birisin.\n"
     "Meditasyon ve manevi değerler senin hayatında büyük yer tutar.\n"
     "Derin düşünmeyi ve kendini keşfetmeyi seversin.\n"
     "Biraz gizemli bir yanın var, hadi itiraf et!",
     "images/hindistan.png"),

    (28, 30, "Rusya", "🇷🇺",
     "Güçlü, duygusal derinliğe sahip ve dirençli birisin.\n"
     "Zorluklar karşısında pes etmezsin.\n"
     "Derin duygularını genellikle içten yaşarsın.\n"
     "Sert görünsen de içten içe çok duygusalsın.",
     "images/rusya.png"),

    (31, 33, "Brezilya", "🇧🇷",
     "Neşeli, enerjik ve hayat dolu bir kişiliğin var!\n"
     "Sosyal ve arkadaş canlısı olduğundan bahsetmeye gerek bile yok!\n"
     "Her ortamda enerjin dikkatleri kolaylıkla üzerine çekiyor.\n"
     "Hayatı dolu dolu yaşamayı seviyorsun.",
     "images/brezilya.png"),

    (34, 35, "ABD", "🇺🇸",
     "Girişimci, özgüvenli ve fırsatları yakalamayı bilen birisin.\n"
     "Yeni şeyler denemekten çekinmiyorsun ve lider ruhlusun.\n"
     "Bağımsızlık ve özgürlük senin hayat felsefen.\n"
     "Kimse sana ne yapacağını söyleyemez!\n"
     "'Ben demiştim.' demeyi seviyorsun.",
     "images/abd.png")
]

# --- 7 ADET SORU ---
sorular = [
    {"soru": "Bir iş yaparken nasıl davranırsın?", "secenekler": {
        "Yavaş ama emin adımlarla ilerlerim.": 1,
        "Planlı ve dikkatli çalışırım.": 2,
        "Her şeyin mükemmel olmasına özen gösteririm.": 3,
        "Hedefe en hızlı şekilde ulaşmaya çalışırım.": 4,
        "Biraz plansız ama hevesli davranırım.": 5
    }},
    {"soru": "Bir sorunla karşılaştığında ilk tepkini nasıl tanımlarsın?", "secenekler": {
        "Sakin kalırım ve düşünürüm.": 1,
        "Analiz eder, plan yaparım.": 2,
        "Sistemi düzeltmeye odaklanırım.": 3,
        "Enerjimle sorunu aşarım.": 4,
        "Duygusal olarak tepki veririm ama çabuk toparlarım.": 5
    }},
    {"soru": "Hafta sonu planını seç!", "secenekler": {
        "Doğada yalnız yürüyüş": 1,
        "Evde huzurlu bir gün": 2,
        "Kendimi geliştirecek bir aktivite": 3,
        "Arkadaşlarla dışarı çıkmak": 4,
        "Spontane bir macera!": 5
    }},
    {"soru": "Bir arkadaşının sana ihtiyacı olduğunda ne yaparsın?", "secenekler": {
        "Sakin bir şekilde dinlerim.": 1,
        "Mantıklı tavsiyeler veririm.": 2,
        "Hemen yardım planı yaparım.": 3,
        "Yanında olur, moral veririm.": 4,
        "Duygusal olarak destek olmaya çalışırım.": 5
    }},
    {"soru": "Senin için başarı nedir?", "secenekler": {
        "Huzurlu bir hayat yaşamak": 1,
        "İşini iyi yapıp saygı görmek": 2,
        "Yüksek hedeflere ulaşmak": 3,
        "Hayattan keyif almak": 4,
        "Yeni deneyimler kazanmak": 5
    }},
    {"soru": "Bir grup içindeyken genelde...", "secenekler": {
        "Dinleyen, sakin kişiyim.": 1,
        "Yönlendiren kişiyim.": 2,
        "Planlayan kişiyim.": 3,
        "Ortamı canlandıran kişiyim.": 4,
        "Spontane davranırım.": 5
    }},
    {"soru": "Kendini en çok hangi cümle tanımlar?", "secenekler": {
        "Sade bir yaşam beni mutlu eder.": 1,
        "Disiplinle her şey başarılır.": 2,
        "Analitik düşünmeyi severim.": 3,
        "Hayatın tadını çıkarmalıyım!": 4,
        "Ruhsal denge benim için önemli.": 5
    }}
]

class KisilikTesti:
    def __init__(self, root):
        self.root = root
        self.root.title("Bir Ülke Olsaydın Hangisi Olurdun?")
        self.root.geometry("650x620")
        self.root.config(bg="#f7f7f7")
        self.soru_index = 0
        self.toplam_puan = 0
        self.image_label = None
        self.acilis_ekrani()

    def acilis_ekrani(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        baslik = tk.Label(self.root, text="🌍 Bir Ülke Olsaydın Hangisi Olurdun?",
                          font=("Arial", 18, "bold"), bg="#f7f7f7")
        baslik.pack(pady=20)

        aciklama = (
            "Merhaba, gezgin!\n"
            "Bu test, kişilik özelliklerine göre seni en çok yansıtan ülkeyi bulur.\n\n"
            "Her soruda seni en iyi tanımlayan seçeneği seç.\n"
            "Testin sonunda, kişiliğini temsil eden ülkeyi bulacaksın!\n\n"
            "Hazırsan başlayalım!"
        )
        lbl = tk.Label(self.root, text=aciklama, font=("Arial", 12), wraplength=600, justify="center", bg="#f7f7f7")
        lbl.pack(pady=30)

        basla_btn = tk.Button(self.root, text="Teste Başla ▶", command=self.baslat,
                              font=("Arial", 13, "bold"), bg="#4a90e2", fg="white", relief="flat", width=18)
        basla_btn.pack(pady=20)

    def baslat(self):
        self.soru_index = 0
        self.toplam_puan = 0
        self.test_ekrani()

    def test_ekrani(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.soru_label = tk.Label(self.root, text="", font=("Arial", 14, "bold"),
                                   wraplength=600, justify="center", bg="#f7f7f7")
        self.soru_label.pack(pady=20)

        self.secim = tk.IntVar()
        self.secenek_butonlar = []

        for _ in range(5):
            rb = tk.Radiobutton(self.root, text="", variable=self.secim, value=0,
                                font=("Arial", 12), anchor="w", justify="left",
                                bg="#f7f7f7", selectcolor="#dfe7fd")
            rb.pack(fill="x", padx=40, pady=4)
            self.secenek_butonlar.append(rb)

        self.ileri_btn = tk.Button(self.root, text="İleri ➜", command=self.sonraki_soru,
                                   font=("Arial", 12, "bold"), bg="#4a90e2", fg="white", relief="flat", width=15)
        self.ileri_btn.pack(pady=25)

        self.soruyu_goster()

    def soruyu_goster(self):
        soru = sorular[self.soru_index]
        self.soru_label.config(text=f"Soru {self.soru_index + 1}/{len(sorular)}\n\n{soru['soru']}")
        self.secim.set(0)
        for i, (metin, puan) in enumerate(soru["secenekler"].items()):
            self.secenek_butonlar[i].config(text=metin, value=puan)

    def sonraki_soru(self):
        secilen_puan = self.secim.get()
        if not secilen_puan:
            messagebox.showwarning("Uyarı", "Lütfen bir seçenek seçin!")
            return

        self.toplam_puan += secilen_puan
        self.soru_index += 1

        if self.soru_index < len(sorular):
            self.soruyu_goster()
        else:
            self.sonucu_goster()

    def sonucu_goster(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # 🔹 Daha sade ülke seçimi
        secilen = None
        for alt, ust, u, b, a, p in ulke_araliklari:
            if alt <= self.toplam_puan <= ust:
                secilen = (u, b, a, p)
                break
        if not secilen:
            secilen = ("Bilinmiyor", "❓", f"Puan: {self.toplam_puan}", None)

        ulke, bayrak, aciklama, img_path = secilen

        sonuc_label = tk.Label(self.root, text="🌍 Test Sonucu", font=("Arial", 18, "bold"), bg="#f7f7f7")
        sonuc_label.pack(pady=10)

        bayrak_lbl = tk.Label(self.root, text=bayrak, font=("Arial", 80), bg="#f7f7f7")
        bayrak_lbl.pack(pady=5)

        ulke_lbl = tk.Label(self.root, text=ulke, font=("Arial", 22, "bold"), bg="#f7f7f7")
        ulke_lbl.pack(pady=5)

        if img_path and os.path.exists(img_path):
            img = Image.open(img_path)
            img = img.resize((180, 120), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            self.image_label = tk.Label(self.root, image=img, bg="#f7f7f7")
            self.image_label.image = img
            self.image_label.pack(pady=10)

        aciklama_lbl = tk.Label(self.root, text=aciklama, font=("Arial", 13), wraplength=550,
                                justify="center", bg="#f7f7f7")
        aciklama_lbl.pack(pady=10)

        yeniden_btn = tk.Button(self.root, text="🔁 Baştan Başla", command=self.acilis_ekrani,
                                font=("Arial", 12, "bold"), bg="#4a90e2", fg="white", relief="flat", width=16)
        yeniden_btn.pack(pady=15)

        cikis_btn = tk.Button(self.root, text="Kapat ✖", command=self.root.destroy,
                              font=("Arial", 11), bg="#ff5e5e", fg="white", relief="flat", width=10)
        cikis_btn.pack(pady=10)


# --- Uygulama başlat ---
root = tk.Tk()
app = KisilikTesti(root)
root.mainloop()
