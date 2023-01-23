from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from twilio.rest import Client, TwilioException
from twilio.twiml.voice_response import Gather, VoiceResponse, Say
from django.template import Context, loader
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.voice_response import VoiceResponse, Say
from django.urls import reverse
from googletrans import Translator
import os
from .apps import QueryAppConfig
import requests

from gtts import gTTS

url = ""


def index(request):
    return HttpResponse("# Welcome to Team EARTH BENDERS  ====UIA====.")


tl = {
    "LANGUAGE": "LANGUAGE TAG",
    "afrikaans": "af-ZA",
    "amharic": "am-ET",
    "armenian": "hy-AM",
    "azerbaijani ": "az-AZ",
    "indonesian ": "id-ID",
    "malay": "ms-MY",
    "bengali": "bn-IN",
    "catalan ": "ca-ES",
    "czech": "cs-CZ",
    "danish": "da-DK",
    "german ": "de-DE",
    "english": "en-IN",
    "spanish ": "es-ES",
    "basque": "eu-ES",
    "filipino ": "fil-PH",
    "french ": "fr-FR",
    "galician ": "gl-ES",
    "georgian": "ka-GE",
    "gujarati ": "gu-IN",
    "croatian ": "hr-HR",
    "zulu ": "zu-ZA",
    "icelandic": "is-IS",
    "italian ": "it-IT",
    "javanese ": "jv-ID",
    "kannada ": "kn-IN",
    "khmer ": "km-KH",
    "lao ": "lo-LA",
    "latvian ": "lv-LV",
    "lithuanian ": "lt-LT",
    "hungarian": "hu-HU",
    "malayalam": "ml-IN",
    "marathi ": "mr-IN",
    "dutch ": "nl-NL",
    "nepali ": "ne-NP",
    "norwegian bokmÃ¥l ": "nb-NO",
    "polish ": "pl-PL",
    "portuguese": "pt-PT",
    "romanian": "ro-RO",
    "sinhala ": "si-LK",
    "slovak": "sk-SK",
    "slovenian": "sl-SI",
    "sundanese ": "su-ID",
    "swahili ": "sw-TZ",
    "finnish ": "fi-FI",
    "swedish ": "sv-SE",
    "tamil ": "ta-IN",
    "telugu": "te-IN",
    "vietnamese ": "vi-VN",
    "turkish ": "tr-TR",
    "urdu ": "ur-IN",
    "greek": "el-GR",
    "bulgarian": "bg-BG",
    "russian": "ru-RU",
    "serbian ": "sr-RS",
    "ukrainian ": "uk-UA",
    "hebrew ": "he-IL",
    "arabic": "ar-AE",
    "persian": "fa-IR",
    "hindi": "hi-IN",
    "thai": "th-TH",
    "korean": "ko-KR",
    "chinese": "cmn-Hant-TW",
    "japanese ": "ja-JP",
}
gl = {
    "af": "afrikaans",
    "sq": "albanian",
    "am": "amharic",
    "ar": "arabic",
    "hy": "armenian",
    "az": "azerbaijani",
    "eu": "basque",
    "be": "belarusian",
    "bn": "bengali",
    "bs": "bosnian",
    "bg": "bulgarian",
    "ca": "catalan",
    "ceb": "cebuano",
    "ny": "chichewa",
    "zh-cn": "chinese (simplified)",
    "zh-tw": "chinese (traditional)",
    "co": "corsican",
    "hr": "croatian",
    "cs": "czech",
    "da": "danish",
    "nl": "dutch",
    "en": "english",
    "eo": "esperanto",
    "et": "estonian",
    "tl": "filipino",
    "fi": "finnish",
    "fr": "french",
    "fy": "frisian",
    "gl": "galician",
    "ka": "georgian",
    "de": "german",
    "el": "greek",
    "gu": "gujarati",
    "ht": "haitian creole",
    "ha": "hausa",
    "haw": "hawaiian",
    "iw": "hebrew",
    "he": "hebrew",
    "hi": "hindi",
    "hmn": "hmong",
    "hu": "hungarian",
    "is": "icelandic",
    "ig": "igbo",
    "id": "indonesian",
    "ga": "irish",
    "it": "italian",
    "ja": "japanese",
    "jw": "javanese",
    "kn": "kannada",
    "kk": "kazakh",
    "km": "khmer",
    "ko": "korean",
    "ku": "kurdish (kurmanji)",
    "ky": "kyrgyz",
    "lo": "lao",
    "la": "latin",
    "lv": "latvian",
    "lt": "lithuanian",
    "lb": "luxembourgish",
    "mk": "macedonian",
    "mg": "malagasy",
    "ms": "malay",
    "ml": "malayalam",
    "mt": "maltese",
    "mi": "maori",
    "mr": "marathi",
    "mn": "mongolian",
    "my": "myanmar (burmese)",
    "ne": "nepali",
    "no": "norwegian",
    "or": "odia",
    "ps": "pashto",
    "fa": "persian",
    "pl": "polish",
    "pt": "portuguese",
    "pa": "punjabi",
    "ro": "romanian",
    "ru": "russian",
    "sm": "samoan",
    "gd": "scots gaelic",
    "sr": "serbian",
    "st": "sesotho",
    "sn": "shona",
    "sd": "sindhi",
    "si": "sinhala",
    "sk": "slovak",
    "sl": "slovenian",
    "so": "somali",
    "es": "spanish",
    "su": "sundanese",
    "sw": "swahili",
    "sv": "swedish",
    "tg": "tajik",
    "ta": "tamil",
    "te": "telugu",
    "th": "thai",
    "tr": "turkish",
    "uk": "ukrainian",
    "ur": "urdu",
    "ug": "uyghur",
    "uz": "uzbek",
    "vi": "vietnamese",
    "cy": "welsh",
    "xh": "xhosa",
    "yi": "yiddish",
    "yo": "yoruba",
    "zu": "zulu",
}

