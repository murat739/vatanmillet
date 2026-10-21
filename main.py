import streamlit as st
import pandas as pd
import random

# ==========================================
# 1. SAYFA YAPILANDIRMASI
# ==========================================
st.set_page_config(
    page_title="Vatan, Bayrak & Mukaddesat Portalı",
    page_icon="🇹🇷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. DİL DESTEĞİ VE SÖZLÜK (TRANSLATIONS)
# ==========================================
if 'lang' not in st.session_state:
    st.session_state.lang = 'Türkçe'

# Yan menüde dil seçimi
lang = st.sidebar.radio(
    "🌐 Dil Seçimi / Select Language:", 
    ["Türkçe", "English"],
    index=0 if st.session_state.lang == "Türkçe" else 1
)
st.session_state.lang = lang

# Arayüz Etiketleri Sözlüğü
UI_TEXT = {
    "Türkçe": {
        "title": "🇹🇷 VATAN, BAYRAK VE BİRLİK PORTALI 🇹🇷",
        "subtitle": "Osmanlı'dan Günümüze Vatan, İman, Bayrak ve Birlik Şuurunun Abideleri",
        "panel_title": "⚙️ Kontrol Paneli",
        "cat_select": "📌 Kategori Seçin:",
        "search_label": "🔍 Kelime, Padişah veya Kaynak Ara:",
        "search_placeholder": "Örn: Kosova, Fatih, Nöbet, Edebali, Yunus...",
        "random_btn": "🎲 Günün Hikmetini Getir",
        "all_cats": "Tüm Konular",
        "total_records": "Kayıtlı Eser & Söz",
        "listed_records": "Listelenen İçerik",
        "themes": "Milli Temalar",
        "source_lbl": "📜 Kaynak & Belge:",
        "hikmet_lbl": "💡 Milli & Manevi Hikmet:",
        "no_result": "Aradığınız kritere uygun kayıt bulunamadı.",
        "marquee_title": "🇹🇷 MİLLİ VE MANEVİ DEĞERLERİMİZ 🇹🇷",
        "expander_title": "🇹🇷 Vatan, Bayrak ve Birlik Şuurunun Temel Esasları",
        "legal_title": "⚖️ Yasal Uyarı ve Kullanım Şartları",
        "marquee_quotes": [
            "🇹🇷 Bayrakları bayrak yapan üstündeki kandır; Toprak, eğer uğrunda ölen varsa vatandır!",
            "🇹🇷 Girmeden tefrika bir millete, düşman giremez; Toplu vurdukça yürekler, onu top sindiremez!",
            "🇹🇷 Bizim niyetimiz sırf Allah rızasıdır. Elimdeki kılıç yalnız din ve vatan yolundadır! (Fatih Sultan Mehmed)",
            "🇹🇷 İnsanı yaşat ki devlet yaşasın! (Şeyh Edebali)",
            "🇹🇷 Birlikte rahmet, ayrılıkta azap vardır. (Hadis-i Şerif)",
            "🇹🇷 Bölüşürsek tok oluruz, bölünürsek yok oluruz! (Yunus Emre)",
            "🇹🇷 Bir olalım, iri olalım, diri olalım! (Hacı Bektaş-ı Velî)"
        ],
        "legal_body": """
        **Yasal Bilgilendirme ve Kullanım Şartları:**
        1. **Amacımız:** Bu portal yalnızca milli, manevi ve tarihi bilinci artırmak; bilgilendirme yapmak amacıyla hazırlanmıştır.
        2. **Ticari Kullanım Yasağı:** Portalda yer alan hiçbir içerik, görsel veya kod yapısı ticari amaçlarla kullanılamaz, satılamaz ve çoğaltılamaz.
        3. **Fikri Mülkiyet ve Kopyalama:** Sayfadaki içeriklerin izinsiz kopyalanması, kazınması (scraping) engellenmiştir.
        4. **Sorumluluk Sınırı:** Portalda sunulan tarihi ve manevi bilgiler açık kaynaklı tarihi vesikalara dayanır. Yazılımcı/Geliştirici doğrudan veya dolaylı olarak doğabilecek hukuki uyuşmazlıklardan sorumlu tutulamaz.
        """,
        "expander_body": """
        * **1. Allah'a Teslimiyet ve Sefer Şuru:** Osmanlı Padişahları ve gönül erleri sefere ve hizmete giderken canlarını Allah'a emanet etmişlerdir.
        * **2. Bayrağın Kutsallığı:** Ayyıldızlı bayrağımız, bağımsızlığımızın ve şehitlerimizin mukaddes emanetidir.
        * **3. Birlik ve Beraberlik:** Tefrikayı reddedip kardeşlik hukukuna sımsıkı sarılmak devletin ve milletin bekasının şartıdır.
        * **4. Ahlak ve Adalet:** Adaletin ve güzel ahlakın olmadığı yerde toplumsal huzur tesis edilemez.
        """
    },
    "English": {
        "title": "🇹🇷 HOMELAND, FLAG & UNITY PORTAL 🇹🇷",
        "subtitle": "Monuments of Homeland, Faith, Flag, and Unity Consciousness from the Ottoman Era to Present",
        "panel_title": "⚙️ Control Panel",
        "cat_select": "📌 Select Category:",
        "search_label": "🔍 Search Word, Sultan or Source:",
        "search_placeholder": "e.g., Kosovo, Fatih, Guard, Edebali, Unity...",
        "random_btn": "🎲 Get Wisdom of the Day",
        "all_cats": "All Categories",
        "total_records": "Total Records",
        "listed_records": "Listed Content",
        "themes": "National Themes",
        "source_lbl": "📜 Source & Document:",
        "hikmet_lbl": "💡 Spiritual & National Wisdom:",
        "no_result": "No records found matching your search criteria.",
        "marquee_title": "🇹🇷 OUR NATIONAL & SPIRITUAL VALUES 🇹🇷",
        "expander_title": "🇹🇷 Principles of Homeland, Flag, and Unity Consciousness",
        "legal_title": "⚖️ Legal Disclaimer & Terms of Use",
        "marquee_quotes": [
            "🇹🇷 What makes flags a true flag is the blood upon it; Soil becomes a homeland if there are those who die for it!",
            "🇹🇷 No enemy can penetrate a nation unless division enters; When hearts beat as one, no cannon can defeat them!",
            "🇹🇷 Our intention is purely for the sake of God. The sword in my hand is only for faith and homeland! (Sultan Mehmed II)",
            "🇹🇷 Preserve the people so that the state may live! (Sheikh Edebali)",
            "🇹🇷 There is mercy in unity, and torment in division. (Hadith)",
            "🇹🇷 If we share we satisfy, if we divide we perish! (Yunus Emre)",
            "🇹🇷 Let us be one, let us be strong, let us be alive! (Haji Bektash Veli)"
        ],
        "legal_body": """
        **Legal Notice & Terms of Use:**
        1. **Purpose:** This portal is strictly designed for educational, informational, and cultural awareness purposes.
        2. **Non-Commercial Use:** No content, text, or script within this portal may be used, resold, or reproduced for commercial gain.
        3. **Intellectual Property:** Unlawful copying or scraping of website data is prohibited and technically restricted.
        4. **Limitation of Liability:** Historical and spiritual entries are based on traditional open-source records. The developer assumes no legal liability for external misinterpretations.
        """,
        "expander_body": """
        * **1. Devotion to God & Campaign Spirit:** Ottoman Sultans and spiritual masters entrusted their lives to God during campaigns and services.
        * **2. Sanctity of the Flag:** Our crescent and star flag is the sacred legacy of our martyrs and independence.
        * **3. Unity & Solidarity:** Rejecting division and embracing brotherhood is essential for the survival of the state and nation.
        * **4. Morality & Justice:** Social peace cannot be established without justice and high moral principles.
        """
    }
}[lang]

# ==========================================
# 3. ÖZEL CSS VE GÜVENLİK (KOPYALAMA ENGELLEME)
# ==========================================
st.markdown("""
<style>
    /* Metin Seçimini Engelleme (CSS Protection) */
    * {
        -webkit-user-select: none !important;
        -moz-user-select: none !important;
        -ms-user-select: none !important;
        user-select: none !important;
    }

    .main {
        background-color: #F8FAFC;
    }
    
    .half-screen-marquee {
        width: 100%;
        min-height: 180px;
        background: linear-gradient(135deg, #B91C1C 0%, #7F1D1D 50%, #450A0A 100%);
        color: #FFFFFF;
        border-radius: 20px;
        box-shadow: 0 12px 30px rgba(185, 28, 28, 0.4);
        border: 4px solid #FCA5A5;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        position: relative;
        margin-bottom: 30px;
        padding: 20px;
    }

    .marquee-header-title {
        font-size: 22px;
        font-weight: 900;
        letter-spacing: 2px;
        color: #FEF08A;
        text-transform: uppercase;
        margin-bottom: 15px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.6);
        text-align: center;
    }

    .marquee-content-box {
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
        box-sizing: border-box;
    }

    .marquee-text {
        display: inline-block;
        padding-left: 100%;
        animation: marquee 34s linear infinite;
        font-size: 28px;
        font-weight: 800;
        color: #FFFFFF;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.8);
        line-height: 1.4;
    }

    .marquee-text span {
        color: #FCA5A5;
        margin: 0 25px;
    }

    @keyframes marquee {
        0%   { transform: translate(0, 0); }
        100% { transform: translate(-100%, 0); }
    }

    .stCard {
        background-color: #FFFFFF;
        border-radius: 18px;
        padding: 26px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        border-left: 6px solid #DC2626;
        border-top: 1px solid #E2E8F0;
        border-right: 1px solid #E2E8F0;
        border-bottom: 1px solid #E2E8F0;
        margin-bottom: 22px;
    }
    .badge-tag {
        background-color: #FEF2F2;
        color: #991B1B;
        font-size: 13px;
        font-weight: bold;
        padding: 6px 16px;
        border-radius: 30px;
        border: 1px solid #FCA5A5;
        display: inline-block;
        margin-bottom: 12px;
    }
    .card-title {
        color: #0F172A;
        font-size: 22px;
        font-weight: 800;
        margin-bottom: 8px;
    }
    .source-box {
        background-color: #F1F5F9;
        color: #334155;
        padding: 8px 16px;
        border-radius: 8px;
        font-size: 14px;
        font-weight: 700;
        margin-bottom: 16px;
        display: inline-block;
        border-left: 3px solid #64748B;
    }
    .quote-text {
        color: #1E293B;
        font-size: 18px;
        line-height: 1.8;
        background-color: #F8FAFC;
        padding: 20px;
        border-radius: 12px;
        font-style: italic;
        margin-bottom: 16px;
        border: 1px dashed #CBD5E1;
        white-space: pre-line;
    }
    .message-box {
        background-color: #FEF3C7;
        color: #78350F;
        padding: 14px 18px;
        border-radius: 12px;
        font-size: 15px;
        font-weight: 600;
        line-height: 1.6;
    }
</style>

<!-- Sağ Tık ve Kopyalama Engelleme Scripti -->
<script>
    document.addEventListener('contextmenu', event => event.preventDefault());
    document.addEventListener('keydown', function(event) {
        if (event.ctrlKey && (event.key === 'c' || event.key === 'u' || event.key === 's' || event.key === 'a')) {
            event.preventDefault();
        }
    });
</script>
""", unsafe_allow_html=True)

# ==========================================
# 4. ÇOK DİLLİ VERİ SETİ (GÜÇLENDİRİLMİŞ VELİ KULLAR İÇERİĞİ)
# ==========================================
@st.cache_data
def load_bilingual_data():
    records = [
        # --- OSMANLI PADİŞAHLARI ---
        {
            "Kategori_TR": "Osmanlı Padişahları & Devlet Adamları",
            "Kategori_EN": "Ottoman Sultans & Statesmen",
            "Konu_TR": "Sultan 1. Murad Han'ın Kosova Meydan Muharebesi Duası",
            "Konu_EN": "Sultan Murad I's Prayer Before the Battle of Kosovo",
            "Kaynak_TR": "Neşrî Tarihi / Kosova Meydan Savaşı (1389)",
            "Kaynak_EN": "Neshri History / Battle of Kosovo (1389)",
            "Metin_TR": "Ya Rab! Bu fırtına ve toz bulutunu kaldır, Müslüman askerini düşman elinde helak etme! Ya İlahi! Bunca canı benim yüzümden helak etme! Onları muzaffer eyle, beni ise şehit eyle! Yeter ki bu din ve bayrak sağ kalsın!",
            "Metin_EN": "O Lord! Lift this storm and dust cloud, do not let the Muslim army perish at the hands of the enemy! O God! Do not destroy so many lives because of me! Grant them victory and grant me martyrdom! As long as this faith and flag endure!",
            "Hikmet_TR": "Sultan Murad Han sefere giderken canını vatanına feda etmiş ve o gece şehitlik mertebesine erişmiştir.",
            "Hikmet_EN": "Sultan Murad I sacrificed his life for his homeland on his campaign and attained martyrdom that night."
        },
        {
            "Kategori_TR": "Osmanlı Padişahları & Devlet Adamları",
            "Kategori_EN": "Ottoman Sultans & Statesmen",
            "Konu_TR": "Fatih Sultan Mehmed Han'ın Fetih Anındaki Yakarışı",
            "Konu_EN": "Sultan Mehmed the Conqueror's Prayer During Conquest",
            "Kaynak_TR": "Tursun Bey / Târih-i Abu'l-Feth",
            "Kaynak_EN": "Tursun Bey / History of the Conqueror",
            "Metin_TR": "Bizim niyetimiz sırf Allah rızasıdır. Elimdeki kılıç yalnız din ve vatan yolundadır. Eğer dünya mülkü için savaşırsak Allah bize zafer nasip etmesin!",
            "Metin_EN": "Our intention is purely for the sake of God. The sword in my hand is only for faith and homeland. If we fight for worldly possessions, may God not grant us victory!",
            "Hikmet_TR": "İstanbul'un fethi sadece askeri bir zafer değil; samimiyet, ilim ve imanla elde edilmiş kutlu bir muvaffakiyettir.",
            "Hikmet_EN": "The conquest of Istanbul was not merely a military victory, but a blessed achievement born of sincerity, knowledge, and faith."
        },
        {
            "Kategori_TR": "Osmanlı Padişahları & Devlet Adamları",
            "Kategori_EN": "Ottoman Sultans & Statesmen",
            "Konu_TR": "Sultan 2. Abdülhamid Han'ın Vatan Toprağı Hassasiyeti",
            "Konu_EN": "Sultan Abdulhamid II's Devotion to Homeland Soil",
            "Kaynak_TR": "Sultan Abdülhamid Han'ın Siyasi Hatıratı",
            "Kaynak_EN": "Political Memoirs of Sultan Abdulhamid II",
            "Metin_TR": "Ben bir karış bile toprak satmam. Zira bu topraklar bana ait değil, milletime aittir. Milletim bu vatanı kanlarıyla sulayarak kazanmıştır. Kanla alınan kanla verilir!",
            "Metin_EN": "I will not sell even an inch of land. For this land does not belong to me, but to my nation. My nation gained this homeland with their blood. What is taken with blood can only be given with blood!",
            "Hikmet_TR": "Vatan toprağı pazarlık konusu yapılamaz; o şehitlerimizin paha biçilemez emanetidir.",
            "Hikmet_EN": "Homeland soil cannot be bargained over; it is the priceless legacy of our martyrs."
        },

        # --- AYET-İ KERİMELER ---
        {
            "Kategori_TR": "Ayet-i Kerimeler",
            "Kategori_EN": "Quranic Verses",
            "Konu_TR": "Birlik ve Beraberlik Emri",
            "Konu_EN": "Command of Unity and Togetherness",
            "Kaynak_TR": "Kur'an-ı Kerim, Âl-i İmrân Suresi 103. Ayet",
            "Kaynak_EN": "Holy Quran, Surah Ali 'Imran, Verse 103",
            "Metin_TR": "Hep birlikte Allah'ın ipine sımsıkı sarılın, parçalanıp bölünmeyin! Allah'ın üzerinizdeki nimetini hatırlayın...",
            "Metin_EN": "And hold firmly to the rope of Allah all together and do not become divided. And remember the favor of Allah upon you...",
            "Hikmet_TR": "Milletimizi ayakta tutan çimento, ortak değerler etrafında kenetlenmektir.",
            "Hikmet_EN": "The bond that sustains our nation is uniting around shared values."
        },
        {
            "Kategori_TR": "Ayet-i Kerimeler",
            "Kategori_EN": "Quranic Verses",
            "Konu_TR": "Şehitlerin Ölümsüzlüğü",
            "Konu_EN": "Immortality of Martyrs",
            "Kaynak_TR": "Kur'an-ı Kerim, Bakara Suresi 154. Ayet",
            "Kaynak_EN": "Holy Quran, Surah Al-Baqarah, Verse 154",
            "Metin_TR": "Allah yolunda öldürülenlere 'ölüler' demeyin. Hayır, onlar diridirler, fakat siz bilemezsiniz.",
            "Metin_EN": "And do not say about those who are killed in the way of Allah, 'They are dead.' Rather, they are alive, but you perceive it not.",
            "Hikmet_TR": "Vatan ve bayrak uğruna can veren şehitlerimiz rütbelerin en yücesine ermiştir.",
            "Hikmet_EN": "Our martyrs who sacrificed their lives for homeland and flag have reached the highest honor."
        },

        # --- HADİS-İ ŞERİFLER ---
        {
            "Kategori_TR": "Sahih Hadis-i Şerifler",
            "Kategori_EN": "Authentic Hadiths",
            "Konu_TR": "Vatan Hududunda Nöbet Tutmanın Fazileti",
            "Konu_EN": "Virtue of Guarding the Homeland Borders",
            "Kaynak_TR": "Sahihi Müslim (İmâre 163); Tirmizî (Zühd 27)",
            "Kaynak_EN": "Sahih Muslim (Imara 163); Tirmidhi (Zuhd 27)",
            "Metin_TR": "Allah rızası için bir gün vatan hududunda nöbet tutmak, dünya ve içindekilerden daha hayırlıdır. İki göz vardır ki onlara cehennem ateşi dokunmaz: Biri Allah korkusundan ağlayan göz, diğeri vatan nöbeti tutan göz.",
            "Metin_EN": "Guarding the border for one day for the sake of Allah is better than the world and everything in it. Two eyes will not be touched by Hellfire: an eye that wept out of fear of Allah, and an eye that spent the night guarding in the cause of Allah.",
            "Hikmet_TR": "Askerimizin ve emniyet güçlerimizin vatan nöbeti en yüce ibadetlerdendir.",
            "Hikmet_EN": "Guarding the homeland by our soldiers and security forces is among the highest forms of worship."
        },
        {
            "Kategori_TR": "Sahih Hadis-i Şerifler",
            "Kategori_EN": "Authentic Hadiths",
            "Konu_TR": "Birlik ve Kardeşlik Hukuku",
            "Konu_EN": "Law of Unity and Brotherhood",
            "Kaynak_TR": "Sahihi Buhârî (Edeb 27); Sahihi Müslim (Birr 66)",
            "Kaynak_EN": "Sahih Bukhari (Adab 27); Sahih Muslim (Birr 66)",
            "Metin_TR": "Müminler birbirlerini sevmede, birbirlerine merhamet etmede ve birbirlerini korumada bir vücut gibidirler. Vücudun bir uzvu rahatsız olursa, diğer organlar da uykusuzluk ve humma ile ona katılır.",
            "Metin_EN": "The believers in their mutual kindness, compassion and sympathy are just like one body. When one of the limbs suffers, the whole body responds to it with wakefulness and fever.",
            "Hikmet_TR": "Toplumsal dayanışma ve kardeşlik, milli birliğimizin temel taşıdır.",
            "Hikmet_EN": "Social solidarity and brotherhood are the cornerstones of our national unity."
        },

        # --- GÖNÜL SULTANLARI VE VELİ KULLAR (GENİŞLETİLMİŞ) ---
        {
            "Kategori_TR": "Gönül Sultanları & Veli Kullar",
            "Kategori_EN": "Spiritual Masters & Saints",
            "Konu_TR": "Şeyh Edebali'nin Osman Gazi'ye Vasiyeti",
            "Konu_EN": "Sheikh Edebali's Advice to Osman Gazi",
            "Kaynak_TR": "Şeyh Edebali / Osmanlı Devleti'nin Kuruluş Belgesi",
            "Kaynak_EN": "Sheikh Edebali / Foundation Legacy of the Ottoman Empire",
            "Metin_TR": "Ey oğul! İnsanları yaşat ki devlet yaşasın! Ananı, atanı hürmetle an; bereket büyüklerle beraberdir. Öfken ve nefsin bir olup aklını mağlup etmesin. Adaletli ol, merhametli ol, birliği koru!",
            "Metin_EN": "O my son! Preserve the people so that the state may live! Honor your elders; abundance is with them. Let not your anger and ego unite to defeat your reason. Be just, be merciful, preserve unity!",
            "Hikmet_TR": "Devletin bekası, adalete ve insana verilen değere dayanır.",
            "Hikmet_EN": "The continuity of the state relies upon justice and the value given to humanity."
        },
        {
            "Kategori_TR": "Gönül Sultanları & Veli Kullar",
            "Kategori_EN": "Spiritual Masters & Saints",
            "Konu_TR": "Yunus Emre - Sevgide Birlik Şuuru",
            "Konu_EN": "Yunus Emre - Consciousness of Unity Through Love",
            "Kaynak_TR": "Yunus Emre Divanı",
            "Kaynak_EN": "Divan of Yunus Emre",
            "Metin_TR": "Gelin tanış olalım, işi kolay kılalım,\nSevelim sevilelim, dünya kimseye kalmaz.\n\nBölüşürsek tok oluruz, bölünürsek yok oluruz!",
            "Metin_EN": "Come, let us know one another, let us make things easy,\nLet us love and be loved, the world remains to no one.\n\nIf we share we satisfy, if we divide we perish!",
            "Hikmet_TR": "Kardeşlik ve sevgi dili, toplumsal huzurun anahtarıdır.",
            "Hikmet_EN": "The language of love and brotherhood is the key to social tranquility."
        },
        {
            "Kategori_TR": "Gönül Sultanları & Veli Kullar",
            "Kategori_EN": "Spiritual Masters & Saints",
            "Konu_TR": "Mevlânâ Celâleddîn-i Rûmî - Birlik Mayası",
            "Konu_EN": "Mawlana Jalaluddin Rumi - The Leaven of Unity",
            "Kaynak_TR": "Mevlânâ / Mesnevî-i Şerif",
            "Kaynak_EN": "Mawlana Rumi / Masnavi",
            "Metin_TR": "Biz birleştirmek için geldik, ayırmaya değil. Sen ve ben bir elin parmakları gibiyiz. Ayrı kalırsak kırılırız, birleşirsek yumruk oluruz!",
            "Metin_EN": "We came to unite, not to divide. You and I are like the fingers of one hand. Separated we break, united we stand strong!",
            "Hikmet_TR": "Kalpleri birleşen milletleri hiçbir güç mağlup edemez.",
            "Hikmet_EN": "No power can defeat a nation whose hearts are united."
        },
        {
            "Kategori_TR": "Gönül Sultanları & Veli Kullar",
            "Kategori_EN": "Spiritual Masters & Saints",
            "Konu_TR": "Hacı Bektaş-ı Velî - Kardeşlik Hikmeti",
            "Konu_EN": "Haji Bektash Veli - Wisdom of Brotherhood",
            "Kaynak_TR": "Makâlât / Hacı Bektaş-ı Velî",
            "Kaynak_EN": "Makalat / Haji Bektash Veli",
            "Metin_TR": "Bir olalım, iri olalım, diri olalım. Eline, beline, diline sahip ol. Düşmanınızın bile insan olduğunu unutmayın!",
            "Metin_EN": "Let us be one, let us be strong, let us be alive. Control your hand, your passions, and your tongue. Never forget that even your enemy is a human being!",
            "Hikmet_TR": "Milli bünyemizi güçlü kılan en büyük unsur yüksek ahlak ve sarsılmaz birlikteliktir.",
            "Hikmet_EN": "The greatest element making our national structure strong is high morality and unwavering unity."
        },
        {
            "Kategori_TR": "Gönül Sultanları & Veli Kullar",
            "Kategori_EN": "Spiritual Masters & Saints",
            "Konu_TR": "Aziz Mahmud Hüdayi Hazretleri - Niyaz ve Hizmet",
            "Konu_EN": "Aziz Mahmud Hudayi - Devotion and Service",
            "Kaynak_TR": "Aziz Mahmud Hüdayi Divanı",
            "Kaynak_EN": "Divan of Aziz Mahmud Hudayi",
            "Metin_TR": "Vatanına ve milletine hizmet eden, hakiki kul olur. Nefsini unutan, Hakk'ı bulur. Devletine sadakat gösterenlerin hanesi mamur olur.",
            "Metin_EN": "He who serves his homeland and nation becomes a true servant. He who forgets his ego finds God. The homes of those loyal to their state remain prosperous.",
            "Hikmet_TR": "Devlete ve millete sadakatle hizmet etmek, manevi derecelerin en yücelerindendir.",
            "Hikmet_EN": "Serving the state and nation with loyalty is among the highest spiritual attainments."
        },
        {
            "Kategori_TR": "Gönül Sultanları & Veli Kullar",
            "Kategori_EN": "Spiritual Masters & Saints",
            "Konu_TR": "İmam-ı Azam Ebu Hanife - Adalet ve Hürriyet",
            "Konu_EN": "Imam Abu Hanifa - Justice and Freedom",
            "Kaynak_TR": "El-Âlim ve'l-Müte'allim",
            "Kaynak_EN": "Al-Alim wal-Muta'allim",
            "Metin_TR": "Adaletin olmadığı bir beldede ilim ve vatan sevgisi yeşermez. Haksızlığa karşı dik durmak imandandır.",
            "Metin_EN": "In a land where justice is absent, knowledge and love of homeland cannot flourish. Standing firm against injustice stems from faith.",
            "Hikmet_TR": "Adalet, toplumların ve devletlerin sarsılmaz temelidir.",
            "Hikmet_EN": "Justice is the unshakeable foundation of societies and states."
        },

        # --- MİLLİ ŞAİRLER VE EDEBİYAT ---
        {
            "Kategori_TR": "Milli Şairler & Edebi Eserler",
            "Kategori_EN": "National Poets & Literary Works",
            "Konu_TR": "Mehmet Âkif Ersoy - Birlik Şuurunun Çeliği",
            "Konu_EN": "Mehmet Akif Ersoy - The Steel of Unity Consciousness",
            "Kaynak_TR": "İstiklal Şairi Mehmet Âkif Ersoy / Safahat",
            "Kaynak_EN": "National Poet Mehmet Akif Ersoy / Safahat",
            "Metin_TR": "Girmeden tefrika bir millete, düşman giremez;\nToplu vurdukça yürekler, onu top sindiremez.\n\nSahipsiz olan memleketin batması haktır;\nSen sahip olursan bu vatan batmayacaktır!",
            "Metin_EN": "No enemy can penetrate a nation unless division enters;\nWhen hearts beat as one, no cannon can defeat them.\n\nIt is natural for an unclaimed country to sink;\nIf you claim it, this homeland shall never fall!",
            "Hikmet_TR": "Birliğimizi koruduğumuz sürece bu vatana hiçbir harici güç zarar veremez.",
            "Hikmet_EN": "As long as we maintain our unity, no external power can harm this homeland."
        },
        {
            "Kategori_TR": "Milli Şairler & Edebi Eserler",
            "Kategori_EN": "National Poets & Literary Works",
            "Konu_TR": "Mithat Cemal Kuntay - Vatan Olma Şartı",
            "Konu_EN": "Mithat Cemal Kuntay - Condition of Becoming a Homeland",
            "Kaynak_TR": "On Beş Yılı Karşılarken Şiiri",
            "Kaynak_EN": "Welcoming Fifteen Years Poem",
            "Metin_TR": "Bayrakları bayrak yapan üstündeki kandır,\nToprak, eğer uğrunda ölen varsa vatandır!",
            "Metin_EN": "What makes flags a true flag is the blood upon it;\nSoil becomes a homeland if there are those who die for it!",
            "Hikmet_TR": "Toprağı vatan yapan şey, uğrunda verilen mukaddes mücadeledir.",
            "Hikmet_EN": "What transforms soil into a homeland is the sacred struggle sacrificed for it."
        }
    ]
    return pd.DataFrame(records)

df = load_bilingual_data()

# ==========================================
# 5. BANNER (KAYAR YAZI - DİNAMİK ÇİFT DİLLİ)
# ==========================================
marquee_quotes = UI_TEXT['marquee_quotes']
marquee_text_combined = " &nbsp;&nbsp;&nbsp;&nbsp; <span>★</span> &nbsp;&nbsp;&nbsp;&nbsp; ".join(marquee_quotes)

st.markdown(f"""
<div class="half-screen-marquee">
    <div class="marquee-header-title">{UI_TEXT['marquee_title']}</div>
    <div class="marquee-content-box">
        <div class="marquee-text">
            {marquee_text_combined}
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 6. YAN MENÜ FİLTRELERİ
# ==========================================
st.sidebar.markdown(f"## {UI_TEXT['panel_title']}")

cat_col = f"Kategori_{'TR' if lang == 'Türkçe' else 'EN'}"
title_col = f"Konu_{'TR' if lang == 'Türkçe' else 'EN'}"
source_col = f"Kaynak_{'TR' if lang == 'Türkçe' else 'EN'}"
text_col = f"Metin_{'TR' if lang == 'Türkçe' else 'EN'}"
hikmet_col = f"Hikmet_{'TR' if lang == 'Türkçe' else 'EN'}"

categories = [UI_TEXT['all_cats']] + list(df[cat_col].unique())
selected_cat = st.sidebar.selectbox(UI_TEXT['cat_select'], categories)

search_term = st.sidebar.text_input(UI_TEXT['search_label'], placeholder=UI_TEXT['search_placeholder'])

st.sidebar.markdown("---")
if st.sidebar.button(UI_TEXT['random_btn']):
    random_row = df.sample(1).iloc[0]
    st.sidebar.info(f"*{random_row[title_col]}*\n\n_{random_row[text_col][:120]}..._")

st.sidebar.markdown("---")
st.sidebar.caption("© 2026 Vatan & Bayrak Sevdalıları İçin Tasarlanmıştır.")

# ==========================================
# 7. ANA İÇERİK
# ==========================================
st.title(UI_TEXT['title'])
st.caption(UI_TEXT['subtitle'])

# Filtreleme
filtered_df = df.copy()
if selected_cat != UI_TEXT['all_cats']:
    filtered_df = filtered_df[filtered_df[cat_col] == selected_cat]

if search_term:
    filtered_df = filtered_df[
        filtered_df[text_col].str.contains(search_term, case=False, regex=False) |
        filtered_df[title_col].str.contains(search_term, case=False, regex=False) |
        filtered_df[source_col].str.contains(search_term, case=False, regex=False)
    ]

# İstatistikler
col1, col2, col3 = st.columns(3)
col1.metric(UI_TEXT['total_records'], f"{len(df)} Kayıt")
col2.metric(UI_TEXT['listed_records'], f"{len(filtered_df)} Kayıt")
col3.metric(UI_TEXT['themes'], f"{len(df[cat_col].unique())} Kategori")

st.markdown("---")

# Kart Gösterimi
if len(filtered_df) == 0:
    st.warning(UI_TEXT['no_result'])
else:
    for idx, row in filtered_df.iterrows():
        st.markdown(f"""
        <div class="stCard">
            <span class="badge-tag">{row[cat_col]}</span>
            <div class="card-title">✨ {row[title_col]}</div>
            <div class="source-box">{UI_TEXT['source_lbl']} {row[source_col]}</div>
            <div class="quote-text">“{row[text_col]}”</div>
            <div class="message-box">{UI_TEXT['hikmet_lbl']} {row[hikmet_col]}</div>
        </div>
        """, unsafe_allow_html=True)

# Bilgilendirme ve Hukuki Açıklama Sekmeleri
exp_col1, exp_col2 = st.columns(2)

with exp_col1:
    with st.expander(UI_TEXT['expander_title']):
        st.markdown(UI_TEXT['expander_body'])

with exp_col2:
    with st.expander(UI_TEXT['legal_title']):
        st.markdown(UI_TEXT['legal_body'])