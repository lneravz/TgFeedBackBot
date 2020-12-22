<div align="center">
    <a href="https://t.me/LneravzSupport">
        <img src="https://i.imgyukle.com/2020/12/22/aRoePf.jpg" width="300" height="300">
    </a>
    <p align="center">
        <h1>Lneravz FeedBack Bot v1.0.0</h1><br>
        <a href="https://t.me/LneravzSupport">Telegram Kanalı</a>
    </p>
</div>

## Kurulum

### Heroku ile

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/lneravz/TgFeedBackBot)


### Git ile

```bash
git clone https://github.com/lneravz/TgFeedBackBot
cd TgFeedBackBot
pip install -r requirements.txt
#config.json dosyasını düzenleyin
python3 main.py
```

## MongoDB

### Neden MongoDB

MongoDB kullanmamızdaki amaç çalıştırdığımız ortamı değiştirsek de kayıtlarımız silinmeyecektir. Ücretsiz süreli heroku hesabı kullananlar yeni bir hesaba geçtiğinde değişiklikleri silinmez.

### Nasıl ayarlanır?

<ol>
    <li>Öncelikler <a href="https://account.mongodb.com/account/register">buradan</a> kayıt oluşturun</li>
    <li>Company name kısmını rastgele doldurabilirsiniz</li>
    <li>Sonrasında gelen sayfada en altta 'Contine' butonunun yanında 'Skip' butonuna tıklayın</li>
    <li>Gelen sayfada ücretsiz olan 'Shared Clusters' bölümünden 'Create a Cluster' butonuna tıklayın</li>
    <li>'Create Cluster' butonuna basarak işleme devam edin</li>
    <li>'Your cluster is being created' yazısı gelecektir. Oluşturulana kadar bekleyin. 1-3 dakika sürebilir</li>
    <li>İşlem bittikten sonra Connect butonuna tıklayın</li>
    <li>'Add a Different IP Adress' butonuna tıklayarak IP Adress bölümüne '0.0.0.0' yazıp 'Add IP Adress' butonuna tıklayın</li>
    <li>Username ve Password belirledikten sonra 'Create Database User' butonuna tıklayın</li>
    <li>Sonrasında 'Choose a Connection Method' butonuna tıklayıp gelen menüde 'Connect your application' bölümüne girin</li>
    <li>Driver kısmından 'Python' ve version kısmından '3.6 or later' seçeneklerini seçtikten sonra 'copy' butonuna tıklayın</li>
    <li>MANGO_STRING yerine kopyaladığınız bu ifadeyi, MONGO_PASSWORD yerine 9. adımda belirlediğiniz şifreyi yazın</li>
</ol>
