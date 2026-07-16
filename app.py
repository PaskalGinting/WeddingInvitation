from flask import Flask, render_template

app = Flask(__name__)

wedding = {

    "bride": "Essymeralda Asbella Br. Gurukinayan, S.Si.Teol",

    "groom": "Yani Cordoba Surbakti, S.T",

    "footer": "Essy & Cordoba",

    "verse_title": "1 Tawarikh 17:27",

    "verse":

    "Maka sekarang, kiranya Engkau berkenan memberkati keluarga hamba-Mu ini supaya tetap ada di hadapan-Mu untuk selama-lamanya. Sebab apa yang Engkau berkati, ya TUHAN, diberkati untuk selama-lamanya.",

    "opening":

    """Ersentabi kami alu jari sepuluh man kam kerina kalimbubu,
    puang kalimbubu, senina/sembuyak, anak beru,
    bagepe anak beru menteri kami kerina,
    amin la gia tersuratken kami gelarndu sekalak-sekalak
    ibas surat enda ula kel tama sangkut ibas pusuhndu
    ibas sie kerina, mindo maaf kami.""",

    "events":[

        {

            "title":"Persiapan",

            "date":"Kamis, 6 Agustus 2026",

            "time":"14.00 WIB - Selesai",

            "location":"GBKP Rg.P.Bulan Km7 Medan",

            "maps":"https://maps.app.goo.gl/d59ADtqkckD42rnD7"

        },

        {

            "title":"Pemberkatan",

            "date":"Jumat, 7 Agustus 2026",

            "time":"15.00 WIB - Selesai",

            "location":"GBKP Rg.P.Bulan Km7 Medan",

            "maps":"https://maps.app.goo.gl/d59ADtqkckD42rnD7"

        },

        {

            "title":"Pesta Adat",

            "date":"Sabtu, 8 Agustus 2026",

            "time":"08.00 WIB - Selesai",

            "location":"Balai Namaken",

            "maps":"https://maps.app.goo.gl/ygVbXs25xrzr6BAPA"

        }

    ],

    "closing":

    """Ikataken kami bujur man bandu kerina si enggo
    isempatkenndu reh bagepe kam simereken pasu-pasu,
    penampat rikut pedah guna ndungi ras pehagaken
    kerjanta enda.

    Ibas sie kerina ertoto kami man Tuhan Dibata
    gelah IA mereken balesen rezeki simpar
    kutengah-tengah jabundu sekalak-sekalak.

    Ibas sie ikataken kami
    Bujur ras Mejuah-juah."""
}

@app.route("/")
def home():
    return render_template("index.html", wedding=wedding)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)