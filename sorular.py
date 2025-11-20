# sorular.py

# --- 100 ADET SORU ---
# Soru formatı: {"soru": "...", "secenekler": {"Şık 1": Puan, "Şık 2": Puan, ...}}
TUM_SORULAR = [
    # -------------------------------------------------------------------------
    # BÖLÜM 1: MİZAC ve ENERJİ (1'den 20'ye kadar)
    # -------------------------------------------------------------------------
    {"soru": "Bir iş yaparken nasıl davranırsın?", "secenekler": {
        "Yavaş ama emin adımlarla ilerlerim.": 1,
        "Planlı ve dikkatli çalışırım.": 2,
        "Her şeyin mükemmel olmasına özen gösteririm.": 3,
        "Biraz plansız ama hevesli davranırım.": 4,
        "Hedefe en hızlı şekilde ulaşmaya çalışırım.": 5
    }},
    {"soru": "Bir sorunla karşılaştığında ilk tepkini nasıl tanımlarsın?", "secenekler": {
        "Sakin kalırım ve düşünürüm.": 1,
        "Analiz eder, plan yaparım.": 2,
        "Sistemi düzeltmeye odaklanırım.": 3,
        "Duygusal olarak tepki veririm ama çabuk toparlanırım.": 4,
        "Enerjimle sorunu aşarım.": 5
    }},
    {"soru": "Sana göre en önemli duygu hangisi?", "secenekler": {
        "Huzur.": 1,
        "Güven.": 2,
        "Hırs.": 3,
        "Aşk.": 4,
        "Neşe.": 5
    }},
    {"soru": "Bir fikre ne zaman ikna olursun?", "secenekler": {
        "İçime sindiği zaman.": 1,
        "Tüm verileri gördüğüm zaman.": 2,
        "Fikri beğendiğim zaman.": 3,
        "Fikir popüler olduğu zaman.": 4,
        "Sıra dışı ve ilginç olduğu zaman.": 5
    }},
    {"soru": "Nasıl öğrenmeyi seversin?", "secenekler": {
        "Tek başıma.": 1,
        "Yapılandırılmış bir ortamda.": 2,
        "Uzmanlardan.": 3,
        "Grup içinde.": 4,
        "Kaos içinde.": 5
    }},
    {"soru": "Bir müzik festivaline gittin, ne yaparsın?", "secenekler": {
        "Kenarda oturup müziğin tadını çıkarırım.": 1,
        "Sahneye en yakın yeri hedeflerim.": 2,
        "En popüler DJ'in performansını izlerim.": 3,
        "Grup arkadaşlarımla dans ederim.": 4,
        "Tanımadığım insanlarla sohbet eder, yeni şeyler denerim.": 5
    }},
    {"soru": "Harcamalarını yönetme tarzın nedir?", "secenekler": {
        "Çok az harcarım, minimalistim.": 1,
        "Bütçe yaparım ve buna uyarım.": 2,
        "Kaliteli ve marka ürünlere yatırım yaparım.": 3,
        "Deneyime harcarım (seyahat, yemek).": 4,
        "Para harcamaktan çekinmem, hayat kısa.": 5
    }},
    {"soru": "Hayatının merkezine neyi koyarsın?", "secenekler": {
        "Kendi iç huzurumu.": 1,
        "Geleceğimi ve kariyerimi.": 2,
        "Aşkı ve estetiği.": 3,
        "Aileyi ve dostluğu.": 4,
        "Özgürlüğü ve macerayı.": 5
    }},
    {"soru": "Bir tartışmada ne kadar katılımcısın?", "secenekler": {
        "Sessiz kalırım, dinlerim.": 1,
        "Mantıklı kanıtlar sunarım.": 2,
        "Duygusallığımı belli etmemeye çalışırım.": 3,
        "Tutkulu bir şekilde savunurum.": 4,
        "Sesi en çok çıkan ben olurum.": 5
    }},
    {"soru": "Seyahat için ideal rotan nedir?", "secenekler": {
        "Kuzeyin sessiz doğası.": 1,
        "Tarihi ve düzenli şehirler.": 2,
        "Sanatın ve modanın başkentleri.": 3,
        "Güneşli, sıcak ve tarihi yerler.": 4,
        "Büyük, kalabalık metropoller.": 5
    }},
    {"soru": "Zaman yönetimine ne kadar önem verirsin?", "secenekler": {
        "Çok rahattır, akışına bırakırım.": 1,
        "Çizelge yaparım ve buna uymaya çalışırım.": 2,
        "Dakiklik benim için kutsaldır.": 3,
        "Esnek olmayı severim.": 4,
        "Kuralları hiçe sayarım.": 5
    }},
    {"soru": "Stresle başa çıkma yöntemin nedir?", "secenekler": {
        "Meditasyon yaparım.": 1,
        "Çalışarak unuturum.": 2,
        "Kendime iyi bakarım (yemek, spor).": 3,
        "Dostlarımla konuşurum.": 4,
        "Enerjimi dışa vururum (spor, dans).": 5
    }},
    {"soru": "Giyim tarzın nasıldır?", "secenekler": {
        "Rahat ve basit.": 1,
        "Klasik ve resmi.": 2,
        "Şık ve trendlere uygun.": 3,
        "Renkli ve dikkat çekici.": 4,
        "Spor ve özgün.": 5
    }},
    {"soru": "Arkadaş çevrende seni en iyi tanımlayan özellik nedir?", "secenekler": {
        "Sessiz dinleyici.": 1,
        "Güvenilir organize edici.": 2,
        "Duygusal destek.": 3,
        "Hayat enerjisi kaynağı.": 4,
        "Risk alan lider.": 5
    }},
    {"soru": "Bir hediyeyi neye göre seçersin?", "secenekler": {
        "Pratik olmasına.": 1,
        "Uzun ömürlü olmasına.": 2,
        "Estetik olmasına.": 3,
        "Anıtsal olmasına.": 4,
        "Büyük ve gösterişli olmasına.": 5
    }},
    {"soru": "Hafta sonu planın ne olur?", "secenekler": {
        "Evde dinlenmek.": 1,
        "Kişisel gelişim veya bir hobiye odaklanmak.": 2,
        "Sosyal bir etkinliğe gitmek.": 3,
        "Aileyi veya geniş arkadaş grubunu toplamak.": 4,
        "Anlık bir yolculuğa çıkmak.": 5
    }},
    {"soru": "İş/Okul hayatında başarının sırrı nedir?", "secenekler": {
        "İç motivasyon.": 1,
        "Sıkı disiplin.": 2,
        "Doğru çevre.": 3,
        "Esneklik ve kararlılık.": 4,
        "Sürekli ilerleme.": 5
    }},
    {"soru": "Yeni bir insanla tanışırken ne hissedersin?", "secenekler": {
        "Çekingen.": 1,
        "Dikkatli.": 2,
        "Meraklı.": 3,
        "Rahat ve sıcakkanlı.": 4,
        "Heyecanlı.": 5
    }},
    {"soru": "Hayvan karakterin ne olurdu?", "secenekler": {
        "Baykuş (Sakin, Gözlemci).": 1,
        "Kunduz (Çalışkan, Yapılandıran).": 2,
        "Kuğu (Zarif, Duygusal).": 3,
        "Aslan (Lider, Tutkulu).": 4,
        "Yunus (Neşeli, Özgür).": 5
    }},
    {"soru": "Hangi aktivite seni en çok rahatlatır?", "secenekler": {
        "Doğada yürüyüş.": 1,
        "Kitap okumak.": 2,
        "Sanat galerisi gezmek.": 3,
        "Büyük bir yemek masasında sohbet.": 4,
        "Kalabalık bir partiye gitmek.": 5
    }},
    # -------------------------------------------------------------------------
    # BÖLÜM 2: KARAR VERME VE DÜZEN (21'den 40'a kadar)
    # -------------------------------------------------------------------------
    {"soru": "Karar verirken en çok neye güvenirsin?", "secenekler": {
        "Sezgilerime.": 1,
        "Verilere ve mantığa.": 2,
        "Uzman görüşlerine.": 3,
        "Kalabalığın eğilimine.": 4,
        "Kendi cesaretime.": 5
    }},
    {"soru": "Evin/Çalışma masanın düzeni nasıldır?", "secenekler": {
        "Sadece ihtiyacım olanlar vardır.": 1,
        "Her şeyin bir yeri vardır.": 2,
        "Estetik ve rahat olmalıdır.": 3,
        "Biraz dağınıktır ama aradığımı bulurum.": 4,
        "Yaratıcı kaos içindedir.": 5
    }},
    {"soru": "Bir projede lider misin, takipçi mi?", "secenekler": {
        "Takipçiyim, ama sessizce yönlendiririm.": 1,
        "Liderliği kabul ederim, plan yaparım.": 2,
        "Lider olurum ama estetik kısmı bende olmalı.": 3,
        "Takım oyuncusuyum, herkesle uyum sağlarım.": 4,
        "Doğal liderim, risk almayı severim.": 5
    }},
    {"soru": "Hayal kırıklığıyla nasıl baş edersin?", "secenekler": {
        "Kendime dönerim.": 1,
        "Çözüm odaklı yaklaşırım.": 2,
        "Bunu sanata veya tutkuya dönüştürürüm.": 3,
        "Ailemden/arkadaşlarımdan destek alırım.": 4,
        "Daha büyük hedefler koyarak unuturum.": 5
    }},
    {"soru": "Para senin için ne ifade eder?", "secenekler": {
        "Güvenlik.": 1,
        "Gelecek güvencesi.": 2,
        "Gösteriş ve yaşam kalitesi.": 3,
        "Yardım etme aracı.": 4,
        "Özgürlük aracı.": 5
    }},
    {"soru": "Başkalarının ne düşündüğü senin için ne kadar önemli?", "secenekler": {
        "Hiç önemli değil.": 1,
        "Profesyonel eleştiriler önemlidir.": 2,
        "Beğenilmek hoşuma gider.": 3,
        "Sevdiklerimin düşüncesi önemlidir.": 4,
        "Popülerlik ve itibar önemlidir.": 5
    }},
    {"soru": "Risk almayı sever misin?", "secenekler": {
        "Asla risk almam.": 1,
        "Hesaplı risk alırım.": 2,
        "Gerekirse estetik bir risk alırım.": 3,
        "Ailem için risk alabilirim.": 4,
        "Her zaman büyük riskler alırım.": 5
    }},
    {"soru": "En çok nerede vakit geçirmeyi seversin?", "secenekler": {
        "Kütüphaneler ve doğa.": 1,
        "Ofis ve derslikler.": 2,
        "Kafeler ve barlar.": 3,
        "Stadyumlar ve konserler.": 4,
        "Spor salonları ve açık alanlar.": 5
    }},
    {"soru": "Bir proje ne zaman biter?", "secenekler": {
        "Bitmesi gerektiği zaman.": 1,
        "Planladığım zaman.": 2,
        "Mükemmel olduğu zaman.": 3,
        "İşlevini yerine getirdiği zaman.": 4,
        "Yeni bir maceraya atılma zamanı geldiği zaman.": 5
    }},
    {"soru": "Seyahat ederken neyi tercih edersin?", "secenekler": {
        "Sessiz bir yerde tek kalmayı.": 1,
        "Turistik yerleri planlı gezmeyi.": 2,
        "Yerel kültürü deneyimlemeyi.": 3,
        "Spontane gelişen olayları.": 4,
        "Lüks ve konforlu seyahati.": 5
    }},
    {"soru": "Hangi mevsimi en çok seversin?", "secenekler": {
        "Kış (Huzur ve içe dönüklük).": 1,
        "Sonbahar (Sakinlik ve düzen).": 2,
        "İlkbahar (Yenilenme ve aşk).": 3,
        "Yaz (Enerji ve sosyallik).": 4,
        "Mevsimsiz, her anı dolu yaşarım.": 5
    }},
    {"soru": "Gelecekten korkar mısın?", "secenekler": {
        "Hayır, sadece anı yaşarım.": 1,
        "Evet, belirsizlik beni rahatsız eder.": 2,
        "Duygusal olarak bazen.": 3,
        "Hayır, her zorluğun üstesinden gelirim.": 4,
        "Hayır, sadece fırsatları görürüm.": 5
    }},
    {"soru": "Sosyal medyayla aran nasıl?", "secenekler": {
        "Çok az kullanırım.": 1,
        "Sadece gerekli bilgileri takip ederim.": 2,
        "Kendi şık ve estetik içeriklerimi paylaşırım.": 3,
        "Arkadaşlarımla iletişim için kullanırım.": 4,
        "Trendleri ve popüler kültürü takip ederim.": 5
    }},
    {"soru": "En büyük zaafın nedir?", "secenekler": {
        "Çok düşünmek.": 1,
        "Çok çalışmak.": 2,
        "Hassasiyet.": 3,
        "Aşırı duygusallık.": 4,
        "Hata yapma korkusu.": 5
    }},
    {"soru": "Bir yabancı dil öğrenme motivasyonun nedir?", "secenekler": {
        "Sadece gereklilik.": 1,
        "Beyin egzersizi için.": 2,
        "Kültür ve sanat öğrenmek için.": 3,
        "İnsanlarla bağ kurmak için.": 4,
        "İş fırsatları için.": 5
    }},
    {"soru": "Hangi film türünü seversin?", "secenekler": {
        "Belgesel.": 1,
        "Bilim kurgu.": 2,
        "Romantik.": 3,
        "Aksiyon.": 4,
        "Biyografi.": 5
    }},
    {"soru": "Bir topluluğa nasıl adapte olursun?", "secenekler": {
        "Gözlemleyerek.": 1,
        "Kuralları öğrenerek.": 2,
        "Uyum sağlayarak.": 3,
        "Kendimi olduğu gibi göstererek.": 4,
        "Dikkat çekerek.": 5
    }},
    {"soru": "Hata yaptığında tepkin ne olur?", "secenekler": {
        "Sessizce düzeltirim.": 1,
        "Analiz eder, nedenini bulurum.": 2,
        "Üzülürüm ama ders çıkarırım.": 3,
        "Dostlarıma anlatır, rahatlarım.": 4,
        "Çabuk geçer, bir sonraki işe odaklanırım.": 5
    }},
    {"soru": "Bir liderde en çok aradığın özellik nedir?", "secenekler": {
        "Dürüstlük.": 1,
        "Rasyonellik.": 2,
        "Karizma.": 3,
        "İnsan sevgisi.": 4,
        "Vizyon.": 5
    }},
    {"soru": "Kendini en iyi nerede hissedersin?", "secenekler": {
        "Doğanın içinde.": 1,
        "Planlanmış bir görev başında.": 2,
        "Şık bir davette.": 3,
        "Evde, ailemle.": 4,
        "Kalabalık bir etkinlikte.": 5
    }},
    # -------------------------------------------------------------------------
    # BÖLÜM 3: SOSYALLİK ve RİSK ALMA (41'den 60'a kadar)
    # -------------------------------------------------------------------------
    {"soru": "Bir kuralı ne zaman çiğnersin?", "secenekler": {
        "Asla çiğnemem.": 1,
        "Çok gerekli ve mantıklı bir neden varsa.": 2,
        "Kuralın estetiği bozduğunu düşünüyorsam.": 3,
        "Sevdiklerim için.": 4,
        "Kural, özgürlüğümü kısıtlıyorsa.": 5
    }},
    {"soru": "Bir grup çalışmasında en çok neye katkıda bulunursun?", "secenekler": {
        "Dengeyi sağlamaya.": 1,
        "Planı oluşturmaya.": 2,
        "Motivasyonu artırmaya.": 3,
        "Bağ kurmaya.": 4,
        "Yeni ve riskli fikirler sunmaya.": 5
    }},
    {"soru": "Boş zamanlarını nasıl değerlendirirsin?", "secenekler": {
        "Kendimi dinlerim.": 1,
        "Bir yeteneğimi geliştiririm.": 2,
        "Keyif aldığım şeyleri yaparım.": 3,
        "Yakın çevremle vakit geçiririm.": 4,
        "Dışarıda, aktif olurum.": 5
    }},
    {"soru": "Hangi slogan seni en iyi tanımlar?", "secenekler": {
        "Sessizlik, altındır.": 1,
        "Başarı, planlama ister.": 2,
        "Zarafet, her şeydir.": 3,
        "Aşkın ve dostluğun gücü.": 4,
        "Ya hep, ya hiç.": 5
    }},
    {"soru": "Bir problemi nasıl çözersin?", "secenekler": {
        "Basit tutarak.": 1,
        "Aşamaları belirleyerek.": 2,
        "Yaratıcı ve farklı bir yolla.": 3,
        "İnsanlarla işbirliği yaparak.": 4,
        "Hızlı ve kararlı bir saldırıyla.": 5
    }},
    {"soru": "Güne nasıl başlarsın?", "secenekler": {
        "Erken kalkar, sessizce güne başlarım.": 1,
        "Yapılacaklar listesiyle.": 2,
        "Güzel bir kahve ve estetik bir ortamla.": 3,
        "Müzikle ve enerjiyle.": 4,
        "Hemen spor yaparak.": 5
    }},
    {"soru": "Yemek yeme tarzın nedir?", "secenekler": {
        "Sade ve sağlıklı.": 1,
        "Geleneksel ve düzenli saatlerde.": 2,
        "Lezzet ve sunum önemlidir.": 3,
        "Aile ve arkadaşlarla uzun masalarda.": 4,
        "Hızlı ve dışarıda.": 5
    }},
    {"soru": "Bir ortamda dikkat çekmeyi sever misin?", "secenekler": {
        "Hayır, gözden uzak olmayı tercih ederim.": 1,
        "Eğer işimle ilgiliyse.": 2,
        "Evet, şıklığımın fark edilmesini isterim.": 3,
        "Dostlarımla eğleniyorsam.": 4,
        "Evet, liderlik yapmaktan hoşlanırım.": 5
    }},
    {"soru": "Çevren ne kadar önemlidir?", "secenekler": {
        "Sadece huzur veren bir ortam.": 1,
        "Temiz ve organize bir çevre.": 2,
        "Estetik ve ilham veren bir çevre.": 3,
        "Sıcak ve tanıdık insanlar.": 4,
        "Rekabetçi ve dinamik bir çevre.": 5
    }},
    {"soru": "Gelecek 5 yılını nasıl hayal ediyorsun?", "secenekler": {
        "Sakin ve huzurlu.": 1,
        "Başarılı ve planlı.": 2,
        "Aşk dolu ve tutkulu.": 3,
        "İnsanlara yardım ederek.": 4,
        "Büyük bir zirvede.": 5
    }},
    {"soru": "Bir iltifat aldığında tepkin ne olur?", "secenekler": {
        "Mahcup olurum.": 1,
        "Teşekkür ederim, hak ettiğimi bilirim.": 2,
        "Gülümserim.": 3,
        "Hemen iltifatla karşılık veririm.": 4,
        "Kendime olan güvenim artar.": 5
    }},
    {"soru": "Eleştiriye nasıl yaklaşırsın?", "secenekler": {
        "Huzurumu kaçırır.": 1,
        "Yapıcıysa kabul ederim.": 2,
        "Eleştirenin kim olduğuna bakarım.": 3,
        "Önce duygusal tepki veririm.": 4,
        "Kişisel gelişim fırsatı olarak görürüm.": 5
    }},
    {"soru": "Bir hobi seçmen gerekseydi, hangisini seçerdin?", "secenekler": {
        "Yazmak (içe dönük).": 1,
        "Satranç (mantıksal).": 2,
        "Resim/Müzik (estetik).": 3,
        "Takım sporu (sosyal).": 4,
        "Ekstrem sporlar (risk).": 5
    }},
    {"soru": "İnsanlara güvenmek senin için ne kadar kolay?", "secenekler": {
        "Çok zordur, az kişiye güvenirim.": 1,
        "Mantıklı kanıtlar varsa.": 2,
        "İçten ve samimi biriyse.": 3,
        "Ailem ve yakın çevrem için kolaydır.": 4,
        "Herkese bir şans veririm.": 5
    }},
    {"soru": "Hangi teknolojiyi daha çok kullanırsın?", "secenekler": {
        "Basit ve işlevsel olanı.": 1,
        "En son ve en verimli olanı.": 2,
        "Şık tasarımlı olanı.": 3,
        "Geniş kitlelerin kullandığı sosyal uygulamaları.": 4,
        "En yeni ve fütüristik olanı.": 5
    }},
    {"soru": "Hayatta en çok neye değer verirsin?", "secenekler": {
        "Denge ve sükûnet.": 1,
        "Doğruluk ve kesinlik.": 2,
        "Güzellik ve zevk.": 3,
        "Bağlılık ve sıcaklık.": 4,
        "Güç ve başarı.": 5
    }},
    {"soru": "Birinin seni ikna etme yolu nasıl olmalı?", "secenekler": {
        "Nazik ve yavaş.": 1,
        "Rakamlarla ve kanıtlarla.": 2,
        "Duygusallıkla.": 3,
        "İçten ve samimi bir konuşmayla.": 4,
        "Cesur ve iddialı bir sunumla.": 5
    }},
    {"soru": "Arkadaşlarını neye göre seçersin?", "secenekler": {
        "Sakin ve güvenilir olmasına.": 1,
        "Zeki ve çalışkan olmasına.": 2,
        "Zevkli ve sanattan anlamasına.": 3,
        "Duygusal bağ kurabileceğim kişilere.": 4,
        "Bana meydan okuyacak kişilere.": 5
    }},
    {"soru": "Bir şeyi ne kadar hızlı bitirirsin?", "secenekler": {
        "Acele etmem, zamanımı alırım.": 1,
        "Planladığım sürede.": 2,
        "İlham gelirse hızlı bitiririm.": 3,
        "Biraz ertelerim, sonra hızlanırım.": 4,
        "Hemen başlar, hemen bitiririm.": 5
    }},
    {"soru": "En büyük lüksün nedir?", "secenekler": {
        "Yeterince uyumak.": 1,
        "Yeni bir beceri öğrenmek.": 2,
        "İyi yemek yemek.": 3,
        "Geniş ailemle zaman geçirmek.": 4,
        "Zorlukların üstesinden gelmek.": 5
    }},
    # -------------------------------------------------------------------------
    # BÖLÜM 4: KÜLTÜR ve YAŞAM TARZI (61'den 80'e kadar)
    # -------------------------------------------------------------------------
    {"soru": "Tatile giderken bavulun nasıldır?", "secenekler": {
        "Sadece gerekli olanlar.": 1,
        "Her duruma uygun, planlı kıyafetler.": 2,
        "Şık parçalar ve aksesuarlar.": 3,
        "Rahat ve renkli kıyafetler.": 4,
        "Bir sürü lüks eşya.": 5
    }},
    {"soru": "Hangi aktivite seni daha çok yorar?", "secenekler": {
        "Büyük bir partide olmak.": 1,
        "Plansız bir geziye çıkmak.": 2,
        "Kaba veya estetikten yoksun bir ortamda bulunmak.": 3,
        "Evde tek başına kalmak.": 4,
        "Sınırları zorlamamak.": 5
    }},
    {"soru": "Topluluk önünde konuşmaktan çekinir misin?", "secenekler": {
        "Evet, çekinirim.": 1,
        "Hayır, ama hazırlıklı olmalıyım.": 2,
        "Hayır, sahne ışığını severim.": 3,
        "Sadece tanıdık bir kitle önünde rahattım.": 4,
        "Hayır, her zaman konuşurum.": 5
    }},
    {"soru": "Birine yardım ederken en çok neye önem verirsin?", "secenekler": {
        "Gizliliğe.": 1,
        "Doğru ve mantıklı çözüme.": 2,
        "Duygusal desteye.": 3,
        "Pratik çözümlere.": 4,
        "Hızlı ve etkili çözüme.": 5
    }},
    {"soru": "Bir yabancı ülkenin nesi seni en çok çeker?", "secenekler": {
        "Doğası ve sessizliği.": 1,
        "Gelişmişlik düzeyi.": 2,
        "Sanat ve tarihi.": 3,
        "İnsanlarının sıcaklığı.": 4,
        "Ekonomik fırsatları.": 5
    }},
    {"soru": "Bir iş arkadaşınla aran nasıl olmalı?", "secenekler": {
        "Profesyonel ve mesafeli.": 1,
        "Saygılı ve uyumlu.": 2,
        "Motivasyonu yüksek tutacak şekilde.": 3,
        "Arkadaşça ve destekleyici.": 4,
        "Rekabetçi ama saygılı.": 5
    }},
    {"soru": "Trafikte sıkıştığında ne yaparsın?", "secenekler": {
        "Sakin kalır, müzik dinlerim.": 1,
        "Alternatif yollar ararım.": 2,
        "Gergin hissederim, sabırsızlanırım.": 3,
        "Hemen bir arkadaşımı ararım.": 4,
        "Korname çalabilirim, tepkimi belli ederim.": 5
    }},
    {"soru": "Kitap okuma alışkanlığın nasıldır?", "secenekler": {
        "Yavaş okur, derin düşünürüm.": 1,
        "Planlı okurum.": 2,
        "Klasikleri ve sanatı okurum.": 3,
        "Çok okur, her türden okurum.": 4,
        "Popüler ve güncel kitapları okurum.": 5
    }},
    {"soru": "Birisi sana sürpriz yaptığında ne hissedersin?", "secenekler": {
        "Rahatsız.": 1,
        "Şaşkın.": 2,
        "Heyecanlı.": 3,
        "Mutlu.": 4,
        "Coşkulu.": 5
    }},
    {"soru": "Bir restoranda en çok neye dikkat edersin?", "secenekler": {
        "Sessiz olmasına.": 1,
        "Hijyenine ve düzenine.": 2,
        "Sunumuna ve ambiyansa.": 3,
        "Lezzetine ve bolluğuna.": 4,
        "Popülerliğine ve ününe.": 5
    }},
    {"soru": "Geçmiş mi, gelecek mi?", "secenekler": {
        "Geçmişin bilgeliği.": 1,
        "Planlanmış gelecek.": 2,
        "Anı yaşamak.": 3,
        "Geleceğe umutla bakmak.": 4,
        "Büyük gelecek hayalleri.": 5
    }},
    {"soru": "Hangi spor seni en çok temsil eder?", "secenekler": {
        "Yoga/Meditasyon.": 1,
        "Koşu/Yüzme (Bireysel).": 2,
        "Eskrim/Jimnastik (Estetik).": 3,
        "Futbol/Basketbol (Takım).": 4,
        "Boks/Formula 1 (Rekabetçi).": 5
    }},
    {"soru": "Bir yere söz verdiğinde ne kadar dakik olursun?", "secenekler": {
        "Erken giderim.": 1,
        "Tam vaktinde.": 2,
        "Biraz geç kalabilirim.": 3,
        "Esnek olmayı severim.": 4,
        "Çok geç kalabilirim.": 5
    }},
    {"soru": "Karamsarlığa kapıldığında nasıl davranırsın?", "secenekler": {
        "Daha çok yalnız kalırım.": 1,
        "Kendimi işe veririm.": 2,
        "Şık giyinir, moralimi düzeltirim.": 3,
        "Dostlarıma anlatır, rahatlarım.": 4,
        "Kendime güvenimi tazelerim.": 5
    }},
    {"soru": "Evde bir eşyanı kaybedersen ilk tepkin ne olur?", "secenekler": {
        "Aramaya üşenir, yenisini alırım.": 1,
        "Sistematik bir arama başlatırım.": 2,
        "Önemli değil, estetiği bozulmasın.": 3,
        "Tüm evi altüst edebilirim.": 4,
        "Sinirlenir, hemen bulmaya odaklanırım.": 5
    }},
    {"soru": "Dürüstlük senin için ne kadar önemli?", "secenekler": {
        "Çok önemli.": 1,
        "Her zaman.": 2,
        "Bazen duyguları incitmemek için esneyebilir.": 3,
        "Dostlarıma karşı her zaman.": 4,
        "Sadece iş hayatında.": 5
    }},
    {"soru": "Bir tatil planı ne kadar detaylı olmalı?", "secenekler": {
        "Hiç olmasın.": 1,
        "Her saat planlı olmalı.": 2,
        "Gezilecek yerler belli olsun.": 3,
        "Sadece konaklama ayarlandıysa yeter.": 4,
        "Gitmek yeter, gerisi spontane gelişir.": 5
    }},
    {"soru": "Mükemmeliyetçilik seviyen nedir?", "secenekler": {
        "Hiç mükemmeliyetçi değilim.": 1,
        "Yüksek seviyede.": 2,
        "Sadece görünüşle ilgili konularda.": 3,
        "Hedeflerime ulaşmak için.": 4,
        "Mükemmeliyetçilik benim ikinci adım.": 5
    }},
    {"soru": "Bir arkadaşın kötü bir fikirle gelirse ne yaparsın?", "secenekler": {
        "Sessiz kalırım.": 1,
        "Mantıklı nedenlerle itiraz ederim.": 2,
        "Nazikçe fikri değiştiririm.": 3,
        "Destek olur, sonra fikir bir şekilde değişir.": 4,
        "Açıkça ve tartışmacı bir şekilde karşı çıkarım.": 5
    }},
    {"soru": "Hayatın amacı nedir?", "secenekler": {
        "Huzur bulmak.": 1,
        "Başarılı olmak.": 2,
        "Aşkı bulmak.": 3,
        "Mutlu olmak.": 4,
        "Fark yaratmak.": 5
    }},
    # -------------------------------------------------------------------------
    # BÖLÜM 5: DUYGUSALLIK ve TUTKU (81'den 100'e kadar)
    # -------------------------------------------------------------------------
    {"soru": "Kültürel farklılıklara bakış açın nedir?", "secenekler": {
        "Saygı duyar, mesafeli dururum.": 1,
        "Farklılıkları analiz ederim.": 2,
        "Yeni bir sanat eseri gibi görürüm.": 3,
        "Öğrenmeye ve kucaklamaya açığım.": 4,
        "Kendimi kanıtlama fırsatı olarak görürüm.": 5
    }},
    {"soru": "Bir konserde nerede durursun?", "secenekler": {
        "Arkada, kenarda.": 1,
        "Ortada, rahat bir yerde.": 2,
        "En önde, sahneye yakın.": 3,
        "Grup arkadaşlarımla dans ederim.": 4,
        "Kalabalığın ortasında.": 5
    }},
    {"soru": "En çok hangi duyguyu gizlemeye çalışırsın?", "secenekler": {
        "Hırs.": 1,
        "Korku.": 2,
        "Neşe.": 3,
        "Üzüntü.": 4,
        "Öfke.": 5
    }},
    {"soru": "Hangi değeri en üstün tutarsın?", "secenekler": {
        "Tarafsızlık.": 1,
        "Dürüstlük.": 2,
        "Güzellik.": 3,
        "Bağlılık.": 4,
        "Özgüven.": 5
    }},
    {"soru": "Bir yemeği neye göre seçersin?", "secenekler": {
        "Sağlıklı olmasına.": 1,
        "Kaliteli olmasına.": 2,
        "Geleneksel olmasına.": 3,
        "Yeni ve egzotik olmasına.": 4,
        "Popüler olmasına.": 5
    }},
    {"soru": "Hayvanlara karşı tutumun nasıldır?", "secenekler": {
        "Saygı duyarım.": 1,
        "Doğanın parçasıdırlar.": 2,
        "Onların da duyguları vardır.": 3,
        "Onları çok severim.": 4,
        "Güçlü olanı severim.": 5
    }},
    {"soru": "Bir ortamda konuşma sırası sana gelince ne yaparsın?", "secenekler": {
        "Kısa ve öz konuşurum.": 1,
        "Hazırlıklı olduğum konularda konuşurum.": 2,
        "Duygusallığımı belli ederim.": 3,
        "Hikayeler anlatırım.": 4,
        "Liderliği hemen ele alırım.": 5
    }},
    {"soru": "Bir yere taşınsan nerede yaşardın?", "secenekler": {
        "Küçük ve sakin bir kasabada.": 1,
        "Büyük bir şehrin planlı bir bölgesinde.": 2,
        "Tarihi ve sanatsal bir şehirde.": 3,
        "Deniz kenarında, sıcak bir yerde.": 4,
        "Dünyanın en büyük metropolünde.": 5
    }},
    {"soru": "Ruh halin ne kadar hızlı değişir?", "secenekler": {
        "Çok yavaş.": 1,
        "Kontrollü.": 2,
        "Hızlı ve dramatik.": 3,
        "Hızlı ama geçicidir.": 4,
        "Çok hızlı ve yoğundur.": 5
    }},
    {"soru": "Hangi renk seni en iyi tanımlar?", "secenekler": {
        "Beyaz.": 1,
        "Lacivert.": 2,
        "Bordo/Kırmızı.": 3,
        "Turuncu/Sarı.": 4,
        "Siyah.": 5
    }},
    {"soru": "Bir şeyi değiştirmek için ne yaparsın?", "secenekler": {
        "Kendimi değiştiririm.": 1,
        "Mantıklı bir planla ilerlerim.": 2,
        "İnsanları duygusal olarak etkilerim.": 3,
        "Topluluğu harekete geçiririm.": 4,
        "Gücümü kullanırım.": 5
    }},
    {"soru": "Hangi duygu seni en çok yansıtır?", "secenekler": {
        "Sükûnet.": 1,
        "Disiplin.": 2,
        "Tutku.": 3,
        "Neşe.": 4,
        "Cesaret.": 5
    }},
    {"soru": "Bir projede ne zaman vazgeçersin?", "secenekler": {
        "Huzurumu bozduğunda.": 1,
        "Mantıklı bir gerekçe kalmadığında.": 2,
        "İlhamımı kaybettiğimde.": 3,
        "Ailem karşı çıktığında.": 4,
        "Asla vazgeçmem.": 5
    }},
    {"soru": "Yeni bir şey denerken nasılsın?", "secenekler": {
        "Çok temkinli.": 1,
        "Detaylı araştırırım.": 2,
        "Estetik görünmesine önem veririm.": 3,
        "Coşkulu ve hevesli.": 4,
        "Gözü kara denerim.": 5
    }},
    {"soru": "Hangi sanat dalı sana en yakındır?", "secenekler": {
        "Edebiyat.": 1,
        "Mimari.": 2,
        "Resim/Moda.": 3,
        "Müzik.": 4,
        "Sinema.": 5
    }},
    {"soru": "Bir fikri nasıl savunursun?", "secenekler": {
        "Sessiz ve mantıklı.": 1,
        "Verilerle ve kanıtlarla.": 2,
        "İnsanların duygularına hitap ederek.": 3,
        "Tüm enerjimle.": 4,
        "Tartışmayı kazanana kadar.": 5
    }},
    {"soru": "Başarıyı nasıl tanımlarsın?", "secenekler": {
        "İç huzuru bulmak.": 1,
        "Hedefe ulaşmak.": 2,
        "Sevdiğim işi yapmak.": 3,
        "Mutlu olmak.": 4,
        "Zirvede olmak.": 5
    }},
    {"soru": "Bir arkadaşın sırrını ne kadar saklarsın?", "secenekler": {
        "Ölene kadar.": 1,
        "Gerekirse.": 2,
        "Eğer çok önemliyse.": 3,
        "Dostluğun gereği olarak.": 4,
        "Güvenimi kırana kadar.": 5
    }},
    {"soru": "En büyük korkun nedir?", "secenekler": {
        "Kaos.": 1,
        "Başarısızlık.": 2,
        "Yalnızlık.": 3,
        "Güven kaybı.": 4,
        "Kısıtlanmak.": 5
    }},
    {"soru": "Bir işi ne zaman ertelersin?", "secenekler": {
        "Sıkıcı olduğunda.": 1,
        "Zaman çizelgemde yer olmadığında.": 2,
        "İlhamım gelmediğinde.": 3,
        "Daha önemli bir şey çıktığında.": 4,
        "Asla ertelemem.": 5
    }}
]