gg = {"english": "en", "hindi": "hi"}


@csrf_exempt
def high_response(request: HttpRequest, s="0", l="en-IN") -> HttpResponse:
    if s == "0":
        vr = VoiceResponse()

        with vr.gather(
            input="speech",
            action="/response/" + l + "/" + s + "/",
            method="POST",
            finish_on_key="#",
            timeout=4,
            enhanced="true",
            speechModel="phone_call",
        ) as gather:

            gather.say(
                "Welcome to farmers helpline,Please provide the language",
                voice="Polly.Aditi",
                language="en-IN",
            )
            vr.redirect("")
        return HttpResponse(str(vr), content_type="text/xml")
    else:
        vr = VoiceResponse()
        with vr.gather(
            input="speech",
            action="/response/" + l + "/" + s + "/",
            method="POST",
            finish_on_key="#",
            timeout=4,
            enhanced="true",
            speechModel="phone_call",
            language=l,
        ) as gather:
            translator = Translator()
            keys = list(tl.keys())
            values = list(tl.values())
            pl = keys[values.index(l)]
            print("Selected language:", pl, gg[pl])
            translation = translator.translate("Please State Your Query", dest=gg[pl])
            print("Trans: ", translation)
            gather.say(translation.text, voice="Polly.Aditi", language=l)
            vr.redirect("")
        return HttpResponse(str(vr), content_type="text/xml")


@csrf_exempt
def handle_response(request: HttpRequest, l="en", s=0) -> HttpResponse:
    vr = VoiceResponse()
    speech = request.POST.get("SpeechResult", "")
    print(speech)
    translator = Translator()
    if s == "0":
        speech.lower()
        speech = speech[:-1]
        l = tl[speech.lower()]
        vr.say(speech)
    else:
        translation = translator.translate(speech, dest="en")
        print(translation.text)
        speech = get_query(translation.text)
        speech.replace(" ", "")
        speech = speech[:-1]
        vr.pause(length=2)
        keys = list(tl.keys())
        values = list(tl.values())
        pl = keys[values.index(l)]
        translation = translator.translate(speech, dest=gg[pl])

        s = int(s)
        s += 1
        s = str(s)
        with vr.gather(
            input="speech",
            action="/callTo/" + s + "/" + l + "/",
            method="POST",
            finish_on_key="#",
            timeout=2,
            enhanced="true",
            speechModel="phone_call",
            language=l,
        ) as gather:
            gather.say(translation.text, voice="Polly.Aditi", language=l)
    s = int(s)
    s += 1
    s = str(s)
    vr.redirect("/callTo/" + s + "/" + l + "/")
    return HttpResponse(str(vr), content_type="text/xml")


def login(request):
    template = loader.get_template("index.html")
    return render(request, "index.html")


def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())


# Create your views here.


@csrf_exempt
def choose_theater(
    request: HttpRequest,
) -> HttpResponse:
    vr = VoiceResponse()
    vr.say("Welcome to movie info!")
    with vr.gather(
        finish_on_key="#",
        timeout=20,
    ) as gather:
        gather.say("Please choose a theater and press #")

    vr.say("We did not receive your selection")
    vr.redirect("")

    return HttpResponse(str(vr), content_type="text/xml")


def get_query(query):
    response = QueryAppConfig.query_pipeline.run(
        query=query, params={"Generator": {"top_k": 1}, "Retriever": {"top_k": 5}}
    )
    msg0 = {"query": query, "answer": response["answers"][0].answer}
    requests.post(url, json=msg0)
    print(response["answers"][0].answer)
    return response["answers"][0].answer


@csrf_exempt
def search(request):
    if request.POST.get("input1"):
        s = get_query(request.POST.get("input1"))
        u = request.POST.get("input1")
        template = loader.get_template("search.html")
        return render(request, "../templates/search.html", {"s": s, "u": u})
    template = loader.get_template("search.html")
    return render(request, "../templates/search.html", {"s": "", "u": ""})


@csrf_exempt
def msg(request):
    msg = request.POST.get("Body")
    number = request.POST.get("From")
    client = Client(
        "ACc71cd837884227dc3aa2e96d0e26686b", "2635f194a5675f7fd37a84aaef6d9848"
    )
    print(msg)
    text = get_query(msg)
    client.messages.create(to=number, from_="+12623333369", body=text)
    return HttpResponse("messages sent!", 200)
