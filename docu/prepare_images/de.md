
<style>
    html, body {
        background: hsl(270,100%,10%);
        color: hsl(40, 100%, 50%);
        font-size: 1.2em;
    }
    img {
        max-width: 80vw;
        max-height: 50vh;
    }
</style>


# Vorbereitung der Bilder

Momentan werden Bilder in Folgendem Format unterstützt:

```
Datei-Typ: BMP
Farb-Tiefe: 3x8bit
Auflösung: 36x36 Pixel
```

als Symbole eignen sich _icons_ aus dem Schriftsatz Bereich -
das was wir als _emoji_ & _smiley_ kennen...
diese sind optimiert in sehr klein - also mit wenig Pixeln - gut erkennbar zu sein.

alternativ kannst du natürlich auch andere bild-quellen nehmen oder etwas selbst malen..

Damit der Zauberstab die Bilder anzeigen kann müssen diese in einem Speziellen Format gepeichert sein.
dieses nennt sich `Windows Bitmap` - und es ist wichtig das es als `24bits` `8R 8G 8B` gespeichert wird.

ich habe dir eine Anleitung geschrieben die genau das mit eben einem emoji macht.

am einfachsten ist es du suchst dir solch ein symbol auf dieser Website heraus:
https://openmoji.org/

alternative gibt es auch apps für den computer um diese als eine liste zu haben..
für linux z.B. den `emoji selector`

## Video Anleitung

Ich habe dir zwei kurze Videos gemacht:

1. Emoji suchen und kopieren
   <video src="openmoji.org%20search%20and%20copy%20%20candle.mp4" controls title="Title"></video>
2. Gimp - einfügen und ausrichten
   <video src="gimp%20paste%20candle.mp4" controls title="Title"></video>

## Text Anleitung

und hier als schritt für schritt text Anleitung:

1. Emoji suchen und kopieren

-   rufe die website [openmoji.org](https://openmoji.org/) auf
-   suche nach einem begriff (englisch)
    ![openmoji.org search](<openmoji.org search.png>)
-   und öffne die detail Ansicht des emoji
-   nun in die zwischenablage kopiere 
    ![openmoji.org candle](<./openmoji.org candle unicode copy.png>)
-   das *Unicode-Zeichen* mit dem kleinen *CopyButton*
    <!-- - **oder** alternative das openmoji Bild mit Strg + click auf den PNG button -->


2. Gimp - einfügen und ausrichten

ich verwende hier [Gimp (GNU Image Manipulation Program)](https://www.gimp.org/).
dies ist ein Frei Verfügbares Bild-Bearbeitungsprogramm welches auf allen gängigen PCs laufen sollte.
die Schritte können jedoch ansich auch mit jedem anderen Grafik-Program durchgeführt werden.

-   [Gimp (GNU Image Manipulation Program) installieren](https://www.gimp.org/)
-   Gimp Starten
-   lade das Beispielbild [`images/01_testpattern_smile.xcf`](./../../CIRCUITPY_disc/images/01_testpattern_smile.xcf) herunter
-   das Beispielbild `01_testpattern_smile.xcf` öffnen: `Datei - Öffnen`
-   dort gibt es nun ein _text_ object.
-   aktivieren des `text tool` (shortcut: `t`):
    ![text tool anwählen](<gimp text tool.png>)
-   nun mit einem click auf den smiley das object anwählen
-   nun ist der Text Modus aktiv.
-   unsere Schrift Größe ist ca 32pixel - so füllt das symbol die ganze Höhe aus.
-   du kannst jetzt das alte symbol löschen
-   und mit `Strg + V` das neue aus der zwischenablage einfügen
    ![gimp pasted](<gimp candle paste.png>)
-   eventuell jetzt noch die font-größe anpassen..
-   und dann falls nötig mit dem verschiebe tool passend positionieren:
    ![gimp move tool](<gimp move tool.png>)
-   am einfachsten lässt es sich mit den pfeiltasten verschieben..
-   nun noch speichern: `Datei - Exportieren als`
    -   name wählen und als Dateiendung `bmp` angeben.
        ![gimp export 1](<gimp export 1.png>)
    -   export drücken
    -   und nun `advanced options` aufklappen und `24bits` `8R 8G 8B` auswählen
        ![gimp export 2](<gimp export 2.png>)
-   nun noch das neue Bild auf den Zauberstab kopieren
    -   dafür den Zauberstab an den computer anschließen
    -   den Datei-Explorer öffnen
    -   es sollte ein neuer USB-Speicherstick mit dem Namen `CIRCUITPY` erschienen sein.
    -   dort gibt es einen Ordner `images`
        ![CIRCUITPY disc - folder images](<dolphin CIRCUITPY disc - folder images.png>)
    -   dort hinein gehört das neue bild.
