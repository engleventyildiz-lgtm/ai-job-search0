# Codex ile kariyer asistanı kurulumu

Bu belge mevcut çerçeveyi Codex ile kullanmaya başlamak içindir. Yeni bir uygulama veya tamamlanmış otomatik kurulum değildir. Asıl kurallar `AGENTS.md`, `CLAUDE.md` ve `.claude/` altında kalır.

## 1. Kişisel çalışma kopyası

Herkese açık fork yalnızca kaynak kod ve kişisel bilgi içermeyen şablonlar içindir. `/setup`, Git'in takip ettiği profil ve CV şablonu dosyalarını değiştirir. `.gitignore` bu değişiklikleri korumaz.

Kişisel kullanım için GitHub'da fork olmayan, bağımsız ve **Private** bir depo oluşturun. Fork'u silmeniz gerekmez. Kaynak projeyi yerel bilgisayarınıza klonlayıp `origin` adresini özel deponuzla değiştirin. Aşağıdaki `PRIVATE_REPO_URL` ifadesini yeni özel deponun HTTPS adresiyle değiştirin; mevcut klasörünüz varsa farklı bir klasör adı kullanın:

```powershell
git clone https://github.com/engleventyildiz-lgtm/ai-job-search0.git career-local
cd career-local
git remote rename origin framework
git remote add origin PRIVATE_REPO_URL
git remote -v
```

GitHub'da yeni deponun **Private** olduğunu ve `origin` adresinin onu gösterdiğini kontrol edin. İlk aktarımda `git push -u origin master` kullanılır. Kişisel bilgileri `framework` uzak deposuna göndermeyin. Gizlilik doğrulanamıyorsa profil doldurmayın; önce yerel, paylaşılmayan bir çalışma kopyası kullanın.

Bu kılavuz bir inceleme dalındaysa önce ilgili değişiklikleri kaynak deponun `master` dalına alın veya inceleme dalını açıkça klonlayın.

## 2. Gerekli araçlar

- Git ve Python 3.10 veya üzeri.
- Yerel çalışma için Codex CLI veya yerel klasöre erişebilen Codex masaüstü ortamı. Başlangıç: https://learn.chatgpt.com/docs/cli
- İlan arama için Bun. Kurulum: https://bun.sh
- Varsayılan PDF şablonları için Windows'ta MiKTeX; `lualatex` ve `xelatex` komutları kullanılabilir olmalı. Paket ayrıntıları: `SETUP.md`.
- PDF metin kontrolü için `python -m pip install pypdf`; çerçeve lint kontrolü için `python -m pip install pyyaml`.

Kurulumdan sonra terminali yeniden açın. Windows'ta `python` veya `py` kullanın; `python3` her kurulumda bulunmaz. Araç yükleme ve GitHub/ChatGPT oturum açma işlemleri kendi bilgisayarınızda tamamlanır. Bu depoda API anahtarı saklamayın.

```powershell
python tools/career_check.py
```

Bu salt okunur kontrol; bulunan araçları, eksik isteğe bağlı bileşenleri ve profil yer tutucusunu raporlar. Çıkış kodu 0 yalnızca temel çerçeve dosyalarının bulunduğunu gösterir; tüm sistemin çalıştığını göstermez.

## 3. Codex ile profil hazırlama

Özel depoyu yerel Codex ortamında açın. CLI kullanıyorsanız klasörde `codex` çalıştırıp hesabınızla giriş yapın. Codex'e normal Türkçe talimat verin:

> AGENTS.md, CODEX_KURULUM_TR.md ve .claude/commands/setup.md dosyalarını oku. Önce çalışma deposunun gizliliğini ve Git uzak adreslerini doğrula. documents/cv içindeki güncel CV'yi kaynak alarak profil kurulumunu yürüt. Belirsiz bilgileri sor; sayı, deneyim, sertifika veya dil seviyesi uydurma. Kişisel bilgileri herkese açık depoya gönderme.

Güncel CV'yi `documents/cv/` içine koyun. Üç hedef rol kümesi belirlenebilir: CAPEX/Project Management, Engineering/Maintenance Management, Plant Engineering/Resident Engineer. Bunlar tercih başlıklarıdır; deneyim iddiası değildir. Eski sohbetlerden gelen bilgileri güncel belgeyle karşılaştırın; çelişkileri otomatik kesinleştirmeyin.

## 4. İlk başvuruyu test etme

Önce tam ilan metniyle çalışın; böylece portal erişimi ayrı bir belirsizlik oluşturmaz:

> .claude/commands/apply.md iş akışını şu ilan için uygula. Desteklenmeyen yetkinlikleri açıkça belirt. Taslak ve inceleme aşamalarını ayır. PDF'leri derle, görsel düzenlerini ve çıkarılan metni kontrol et. Başvuruyu gönderme; sonucu ve eksik kontrolleri raporla.

Claude Code'un `/setup` ve `/apply` komutlarının Codex'te aynı şekilde kayıtlı olduğunu varsaymayın. Yukarıdaki gibi ilgili dosyayı normal bir taleple okutun. Claude'a özel `Agent`, `WebFetch`, `AskUserQuestion`, `$ARGUMENTS` ve `SCRATCHPAD` ifadeleri mevcut ortamın araçları, kullanıcı girdisi ve gerçek geçici klasörüyle eşleştirilmelidir. `.claude/settings.json` Codex izinlerini yapılandırmaz. Mevcut ortamın izin kurallarını kullanın; eksik kabiliyeti tamamlanmış gibi göstermeyin.

Başarılı ilk test: kaynakla tutarlı CV/ön yazı, derlenen ve incelenen PDF'ler, okunabilir PDF metni ve yerel başvuru arşivi. ATS metin kontrolü, işverenin gerçek ATS puanı veya işe alım garantisi değildir.

## 5. İlan taramasını ekleme

İlk başvuru testi geçtikten sonra `python tools/install_portal_clis.py` ile mevcut portalların bağımlılıklarını kurun. Orijinal talimatlar `SETUP.md` ve `.claude/skills/job-scraper/` altındadır. Türkiye kaynaklarının veya her şirketin otomatik desteklendiğini varsaymayın. LinkedIn için ilgili skill'in erişim ve kullanım koşullarını okuyun. Gmail/Notion bağlantıları isteğe bağlıdır ve ayrıca yetkilendirilir.

## Durum ve sınırlar

Bu ekleme yalnızca Codex başlangıç kılavuzu ve teşhis aracıdır. Kullanıcının bilgisayarına araç yüklemez, profil oluşturmaz, otomatik görev kurmaz, başvuru göndermez. Kaynak dosyalar hazırlanmış olması uçtan uca doğrulama yerine geçmez.
