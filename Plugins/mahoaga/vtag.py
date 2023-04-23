import os, logging, asyncio
from Plugins import Maho
from telethon import events, Button
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep
from Plugins import modlar
from Config import *
import time, random 

# Silmeyiniz. 
anlik_calisan = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}
# ---------------------------- Komutlar ---------------------------
@Maho.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
  if not event.chat_id in anlik_calisan:
    return
  else:
    try:
      anlik_calisan.remove(event.chat_id)
    except:
      pass
    return await event.respond('**✅ Etiket işlemi başarıyla durduruldu.**')

# -------------------Tagger-------------------------------
@Maho.on(events.NewMessage(pattern="^/vtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan 
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**Bu komutu sadece grup veya kanallarda kullanabilirsiniz.**")
  
  admins = []
  async for admin in Maho.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadece yöneticiler kullanabilir. ✋**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Bana bir metin verin.**")
  else:
    return await event.respond("**Etikete Başlamak için sebep yazın.\n\n(Örnek:** `/tag Herkese Merhaba!`**)**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi başladı.**")
        
    async for usr in Maho.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"⌯ [{random.choice(soru)}](tg://user?id={usr.id})(tg://user?id={usr.id})\n"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await Maho.send_message(event.chat_id, f"**⌯ 📢 {msg}**\n\n{usrtxt}")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:
           a = await event.respond(f"**✅ Etiket işlemi başarıyla durduruldu.**\n\n**Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}")
           await sleep(10)
           await a.delete()

  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in Maho.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"⌯ [{random.choice(soru)}](tg://user?id={usr.id})tg://user?id={usr.id})\n"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await Maho.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:
           a = await event.respond(f"**✅ Etiket işlemi başarıyla durduruldu.**\n\n**Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}")
           await sleep(10)
           await a.delete()


# SORU ile etiketleme modülü

soru = ('Telefonunda en son aradığın şey neydi?',
'Birisi kız arkadaşın / erkek arkadaşından ayrılmak için sana 1 milyon tl önerseydi, yapar mıydın?',
'Bu grupda en az kimi seviyorsun ve neden?',
'Grupta gizli aşkın var mı ? ',
'Hiç sınıfta rezil oldun mu?',
'Yerden bir şeyi alıp hiç yedin mi?',
'Bu grupta kimsenin arkasından konuştun mu ?',
'Gruptaki sırdaşın kim ? ',
'Gruptaki en sevgiğin admin kim ? ',
'Grupta ki sevmedeğin kişiyi etiketler misin ? ',
'Grubu ne kadar seviyorsun ? ',
'Grubun olmazsa olmaz dediğin şeyi nedir ? ',
'Grup adminlerinden aşık olduğun oldumu ? ',
'Grupta ağzını burnunu kırarım dediğin kimse var mı ? ',
'Grubu seviyor musun ? ',
'Gruptan uzak kaç dakika durabilirsin ? ',
'Grubun en güzel kızı kim ? ',
'Grubun en yakışıklısı kim ? ',
'Grubun en cimrisi kim? ',
'Grupta kimle çay içmek isterdin ? ',
'Grupta hangi oyunu seviyorsun ? ',
'Kurt mu kelime oyunu mu ? ',
'Grubun en gıcığı kim ? ',
'Grubun en pisliği kim ? ',  
'Grubun en dertlisi kim ? ',
'Grubun ağır abisi kim ? ',
'Grubun en egoisti kim ? ',
'Grupta değişmesi gereken şey var mı? ',
'Grupta oynanan oyunları beğeniyor musun ? ',
'Sen admin olsan neyi değiştirirdin ? ',
'Grupta kimin yerinde olmak isterdin ? ',
'Grupta birinin yanında 3 gün kalma şansın olsa kim olurdu ? ',
'Grupta admin olsan kimi banlardın neden ? ',
'Grupta kimin yerinde olmak isterdin ? ',
'Gruptaki en gizemli kişi kim ? ',
'Gruptaki kimin yanına görünmez olarak gitmek istersin ? ',
'Grupta keşke abim/ablam olsaydı dediğin kimse var mı ? ',
'Gizliden gizliden sadece onun için geldiğin kimse var mı grupta ? ',
'Real hayatta tanımak istediğin kimse var mı grupta ? ',
'Grupta bulunan en uyuz kişi kim ? ',
'Real görüştüğün biri var mı grupta ? ',
'Akrabalarından kimseyi davet ettin mi gruba ? ',
'Ailenden biri seni bu grupta görse ne olur ? ',
'Hayatınla ilgili telegramda ne yalan söyledin ? ',
'Grubu gerçekten seviyor musun? ',
'Grupta samimi olduğun kim var etiketlermisin ? ',
'Sevmeyipte seviyormuş gibi davrandığın kimse var mı? ',
'Bir gün karşı cins olarak uyanırsan, ilk yapacağın şey nedir?',
'Büyüyen hayali bir arkadaşınız var mıydı?',
'En kötü alışkanlığınız nedir?',
'Grubun delisi kim etiketler misin?',
'Toplumda en utanç verici anınız neydi?',
'Aynada kendinle hiç konuştun mu?',
'Web geçmişinizi, birileri görürse utanacağınız şey ne olurdu?',
'Uykunda konuşur musun?',
'Gizli aşkın kim?',
'Bu grupta kimle çıkardın?',
'Grubun kralı kim?',
'Son attığın mesaj neydi?',
'İnsanları yanan bir binadan kurtarıyor olsaydınız ve bir kişiyi bu grupdan geride bırakmak zorunda kalırsanız, kim olurdu?',
'Bu gruptaki kim bugüne kadarki en kötü insan olurdu? Neden?',
'Yeniden doğmuş olsaydın, hangi yüz yılda doğmak isterdin?',
'Söylediğiniz veya yaptığınız bir şeyi silmek için zamanda geriye gidebilseydiniz, bu hangi yıl olurdu?',
'Erkek arkadaşın veya kız arkadaşın seni hiç utandırdı mı?',
'Birdenbire görünmez olsaydın ne yapardın?',
'Grupta sevdiğin üç arkadaşını etiketle',
'Şimdiye kadar gördüğüm en garip rüyayı anlat.',
'Hala yaptığın en çocukça şey nedir?',
'Hangi çocuk filmini tekrar tekrar izleyebilirsin?',
'Grupta ki en değerli kişi senin için kim?',
'Saçma takma adların var mı?',
'Telefonunuzda hangi uygulamada en çok zaman harcıyorsunuz?',
'Tek bir oturuşta yediğin en çok yemek ne?',
'Tek başınayken dans ediyor musun?',
'Karanlıktan korkar mısın?',
'Bütün gün evdeysen ne yapardın?',
'Günde kaç öz çekim yapıyorsunuz?',
'En son ne zaman dişlerini fırçaladın?',
'En sevdiğin pijamalar neye benziyor?',
'Hiç yerden bir şey yedin mi?',
'Yapmaman gereken bir şeyi yaparken hiç yakalandın mı?',
'Vücudunun hangi bölümünü seviyorsun, hangi kısmından nefret ediyorsun?',
'Grupta ki kankalarını etiketler misin ?',
'Pantolonunu hiç kestin mi?',
'Kurt oyununu seviyor musun?',
'Kimsenin senin hakkında bilmediği bir şey nedir?',
'Burda ki kimseye yalan söyledin mi?',
'Dirseğini yalayabilir misin?',
'Eğer buradaki herkesi yanan bir binadan kurtarmaya çalışıyor olsaydın ve birini geride bırakmak zorunda kalırsan, kimi geride bırakırdın?',
'Telefonda aradığın son şey neydi?',
'Bir uygulamayı telefonunuzdan silmek zorunda kalsanız hangisini silerdiniz?',
'Bir ilişkideki en büyük korkun nedir?',
'Gruptaki her bir kişi hakkında bir tane olumlu, bir tane olumsuz şey söyleyin.',
'Sevmediğin kötü huyun var mı?',
'Hayatında yaptığın en çılgın şey nedir?',
'Üç gün boyunca bir adada mahsur kalmış olsaydınız, bu grupdan kimleri seçerdiniz?',
'Bu odadaki en sinir bozucu kişi kim?',
'Bu grupdan biriyle evlenmek zorunda kalsan kim olurdu?',
'En uzun ilişkiniz ne kadar sürdü?',
'Bir ünlü Instagram’da seni takip etseydi bu ünlünün kim olmasını isterdin?',
'Instagram’da 5 kişiyi silmek zorunda olsan kimleri silerdin?',
'Kaç çocuk sahibi olmak istersin?',
'Hayallerinizdeki kişiyi tarif edin.',
'Messi mi Ronaldo mu?',
'Pes mi Fifa mı?',
'İlk işin neydi?',
'Üniversite hakkındaki en büyük korkun nedir?',
'En iyi arkadaşının seninle aynı üniversiteye gitmesini ister misin?',
'Mevcut erkek arkadaşının ya da kız arkadaşının seninle aynı üniversiteye gitmesini ister misin?',
'Hayalindeki iş ne?',
'Hiç bir dersten başarısız oldun mu?',
'Hiç kopya çektin mi?',
'Hiç sınıfta uyudun mu?',
'Sınıfta asla yanında oturmak istemeyeceğin kim?',
'Derse hiç geç kaldın mı?',
'Bir öğretmenin önünde yaptığın en utanç verici şey nedir?',
'Hiç masanın altına sakız attın mı?',
'Hiç okulda kavga ettin mi?',
'Bir sınavdan aldığın en kötü puan neydi?',
'Sınıfta hiç uyuya kaldın mı?',
'Hiç gözaltına alındın mı?',
'Eğer görünmez olsaydın hangi derse gizlice girerdin?',
'En kötü grup hangisidir?',
'Bu grupdaki sır tutma  konusunda en çok zorlanan kişi kimdir?',
'Söylediğin en son yalan neydi?',
'Spor yapar mısın?',
'Hayatının geri kalanında sadece bir kıyafet giyebilseydin, bu kıyafetin hangi renk olurdu?',
'Sizce Türkiye’nin eğitim sisteminde yapılması gereken en önemli değişiklik nedir?',
'Karanlıktan/yükseklikten korkar mısın?',
'Kendi görünuşünü 1 ile 10 arasında puanla :)',
'Yaptıgın en yasadışı şey neydi?',
'Şimdi sana bir evlenme teklifi gelse ve sevmediğin biri olsa, ve bu sana son gelecek evlilik teklifi olsa kabul edermiydin?',
'Şu anki ruh haline bakarak ne tür film izlersin (aksiyon/dram/bilim kurgu/romantik komedi/biyografi/fantastik)',
'Kendini en ezik hissettiğin an hangisiydi ?',
'ilerde çocuğun olursa ne isim koymak istersin?',
'Unicorun mu olmasını isterdin ejderhan mı?',
'Kaç sevgilin oldu?',
'Hayatta unutmadığın biri var mı?',
'en sevdiğin şarkı?',
'Yapmaman gereken bir şeyi yaparken hiç yakalandın mı?',
'En sevdiğin sanatçı kim?',
'karşı cinste ilk dikkatini çeken ne?',
'bu yıl hayatında neyi değişmeyi uygun görüyorsun?',
'Birinin telefonunda gördüğün en tuhaf şey nedir?',
'Süper kahramanlar gerçekten var olsaydı Dünya nasıl bir yer olurdu?',
'Hayatın size öğrettiği en önemli ders nedir?',
'Kültürümüzün en çok sevdiğiniz yanı nedir?',
'Ailenizin uyguladığı en tuhaf gelenek nedir?',
'Aileniz dışında, yaşamınız üzerinde en büyük etkisi olan kişi kimdir?',
'Kadın/Erkek olmanın en kötü ve en iyi yanı nedir?',
'Beynini bir robota yerleştirebilir ve sonsuza kadar bu şekilde yaşayabilsedin,bunu yapar mıydın?',
'Evinizde ağırladığın en kötü misafir kimdi ve ne oldu?',
'İnsanların size ne sormasından bıktınız?',
'En tuhaf korkunuz nedir?',
'En sevdiğiniz TV programı hangisidir?',
'Girdiğiniz en saçma tartışma nedir?',
'En son söylediğin yalan nedir?',
'Biriyle çıkarken yaptığın en utanç verici şey neydi?',
'Hiç arabanla (varsa) yanlışlıkla bir şeye birine çarptın mı?',
'Hoşuna gittiğini düşündüğün ama bir türlü açılamadığın biri oldu mu?',
'En tuhaf takma adın nedir?',
'Fiziksel olarak sana en acı veren deneyimin ne oldu?',
'Hangi köprüleri yakmak seni rahatlattı?',
'Toplu taşıma araçlarında yaptığın en çılgınca şey neydi?',
'Şişeden bir cin çıksa üç dileğin ne olurdu?',
'Dünyadaki herhangi birini Türkiye’nin başkanı yapabilseydin bu kim olurdu?',
'Şimdiye kadar bir başkasına söylediğin en acımasızca şey neydi?',
'Birini öperken kendini hiç kötü hissettin mi?',
'Hiçbir sonucu olmayacağını bilsen ne yapmak isterdin?',
'Bir aynanın önünde yaptığın en çılgınca şey nedir?',
'Şimdiye kadar başkasına söylediğin en anlamlı şey neydi?',
'Arkadaşlarınla yapmayı sevdiğin ama sevgilinin önünde asla yapmayacağın şey nedir?',
'Bu hayatta en çok kimi kıskanıyorsun?',
'Grupta neyi değiştirmek isterdin?',
'Bir buluşmadan kaçmak için hiç hasta numarası yaptın mı?',
'Çıktığın en yaşlı kişi kim?',
'Günde kaç tane özçekim yaparsın?',
'Aşk için her şeyi yaparım ama “bunu” yapmam dediğin şey nedir?',
'Haftada kaç kez aynı pantolonu giyiyorsun?',
'Bugün şansın olsa lise aşkınla çıkar mısın?',
'Vücudunun hangi bölümlerinden gıdıklanıyorsun?',
'Çeşitli batıl inançların var mı? Varsa onlar neler?',
'Sevdiğini itiraf etmekten utandığın film hangisidir?',
'En utan verici kişisel bakım alışkanlığın nedir?',
'En son ne zaman ve ne için özür diledin?',
'Sözlü destanlar hakkında ne düşünüyorsun?',
'Grupta ki üç kankanı etiketler misin?',
'Hiç sevgilini aldatmayı düşündün mü?',
'Hiç sevgilini biriyle aldattın mı?',
'Grupta kimin hesabına girmek istersin?',
'Hiç kimseyi özelden rahatsız ettin mi?',
'Saçlarını uzatmayı düşünsen ne kadar uzatırdın?',
'Kimsenin bilmeyeceği garanti olsa kimi öldürmek isterdin?',
'Başkası için aldığın en ucuz hediye nedir?',
'Zamanının çoğunu en çok hangi uygulamada harcıyorsun?',
'Otobüste yaptığın en tuhaf şey nedir?',
'Grupta nefret ettiğin biri var mı?',
'Günde ne kadar dedikodu yaparsın?',
'Çıkmak isteyeceğin en genç kişi kaç yaşında olurdu?',
'kendinde beğendiğin en iyi özellerin nelerdir?',
'Hiç yaşın hakkında yalan söyledin mi?',
'Telefonundan bir uygulamayı silmek zorunda olsan bu hangisi olurdu?',
'Gece geç saatte yaptığın en utanç verici şey nedir?',
'Grup senin için ne ifade ediyor?',
'Hiç sahte kimlik kullandın mı?',
'Kırmızı halıda beraber yürümek istediğin ünlü isim kim?',
'Grubun neşesi kim?',
'Bir cin sana üç dilek hakkı sunsaydı neler dilerdin? ',
'Bir gün karşı cins olarak uyansan yapacağın ilk iş ne olurdu? ',
'Bu gruptaki insanlardan kiminle hayatını değiştirmek isterdin? ',
'Büyürken hiç hayali arkadaşın oldu mu',
'Telefonunuzda aradığın son şey neydi? ',
'Issız bir adaya düşsen yanına alacağın beş şey ne olurdu? ',
'Tam anlamıyla en son ne zaman yalan söyledin',
'Bu hayatta seni en çok kızdıran şey nedir',
'Bu hayatta sahip olduğun en büyük pişmanlık nedir',
'Gördüğün en garip rüya neydi? ',
'Grupta hoşlandığın biri var mı ? ',
'Senin hakkındaki en büyük yanılgı nedir? ',
'Grubun olmazsa olmazı sence kim etiketler misin? ',
'İnsanların senin hakkında bilmesini istediğin şey nedir? ',
'Kötü bir ilişkiden kaçmak için hiç yalan söyledin mi? ',
'İçinde bulunduğun en büyük sorun neydi? ',
'Grupta olmamasını istediğin kişiyi etiketler misin? ',
'Hakkında yalan söylediğin en kötü şey nedir? ',
'Keşke onun hakkında yalan söyleseydim dediğin şey nedir? ',
'Sana bugüne kadar verilen en iyi tavsiye nedir? ',
'Grupta kimden gıcık alıyorsun? ',
'Kilo aldırıp aldırmaması önemli değil, bir oturuşta hepsini yerim dediğin yemek nedir? ',
'Grupta gizli sevdiğin kimse var mı? ',
'Bir böcek istilası gerçekleşse hangi arkadaşın hayatta kalmayı başarır? ',
'Bir arkadaşınla plan yaparken bir başka arkadaşını ektiğin oldu mu? ',
'Şimdiye kadar hiç aralıksız 12 saatten fazla uyuduğun oldu mu? ',
'Hatırladığın kadarıyla ilk aşık olduğun ünlü kimdi? ',
'Hiç yasaya aykırı bir şeyler yaptığın oldu mu? ',
'Grupta en sevdiğin arkadaşını etiketler misin? ',
'Bu hayattaki en büyük güvensizliğin nedir? ',
'Hiç sırf fayda sağladığı için biriyle arkadaş kaldığın oldu mu? ',
'Bu hayatta şimdiye kadar yaptığın en büyük hata nedir? ',
'Bu hayatta şimdiye kadar yaptığın en iğrenç şey nedir? ',
'Oyunu oynayan oyuncu grubunda yer alanlardan kimi öpmek istersin? ',
'En son ne zaman hüngür hüngür ağladığını hatırlıyor musun? ',
'Ailenin senin hakkında bilmediğine sevindiğin şey nedir? ',
'Bu hayatta seni seni en çok ne gıcık eden ve çileden çıkaran şey nedir? ',
'Bir odada uzun bir süre hapsolacağını düşünsen yanında olmasını istediğin üç şey ne olurdu? ',
'Bu hayatta hiç kimseye söylemediğin bir sırrın var mı? ',
'İnsanların senin hakkında bildiği ama en nefret ettiğin şey nedir? ',
'Alışverişin dibine vururken en çok harcama yaptığın gün hangisiydi? ',
'Onsuz bu hayat çekilmezdi dediğin favori bir arkadaşın var mı etiketler misin? ',
)

