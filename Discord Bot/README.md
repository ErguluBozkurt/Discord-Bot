## ADIM 1: Python'u Yükleyin
- Projeyi çalıştırmak için Python 3.8 veya üzeri bir sürüm gereklidir. Python'u resmi sitesinden indirebilirsiniz.**https://www.python.org/downloads/**
Python'ı kullanamk için çeşitli arayüzler mevcuttur. Örneğin:
- Visual Studio Code **https://code.visualstudio.com/**
- Jupyter Notebook **https://jupyter.org/**
- PyCharm **https://www.jetbrains.com/pycharm/**
- Google Colab **https://colab.research.google.com/**


## ADIM 2: Kütüphaneleri İndirin
- Aşağıdaki komutu kullanarak gerekli kütüphaneleri yükleyebilirsiniz:
    pip install -r requirements.txt
- Manuel olarak indirmek isterseniz aşağıdaki komutları python terminalinizde çalıştırın.
    pip install discord.py
    pip install databases
    pip install db-sqlite3
    pip install unittest (Genellikle yüklü olur)


## ADIM 3: Proje Dosyalarını İndirin
- Proje dosyalarını bilgisayarınıza indirin veya klonlayın:
    git clone **https://github.com/sizin-kullanici-adiniz/task_manager_bot.git**
    cd task_manager_bot


## ADIM 4: Bot Hesabı Oluşturma
- Discord hesabınızın olduğundan emin olun. **https://discord.com/**
- "Discord Developer Portal" adresine gidin. **https://discord.com/developers/applications**
- Discord hesabınızın bilgilerini girerek giriş yapın.
- "New Application" butonuna tıklayın ve uygulamanız için bir isim belirleyin.
- Sol taraftaki menüden "Bot" sekmesine geçin ve "Add Bot" butonuna tıklayın. Bu, uygulamanız için bir bot kullanıcısı oluşturacak.


## ADIM 5: Botu Sunucunuza Ekleyin
- Tekrar "Discord Developer Portal" adresinde botunuzun bulunduğu uygulamayı seçin.
- Sol menüden "OAuth2" sekmesine tıklayın.
- "OAuth2 URL Generator" bölümüne gidin.
- "Scopes" altında bot seçeneğini işaretleyin.
- "Bot Permissions" altında botun ihtiyaç duyduğu izinleri seçin (örneğin, "Mesajları Okuma", "Mesaj Gönderme" gibi).
- Oluşturulan URL'yi kopyalayın ve tarayıcınıza yapıştırın.
- Bu URL, botunuzu bir sunucuya eklemenizi sağlar. Botu eklemek istediğiniz sunucuyu seçin ve "Yetkilendir" butonuna tıklayın.


## ADIM 6: Discord Bot Token'ını Alma
- Discord Developer Portal'da botunuzun bulunduğu uygulamayı seçin.
- Sol taraftaki menüden "Bot" sekmesine tıklayın.
- "Token" bölümüne gelin ve Copy butonuna tıklayarak token'ınızı kopyalayın.


## ADIM 7: Token'ı Bot Koduna Ekleyin
- bot.py dosyasını açın.
- "YOUR_DISCORD_BOT_TOKEN" yerine kopyaladığınız token'ı yapıştırın. Örneğin:
    bot.run('NDk5ODQ2NzY0MzYwODUyMzI4.DqBz9g.7z8wv9x0y1z2a3b4c5d6e7f8g9h0i')


## ADIM 8: Botu Çalıştırma
- Botu başlatmak için terminalde aşağıdaki komutu çalıştırın:
    python bot.py
- Testleri çalıştırmak için:
    python run_tests.py


## KOMUTLAR
- - !add_task <description>: Açıklaması <description> olan bir görev ekler.
- - !delete_task <task_id>: <task_id> tanımlayıcısına sahip görevi siler.
- - !show_tasks: Tüm görevlerin bir listesini gösterir.
- - !complete_task <task_id>: <task_id> tanımlayıcısına sahip görevi tamamlandı olarak işaretler.