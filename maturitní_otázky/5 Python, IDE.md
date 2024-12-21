# **Python, IDE**

*Python, IDE (Visual Studio Code) – charakteristika, zařazení, vlastnosti, ne/výhody, využití, možnosti IDE, knihovny, dokumentační stringy, využití Pythonu a trh práce, AI*

## **Charakteristika Pythonu**

- **Vysokoúrovňový**: Python je blízký lidskému jazyku, což usnadňuje jeho pochopení a psaní. Oproti nízkoúrovňovým jazykům, které se více přibližují strojovému kódu, je Python intuitivnější a čitelnější.  
- **Interpretovaný**: Pythonový kód je přímo vykonáván interpretem a není nutné jej před spuštěním kompilovat do strojového kódu, jak tomu bývá u kompilovaných jazyků.  
- **Skriptovací**: Python je ideální pro psaní skriptů, tedy krátkých programů používaných k automatizaci úkolů nebo řízení jiných aplikací.  
- **Open source**: Zdrojový kód Pythonu je volně dostupný, což umožňuje jeho bezplatné využití, úpravy a sdílení s komunitou.  
- **Dynamicky typovaný**: Není potřeba explicitně deklarovat datový typ proměnných – interpret Pythonu jej automaticky určí během běhu programu. Staticky typované jazyky vyžadují přesně deklarovat typ proměnných.
- **Dostupnost:** Python je multiplatformní a lze jej používat na Unixu, Windows, macOS i Linuxu.  
- **Hybridní**: Python podporuje různé programovací styly:  
  - **Objektově orientované programování (OOP)**: Pracuje s objekty, které obsahují data (atributy) a metody (funkce).  
  - **Imperativní programování**: Program se skládá z postupně vykonávaných příkazů.  
  - **Funkcionální programování**: Zdůrazňuje práci s funkcemi a minimalizuje sdílený stav.  
- **Tvůrce:** Guido van Rossum, 1991.

## **Porovnání s ostatními jazyky**

### **Python vs. C**

- **Čitelnost a srozumitelnost:**  
  - Python má jednoduchou syntaxi, která se podobá přirozenému jazyku, což usnadňuje čtení a psaní kódu.  
  - C má složitější syntaxi, která vyžaduje větší důraz na detaily, například na správné ukončení příkazů středníkem.  
- **Rychlost:**  
  - C je rychlejší díky tomu, že je kompilovaný a umožňuje optimalizaci na nízké úrovni.  
  - Python je pomalejší, protože je interpretovaný a překládá příkazy za běhu.  
- **Použití:**  
  - Python se často používá pro rychlý vývoj aplikací, analýzu dat, strojové učení a automatizaci.  
  - C je vhodný pro systémové programování, embedded systémy a výkonnostně náročné aplikace.

### **Python vs. Java**

- **Syntaktická jednoduchost:**  
  - Python nevyžaduje závorky {} ani explicitní deklaraci typů, což zjednodušuje a urychluje vývoj.  
  - Java má přísnější pravidla pro deklaraci typů a často vyžaduje více boilerplate kódu.  
- **Platformní nezávislost:**  
  - Oba jazyky jsou multiplatformní, ale Java se spoléhá na JVM (Java Virtual Machine), což umožňuje princip „napiš jednou, spusť kdekoliv“.  
- **Použití:**  
  - Python je oblíbený ve vědecké oblasti, strojovém učení, skriptování a prototypování.  
  - Java se hojně využívá v korporátním softwaru, mobilních aplikacích (zejména Android) a velkých systémech.  
- **Výkon:**  
  - Java obvykle dosahuje vyššího výkonu díky optimalizacím JVM.

## **Výhody Pythonu**

- **Jednoduchost a snadné učení:**  
  - Python má intuitivní syntaxi, která z něj činí ideální jazyk pro začátečníky. Rozsáhlá dokumentace a aktivní komunita dále usnadňují učení a řešení problémů.  
- **Všestrannost:**  
  - Python podporuje různé programovací paradigmata, což vývojářům umožňuje použít přístup, který nejlépe odpovídá jejich potřebám.  
- **Čitelnost:**  
  - Kód v Pythonu je jasně strukturovaný díky použití odsazení namísto složených závorek, což zjednodušuje spolupráci i údržbu.

## **Nevýhody Pythonu**

- **Práce s databázemi:**  
  - Python nemá tak sofistikované vrstvy pro přístup k databázím jako některé jiné technologie, což jej může znevýhodňovat u složitých aplikací.  
- **Spotřeba paměti:**  
  - Flexibilní a dynamická povaha Pythonu často vede k vyššímu využití paměti.  
- **Runtime errors:**  
  - Chyby, které by mohly být v jiných jazycích detekovány během kompilace, se v Pythonu často objeví až během běhu programu.

## **IDE (Integrated Development Environment)**

- IDE je softwarové prostředí **navržené k usnadnění vývoje aplikací.** Typické funkce zahrnují:  
  - Editor zdrojového kódu.  
  - Kompilátor nebo interpret.  
  - Debugger.  
  - Správce souborů.  
- **Populární IDE pro Python:**  
  - **Visual Studio Code**: Bezplatné, lehké, přizpůsobitelné.  
  - **PyCharm**: Bezplatná i placená verze, nabízí mnoho funkcí, ale je náročnější na hardware.

## **Knihovny**

- Je to **sbírka předkompilovaných kódů,** které lze později použít v programu pro některé specifické dobře definované operace.  
- Když propojíme knihovnu s naším programem a spustíme tento program, linker tuto knihovnu automaticky vyhledá. Extrahuje funkce této knihovny a podle toho interpretuje program. V našem programu tak používáme metody knihovny.  
- Místo toho, abychom používali stejný kód v různých programech a dělali kód složitým, **definujeme nejčastěji používané funkce v modulech a můžeme je jednoduše importovat do programu.**
- *Ukázka práce s knihovnami:*

  ```python
  # Import knihoven
  import os
  import math
  import random

  # Vyčisti konzoli pomocí knihovny os.
  os.system("cls" if os.name == "nt" else "clear")

  # Spočítej obvod kruhu se zadaným poloměrem pomocí knihovny math.
  radius = 5
  circumference = 2 * math.pi * radius
  print(f"Obvod kruhu s poloměrem {radius} je {circumference:.2f}.")

  # Vygeneruj náhodné číslo mezi 1 a 100 pomocí knihovny random.
  random_number = random.randint(1, 100)
  print(f"Náhodné číslo mezi 1 a 100: {random_number}")
  ```

- **Standardní knihovna python:**  
  - Základní knihovny, které jsou nainstalované společně s Pythonem.  
  - Více jak 200+ (všechny jsou vypsané na stránkách pythonu)  
  - **Nejpoužívanější**: os, math, typing, datetime, enum, dataclass  
- **Často využívané knihovny, které nejsou defaultně nainstalované s Pythonem:**  
  - **TensorFlow:** používá se pro vývoj strojového učení a umělé inteligence  
  - **Matplotlib:** používá se pro vykreslování dat nebo funkcí  
  - **Pandas:** používá se v oblasti datové analýzy.
- Knihovny se dají snadno nainstalovat pomocí nástroje Pip.

## **Komentáře a Docstrings**

### **Komentáře**

- Slouží k vysvětlení kódu nebo k zaznamenání důvodů jeho implementace.  
- **Syntax:** Použití \# pro jednořádkové komentáře.  
- **Umístění:** Ideálně nad nebo vedle příslušné části kódu.

  ```python
  # Pokud je zapnutý GOD_MODE, označ vždy otázku za správně a za plný bod.
  if self.god_mode:
      question.is_correct = True
      score += 1
  ```

### **Docstring**

- Používají se pro dokumentaci modulů, funkcí, tříd a metod.  
- **Syntax:** Trojité uvozovky ''' nebo """.

  ``` python
  def calculate_grade(score, total_questions):
      """
      Vypočítá výslednou známku podle procentní úspěšnosti.

      Args:
          score: int, počet správných odpovědí.
          total_questions: int, celkový počet otázek v testu.
      Returns:
          int, výsledná známka.
      """
      success_rate = (score / total_questions) * 100
      for grade, (min_percent, max_percent) in GRADE_THRESHOLDS.items():
          if min_percent <= success_rate <= max_percent:
              return grade, success_rate
      return 5, success_rate
  ```

## **Zásady dobré dokumentace:**

- **Aktuálnost a přesnost**  
  - Dokumentace jak funkcí, modulů či samostatného kodu, by měla být vždycky aktualizovaná a up-to-date, přesná a bez jakýchkoliv technických chyb.  
- **Jednoduchost a stručnost**  
  - Dokumentace by měla být napsána stručně a jednoduše, prostým jazykem.  
  - Vyhnout se zdlouhavým a podrobným vysvětlením, stačí pouze náznak principu a kdo by měl mluvit potom za nás.  
- **Formát a styl**  
  - Dokumentace, jak funkcí či kodu, by měla zachovat stejný formát napříč celému projektu. Doporučuje se psát komentáře ve větách, dodržovat konvence formátování.  
- Více informací na zásady dobré dokumentace a vývoje aplikací v pythonu: PEP8

## **Využití Pythonu a trh práce**

### **Využití Pythonu**

- **Vývoj backendových serverů**  
  - **Backend:**
    - Je to opak tzv. “frontendu \- klientu”, je to tedy část stránky, kterou uživatel nevidí.  
    - Jeho častou formou je **REST API.**
      - REST API (Representational State Transfer Application Programming Interface) je způsob komunikace mezi klientem (frontend) a serverem (backend), který využívá standardní webové protokoly (např. HTTP) k přístupu a manipulaci se zdroji prostřednictvím jasně definovaných endpointů. ( DELETE /user/{user\_id} )  
    - Často operuje s databází, cache či ostatními services dané firmy.  
  - Příklad: **Instagram, Spotify** – obě aplikace využívají Python pro jejich backend.  
  - **Frameworky:** Django, Flask.  
- **Datová analýza**  
  - Využívá se v procesu zkoumání, čištění, transformací a modelování dat s cílem objevit užitečné informace, podpořit závěry a usnadnit rozhodování.  
  - Například firma může využít analýzu dat k optimalizaci svého dodavatelského řetězce, což vede ke snížení nákladů a zlepšení efektivity. Nebo technologická společnost může využít analýzu dat k pochopení chování uživatelů, což vede ke zlepšení návrhu produktů a lepší interakci s uživately.  
  - Ve vědě se analýza dat používá například ke zpracování experimentálních výsledků, ověřování hypotéz, hledání vzorců v datech nebo ke statistickému modelování.  
  - **Knihovny:** Pandas, Matplotlib, Seaborn.  
- **Automatizace a skriptování**  
  - Automatizace rutinních úkolů a testování softwaru.  
  - Příklad: **Automatizace e-mailů, generování reportů.**  
  - **Nástroje:** Selenium, PyAutoGUI.

### **Trh práce a kariéra Python Developera**

- **Proč se stát Python Developerem?**  
  - Python patří mezi 3 nejžádanější jazyky na světě (zdroj: StackOverflow 2020).  
  - **Nabízí širokou škálu kariérních možností:**  
    - **Backend Developer**  
      - Vytváří, spravuje a optimalizuje serverovou logiku, databáze a API, které podporují funkčnost aplikací.  
    - **Datový analytik**  
      - Sbírá, zpracovává a interpretuje data s cílem odhalit užitečné informace, identifikovat trendy a podpořit firemní rozhodování.  
    - **AI inženýr**  
      - Navrhuje, vyvíjí a implementuje algoritmy a modely umělé inteligence, které řeší komplexní problémy nebo automatizují procesy.  
    - **Testovací inženýr**  
      - Navrhuje, provádí a automatizuje testy softwaru nebo hardwaru, identifikuje chyby a zajišťuje, že produkty splňují požadovanou kvalitu a funkčnost.  
- Je to jedna z nejlehčích cest jak se dostat do světa programování a dostat první zaměstnání.

## **Machine Learning, AI**

### **Artificial Intelligence (AI)**

- Široký obor informatiky zaměřený na vývoj strojů nebo systémů, které mohou vykonávat úkoly, jež obvykle vyžadují lidskou inteligenci, jako je řešení problémů nebo rozhodování.  
- Hlavním cílem umělé inteligence je napodobit lidský mozek a umožnit tak systémům samostatně vnímat, uvažovat a jednat.  
- **Typy AI:**  
  - **Weak:** Umělá inteligence navržená pro konkrétní úkol (např. rozpoznávání obličeje, hlasoví asistenti).  
  - **General:** Hypotetická umělá inteligence, která by zvládla jakýkoli intelektuální úkol lépe než ho zvládne člověk (stále ale pouze jen teoreticky).

### **Machine Learning (ML)**

- Odvětví umělé inteligence (AI) zaměřené na vytváření algoritmů, které umožňují systémům učit se z dat a v průběhu času se samostatně zlepšovat.  
- **ML vs AI:**  
  - **AI**: široký obor simulující inteligenci podobnou lidské.  
  - **ML**: podmnožina umělé inteligence, která se zaměřuje na učení vzorů z dat a zlepšování výkonu.  
- Algoritmy provádějí předpovědi nebo klasifikace na základě vstupních dat.  
- Model se upravuje tak, aby se snížily chyby. Tento iterační proces pokračuje, dokud není dosaženo prahové hodnoty přesnosti.

### **Python pro vývoj AI, ML**

- Python je pro AI a ML využíván díky své snadné použitelnosti, která vývojářům umožňuje rychle vytvářet prototypy a implementovat algoritmy. Následná údržba aplikace nebývá drahá a nevyžaduje ani tolik pozornosti.  
- Python však nemusí být nejlepší volbou pro aplikace vyžadující extrémní výkon nebo nízkou latenci, protože bývá pomalejší než jazyky jako C++ nebo R.
- Oproti tomu má však navrh co se týče ekosystému. Python má rozsáhlou sadu knihoven a nástrojů, které jsou často aktualizovány a jsou velice dobře zdokumentované, což některým starším jazykům chybí.

## Review

- **Otázky pro kontrolu:**
  1. Co znamená, že je Python jazyk interpretovaný?
  2. Co znamená, že je Python jazyk dynamicky typovaný?
  3. Jak by vypadal jazyk, který je kompilovaný a staticky typovaný? V čem by měl návrh na rozdíl od Pythonu?
  4. V čem se liší Python od ostatních jazyků? V čem má návrh? V čem je naopak horší?
  5. Co je to IDE? Jaké základní nástroje by mělo každé solidní IDE obsahovat? Jaké jsou nejpopulárnější možnosti pro Python?
  6. Co jsou to knihovny v Pythonu? Proč je využíváme?
  7. Co je to standardní knihovna Pythonu? Jaké jsou její nejpoužívanější knihovny? Jak nainstalovat knihovnu, která není součástí standardní knihovny?
  8. Co jsou to komentáře a docstringy v Pythonu? Jaký je mezi nimi rozdíl? K čemu slouží?
  9. Jak psát správně dokumentaci? Co je to PEP8?
  10. Python se využívá ve vývoji backendu. Co je to backend a za co zodpovídá backend developer?
  11. Python se často objevuje v kontextu datové analýzy. Co je to datová analýza? Jaké je její reálné využití v praxi?
  12. Co je to Artificial Intelligence (AI)? Jaký je její hlavní cíl? Jaké máme základní typy?
  13. Co je to Machine Learning (ML)? Jak se liší od AI? Jak bychom mohli využít ML v praxi?
  14. Python pro vývoj AI a ML. Proč ano? Proč ne? Po kterém jazyce sáhnout, když ne Python?

- **Ukázkové odpovědi:**
  1. Python je interpretovaný jazyk, což znamená, že jeho kód je vykonáván přímo interpreterem řádek po řádku. Na rozdíl od kompilovaných jazyků není potřeba kód nejprve převést do strojového kódu pomocí kompilátoru, což umožňuje okamžité spuštění programu.
  2. Znamená to, že jako vývojář nemusíte explicitně určovat datový typ proměnných. To usnadňuje a urychluje vývoj aplikací. Dynamicky typované jazyky jsou oblíbené zejména mezi začátečníky, protože odstraňují potřebu řešit složité deklarace datových typů.
  3. U kompilovaného jazyka bychom před spuštěním museli počkat, než se kód zkompiluje. Vývoj by také zabral více času, protože by bylo nutné manuálně deklarovat datové typy pro každou proměnnou. Výsledná aplikace by však byla rychlejší a bezpečnější díky statickému typování. Navíc by většina chyb byla odhalena už při kompilaci, což minimalizuje riziko výskytu runtime chyb.
  4. Python se zásadně liší svou jednoduchostí a syntaxí. Je flexibilní a rychlý na naučení, což usnadňuje vývoj aplikací, který je díky dynamickému typování a interpreteru mnohem rychlejší a aplikace se i snadněji udržují a rozšiřují. Na druhou stranu není ideální pro vývoj aplikací s vysokými nároky na rychlost a optimalizaci. Dynamické typování může vést k runtime chybám, které jsou často těžko replikovatelné a mohou způsobit pád aplikace v produkční verzi.
  5. IDE je software, který poskytuje prostředí pro psaní kódu a usnadňuje práci vývojáře tím, že shromažďuje všechny potřebné nástroje a informace na jednom místě. Každé IDE by mělo obsahovat editor zdrojového kódu, debugger, kompilátor nebo interpreter a file explorer. Nejpopulárnější volby pro Python jsou VSCode a PyCharm.
  6. Je to předkompilovaný kód, který si můžeme kdykoliv importovat do našeho projektu. Tím ušetříme čas a práci, protože se vyhneme znovu vymýšlení a implementaci logiky, která už byla dávno navržena a implementována za nás.
  7. Je to sada knihoven, které jsou součástí standardní instalace Pythonu. Mezi nejpoužívanější knihovny patří například os, která nabízí mnoho metod pro práci s operačním systémem. Často se také využívá knihovna math. Knihovny, které nejsou součástí základní instalace Pythonu, lze doinstalovat pomocí nástroje Pip.
  8. Komentáře v Pythonu slouží k dokumentaci kódu, aby usnadnily jeho čtení a pochopení pro nás i ostatní vývojáře. Docstringy jsou speciální typ komentářů určený k popisu funkcí, tříd nebo modulů.
  9. Dokumentace by vždy měla být technicky přesná a aktuální, aby se předešlo chybám při vývoji. Měla by být co nejstručnější, zachycovat hlavní myšlenku a nechat kód mluvit za sebe. Zároveň je důležité, aby dokumentace dodržovala dohodnutý formát. PEP8 je style guide přímo od Pythonu, který definuje, jak by měl vypadat kód, včetně doporučení pro jeho strukturu, formátování a komentáře.
  10. Backend je část webové aplikace, která není viditelná pro uživatele. Na rozdíl od frontendu, který přímo interaguje s uživatelem, backend zajišťuje logiku a zpracování na pozadí. Často bývá označován jako server, zatímco frontend jako klient. Backend úzce spolupracuje s databází, kterou využívá pro ukládání a správu dat. Úkolem backend developera je tento server vyvíjet, rozšiřovat a zajišťovat jeho bezproblémový provoz.
  11. Datová analýza zahrnuje manipulaci, čištění a modelování dat s cílem získat nové a užitečné informace. Firmy často hledají datové analytiky například pro optimalizaci svého dodavatelského řetězce nebo pro získání nových informací pro podporu důležitých rozhodnutí. Datová analýza však nachází uplatnění i mimo komerční sféru, například ve vědeckých disciplínách, kde slouží třeba k ověřování různých hypotéz.
  12. Tato oblast informatiky se zaměřuje na vývoj strojů nebo systémů, které jsou schopné vykonávat úkoly, jež obvykle vyžadují lidskou inteligenci. Hlavním cílem umělé inteligence (AI) je napodobit fungování lidského mozku, což by umožnilo systémům jednat, přemýšlet a vykonávat práci samostatně, bez lidského zásahu. AI dělíme na dva typy: Weak AI, která je vyvinutá pro konkrétní úkoly, jako jsou třeba překladače nebo rozpoznávání tváří, a General AI, což je zatím teoretická umělá inteligence, která by byla schopná vykonávat jakýkoli úkol stejně dobře jako člověk, a to i lépe.
  13. Strojové učení (ML) je odvětví umělé inteligence (AI), které se zaměřuje na vývoj algoritmů umožňujících systémům učit se z dat a postupně se samostatně zlepšovat. Na rozdíl od AI, která usiluje o napodobení lidské inteligence, se ML soustředí na rozpoznávání vzorů v datech a optimalizaci výkonu. V praxi se s ním můžeme setkat například při algoritmech doporučování, jakými jsou systémy na TikToku, YouTube nebo Netflixu, kde ML analyzuje uživatelovu interakci s obsahem a na základě toho doporučuje nový obsah. V bankovnictví se ML využívá například při detekci podvodů, kdy algoritmy analyzují transakce a identifikují neobvyklé nebo podezřelé aktivity.
  14. Python je velmi populární pro vývoj AI a ML díky své jednoduchosti a rychlosti vývoje aplikací. Je oblíbený také díky velkému ekosystému knihoven a nástrojů, které usnadňují práci při vývoji AI a ML. Python však není ideální pro systémy, kde je kladeno důraz na extrémní rychlost a nízkou latenci, protože jeho výkon může v těchto případech být nedostatečný. U aplikací s těmito nároky se vývojáři často obracejí na nízkourovňové kompilované jazyky, jako je C++ nebo R, které jsou také oblíbenou volbou pro vývoj v oblasti AI a ML s těmito nároky.
