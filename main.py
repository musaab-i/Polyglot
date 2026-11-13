
from dataclasses import dataclass
from random import shuffle
from drafter import *
from bakery import assert_equal

set_website_title("Polyglot")
set_site_information(
    author="Musaab I.",
    description="Improve your language skills through targeted practice.",
    sources="",
    planning=[""],
    links=["https://musaab-i.github.io/Polyglot/"]
)
hide_debug_information()
set_website_framed(False)

# ------------------------------------------------------------------------
# EXPLANATION OF CODE THAT IS POTENTIALLY BEYOND THE SCOPE OF THIS COURSE
# ------------------------------------------------------------------------
#
# 1. Text()
#    Text() displays words or sentences on the webpage. It is used
#    to show instructions, titles, questions, and other information.
#
# 2. SelectBox()
#    SelectBox() creates a dropdown menu containing choices.
#    The user can select one option from the available choices.
#    In this website, it is used to select languages, categories,
#    and vocabulary domains.
#
# 3. TextArea()
#    TextArea() creates a larger text input area. Unlike a TextBox,
#    it is designed for entering longer pieces of text.
#
# 4. Link()
#    Link() creates a clickable link that takes the user to another
#    page or route in the website.
#
# 5. Tuples
#    A tuple stores multiple values together, similar to a list.
#    Unlike a list, a tuple cannot be changed after it is created.
#    In this website, a tuple is used to check several punctuation
#    marks in the normalize_answer() function.
#
# 6. .copy()
#    copy() creates a separate copy of a list. This allows the
#    program to rearrange the copied list without changing the
#    original list.
#
# 7. .extend()
#    extend() adds all the elements from one list to another list.
#    It is used to combine vocabulary groups into one larger list.
#
# ------------------------------------------------------------------
# END OF EXPLANATIONS
# ------------------------------------------------------------------


# ============================================================
# CONSTANTS
# ============================================================

LANGUAGES = ["English", "Spanish", "Arabic"]
DOMAINS = ["General", "Mechanical Engineering", "All"]
CATEGORIES = ["Noun", "Verb", "Expression", "All"]


# 100 general nouns
GENERAL_NOUNS = """
person|persona|شخص
child|niño|طفل
parent|padre|والد
mother|madre|أم
father|padre|أب
sibling|hermano|شقيق
sister|hermana|أخت
brother|hermano|أخ
family|familia|عائلة
friend|amigo|صديق
neighbor|vecino|جار
teacher|profesor|معلم
student|estudiante|طالب
doctor|médico|طبيب
engineer|ingeniero|مهندس
worker|trabajador|عامل
farmer|agricultor|مزارع
driver|conductor|سائق
visitor|visitante|زائر
customer|cliente|زبون
home|hogar|منزل
house|casa|بيت
room|habitación|غرفة
door|puerta|باب
window|ventana|نافذة
wall|pared|جدار
floor|suelo|أرضية
roof|techo|سقف
kitchen|cocina|مطبخ
bathroom|baño|حمام
bed|cama|سرير
table|mesa|طاولة
chair|silla|كرسي
desk|escritorio|مكتب
lamp|lámpara|مصباح
key|llave|مفتاح
bag|bolsa|حقيبة
box|caja|صندوق
bottle|botella|زجاجة
cup|taza|كوب
plate|plato|طبق
spoon|cuchara|ملعقة
fork|tenedor|شوكة
knife|cuchillo|سكين
bread|pan|خبز
rice|arroz|أرز
apple|manzana|تفاحة
orange|naranja|برتقالة
banana|plátano|موزة
vegetable|verdura|خضار
fruit|fruta|فاكهة
meal|comida|وجبة
breakfast|desayuno|إفطار
lunch|almuerzo|غداء
dinner|cena|عشاء
water|agua|ماء
milk|leche|حليب
tea|té|شاي
juice|jugo|عصير
school|escuela|مدرسة
classroom|aula|فصل
lesson|lección|درس
question|pregunta|سؤال
answer|respuesta|إجابة
book|libro|كتاب
page|página|صفحة
paper|papel|ورقة
pencil|lápiz|قلم رصاص
pen|bolígrafo|قلم
notebook|cuaderno|دفتر
computer|computadora|حاسوب
screen|pantalla|شاشة
keyboard|teclado|لوحة مفاتيح
phone|teléfono|هاتف
website|sitio web|موقع إلكتروني
message|mensaje|رسالة
picture|imagen|صورة
map|mapa|خريطة
city|ciudad|مدينة
village|pueblo|قرية
street|calle|شارع
road|carretera|طريق
bridge|puente|جسر
park|parque|حديقة
garden|jardín|بستان
tree|árbol|شجرة
flower|flor|زهرة
animal|animal|حيوان
cat|gato|قطة
dog|perro|كلب
bird|pájaro|طائر
horse|caballo|حصان
sun|sol|شمس
moon|luna|قمر
sky|cielo|سماء
cloud|nube|سحابة
rain|lluvia|مطر
wind|viento|رياح
day|día|يوم
time|tiempo|وقت
"""


# 100 general verbs
GENERAL_VERBS = """
to be|ser|يكون
to have|tener|يملك
to do|hacer|يفعل
to make|hacer|يصنع
to go|ir|يذهب
to come|venir|يأتي
to walk|caminar|يمشي
to run|correr|يركض
to sit|sentarse|يجلس
to stand|estar de pie|يقف
to sleep|dormir|ينام
to wake up|despertarse|يستيقظ
to eat|comer|يأكل
to drink|beber|يشرب
to cook|cocinar|يطبخ
to read|leer|يقرأ
to write|escribir|يكتب
to speak|hablar|يتحدث
to listen|escuchar|يستمع
to hear|oír|يسمع
to see|ver|يرى
to look|mirar|ينظر
to watch|observar|يشاهد
to learn|aprender|يتعلم
to study|estudiar|يدرس
to teach|enseñar|يعلّم
to understand|entender|يفهم
to know|saber|يعرف
to think|pensar|يفكر
to remember|recordar|يتذكر
to forget|olvidar|ينسى
to ask|preguntar|يسأل
to answer|responder|يجيب
to explain|explicar|يشرح
to help|ayudar|يساعد
to work|trabajar|يعمل
to play|jugar|يلعب
to build|construir|يبني
to create|crear|ينشئ
to draw|dibujar|يرسم
to open|abrir|يفتح
to close|cerrar|يغلق
to start|empezar|يبدأ
to finish|terminar|ينهي
to stop|parar|يتوقف
to continue|continuar|يستمر
to move|mover|يحرك
to carry|llevar|يحمل
to bring|traer|يحضر
to take|tomar|يأخذ
to give|dar|يعطي
to send|enviar|يرسل
to receive|recibir|يستقبل
to buy|comprar|يشتري
to sell|vender|يبيع
to pay|pagar|يدفع
to count|contar|يعد
to calculate|calcular|يحسب
to measure|medir|يقيس
to compare|comparar|يقارن
to choose|elegir|يختار
to decide|decidir|يقرر
to find|encontrar|يجد
to search|buscar|يبحث
to use|usar|يستخدم
to change|cambiar|يغير
to improve|mejorar|يحسن
to clean|limpiar|ينظف
to wash|lavar|يغسل
to dry|secar|يجفف
to cut|cortar|يقطع
to fix|arreglar|يصلح
to repair|reparar|يصلح
to check|revisar|يفحص
to test|probar|يختبر
to plan|planear|يخطط
to organize|organizar|ينظم
to prepare|preparar|يجهز
to wait|esperar|ينتظر
to travel|viajar|يسافر
to arrive|llegar|يصل
to leave|salir|يغادر
to enter|entrar|يدخل
to return|regresar|يعود
to visit|visitar|يزور
to meet|conocer|يلتقي
to call|llamar|يتصل
to smile|sonreír|يبتسم
to laugh|reír|يضحك
to ask for|pedir|يطلب
to share|compartir|يشارك
to follow|seguir|يتبع
to lead|dirigir|يقود
to turn|girar|يدور
to push|empujar|يدفع
to pull|tirar|يسحب
to lift|levantar|يرفع
to drop|dejar caer|يسقط
to hold|sostener|يمسك
to touch|tocar|يلمس
"""


# 20 general expressions
GENERAL_EXPRESSIONS = """
Good morning|Buenos días|صباح الخير
Good evening|Buenas tardes|مساء الخير
Good night|Buenas noches|تصبح على خير
How are you?|¿Cómo estás?|كيف حالك؟
I am fine|Estoy bien|أنا بخير
Thank you|Gracias|شكراً
You are welcome|De nada|على الرحب والسعة
Please|Por favor|من فضلك
Excuse me|Disculpe|عذراً
I understand|Entiendo|أنا أفهم
I do not understand|No entiendo|لا أفهم
Can you help me?|¿Puedes ayudarme?|هل يمكنك مساعدتي؟
What does this mean?|¿Qué significa esto?|ماذا يعني هذا؟
How do you say this?|¿Cómo se dice esto?|كيف تقول هذا؟
Where is the school?|¿Dónde está la escuela?|أين المدرسة؟
I am learning|Estoy aprendiendo|أنا أتعلم
Please repeat|Repita, por favor|أعد من فضلك
Speak slowly|Hable despacio|تحدث ببطء
See you tomorrow|Hasta mañana|أراك غداً
Have a good day|Que tengas un buen día|أتمنى لك يوماً سعيداً
"""


# 40 mechanical engineering nouns
ENGINEERING_NOUNS = """
machine|máquina|آلة
engine|motor|محرك
gear|engranaje|ترس
shaft|eje|عمود
bearing|cojinete|محمل
pulley|polea|بكرة
belt|correa|حزام
chain|cadena|سلسلة
sprocket|piñón|عجلة مسننة
spring|resorte|نابض
bolt|perno|مسمار
nut|tuerca|صامولة
screw|tornillo|برغي
washer|arandela|وردة معدنية
wrench|llave inglesa|مفتاح ربط
hammer|martillo|مطرقة
drill|taladro|مثقاب
lathe|torno|مخرطة
mill|fresadora|آلة تفريز
piston|pistón|مكبس
cylinder|cilindro|أسطوانة
valve|válvula|صمام
pump|bomba|مضخة
compressor|compresor|ضاغط
turbine|turbina|توربين
fan|ventilador|مروحة
brake|freno|مكبح
clutch|embrague|قابض
frame|bastidor|هيكل
bracket|soporte|حامل
housing|carcasa|غلاف
gasket|junta|حشية
seal|sello|مانع تسرب
nozzle|boquilla|فوهة
pipe|tubería|أنبوب
tube|tubo|أنبوب
tank|tanque|خزان
reservoir|depósito|خزان
sensor|sensor|مستشعر
actuator|actuador|مشغل
"""


# 40 mechanical engineering verbs
ENGINEERING_VERBS = """
to assemble|ensamblar|يجمع
to disassemble|desmontar|يفكك
to manufacture|fabricar|يصنع
to machine|mecanizar|يشغل آلياً
to weld|soldar|يلحم
to drill|taladrar|يثقب
to mill|fresar|يفرز
to grind|rectificar|يجلي
to polish|pulir|يصقل
to cut|cortar|يقطع
to bend|doblar|يثني
to shape|dar forma|يشكل
to cast|fundir|يسبك
to forge|forjar|يطرق
to mold|moldear|يقلب
to lubricate|lubricar|يشحم
to tighten|apretar|يشد
to loosen|aflojar|يرخي
to fasten|sujetar|يثبت
to clamp|sujetar con abrazadera|يثبت بمشبك
to rotate|rotar|يدور
to spin|girar|يلف
to compress|comprimir|يضغط
to expand|expandir|يتمدد
to cool|enfriar|يبرد
to heat|calentar|يسخن
to transfer|transferir|ينقل
to transmit|transmitir|ينقل
to generate|generar|يولد
to convert|convertir|يحول
to install|instalar|يركب
to inspect|inspeccionar|يفحص
to calibrate|calibrar|يعاير
to align|alinear|يحاذي
to balance|equilibrar|يوازن
to test|probar|يختبر
to operate|operar|يشغل
to maintain|mantener|يصون
to troubleshoot|diagnosticar|يحدد العطل
to replace|reemplazar|يستبدل
"""


# 20 mechanical engineering expressions
ENGINEERING_EXPRESSIONS = """
Mechanical system|Sistema mecánico|نظام ميكانيكي
Moving component|Componente móvil|مكون متحرك
Fixed component|Componente fijo|مكون ثابت
Rotational motion|Movimiento rotacional|حركة دورانية
Linear motion|Movimiento lineal|حركة خطية
Applied force|Fuerza aplicada|قوة مطبقة
Input power|Potencia de entrada|قدرة الإدخال
Output power|Potencia de salida|قدرة الخرج
Mechanical energy|Energía mecánica|طاقة ميكانيكية
Thermal energy|Energía térmica|طاقة حرارية
Internal pressure|Presión interna|ضغط داخلي
Operating temperature|Temperatura de funcionamiento|درجة حرارة التشغيل
Safety factor|Factor de seguridad|معامل الأمان
Design requirement|Requisito de diseño|متطلب تصميم
Material property|Propiedad del material|خاصية المادة
Load capacity|Capacidad de carga|قدرة التحميل
Fluid flow|Flujo de fluido|تدفق المائع
Heat transfer|Transferencia de calor|انتقال الحرارة
Preventive maintenance|Mantenimiento preventivo|الصيانة الوقائية
Technical drawing|Dibujo técnico|رسم فني
"""


# ============================================================
# DATA CLASSES
# ============================================================

@dataclass
class Word:
    """Represent one vocabulary item in three languages.

    Args:
        english (str): English vocabulary.
        spanish (str): Spanish translation.
        arabic (str): Arabic translation.
        category (str): Noun, Verb, or Expression.
        domain (str): General or Mechanical Engineering.

    Returns:
        None: Creates one vocabulary record.
    """
    english: str
    spanish: str
    arabic: str
    category: str
    domain: str


@dataclass
class Mistake:
    """Represent one incorrect answer in the current study session.

    Args:
        source_language (str): Language of the question.
        target_language (str): Language of the expected answer.
        domain (str): General or Mechanical Engineering.
        category (str): Vocabulary category.
        question (str): Original vocabulary item.
        chosen_answer (str): Learner's incorrect answer.
        correct_answer (str): Correct translation.

    Returns:
        None: Creates one mistake record.
    """
    source_language: str
    target_language: str
    domain: str
    category: str
    question: str
    chosen_answer: str
    correct_answer: str


@dataclass
class State:
    """Store all information used by the Polyglot website.

    Args:
        words (list[Word]): All vocabulary records.
        mistakes (list[Mistake]): Current-session incorrect answers.
        source_language (str): Language used for questions.
        target_language (str): Language used for answers.
        active_indices (list[int]): Vocabulary indexes for the quiz.
        question_order (list[int]): Randomized question order.
        answer_choices (list[str]): Choices for the current question.
        question_position (int): Current quiz position.
        score (int): Correct answers in the current challenge.
        quiz_domain (str): Selected vocabulary domain.
        quiz_category (str): Selected vocabulary category.
        feedback (str): Message shown to the learner.
        translation_index (int): Current translation-practice index.
        dictionary_query (str): Current dictionary search text.
        dictionary_domain (str): Dictionary domain filter.
        include_engineering (bool): Whether engineering terms appear.

    Returns:
        None: Creates the website's state.
    """
    words: list[Word]
    mistakes: list[Mistake]
    source_language: str
    target_language: str
    active_indices: list[int]
    question_order: list[int]
    answer_choices: list[str]
    question_position: int
    score: int
    quiz_domain: str
    quiz_category: str
    feedback: str
    translation_index: int
    dictionary_query: str
    dictionary_domain: str
    include_engineering: bool


# ============================================================
# VOCABULARY HELPERS
# ============================================================

def load_group(data: str, category: str, domain: str) -> list[Word]:
    """Convert vocabulary text into Word objects.

    Args:
        data (str): Vocabulary rows separated by new lines.
        category (str): Noun, Verb, or Expression.
        domain (str): General or Mechanical Engineering.

    Returns:
        list[Word]: Parsed vocabulary records.
    """
    result = []

    for line in data.strip().split("\n"):
        parts = line.strip().split("|")

        if len(parts) == 3:
            result.append(
                Word(parts[0], parts[1], parts[2], category, domain)
            )

    return result


def load_all_words() -> list[Word]:
    """Load all general and mechanical engineering vocabulary.

    Args:
        None.

    Returns:
        list[Word]: All vocabulary records.
    """
    words = []
    words.extend(load_group(GENERAL_NOUNS, "Noun", "General"))
    words.extend(load_group(GENERAL_VERBS, "Verb", "General"))
    words.extend(load_group(GENERAL_EXPRESSIONS, "Expression", "General"))
    words.extend(load_group(ENGINEERING_NOUNS, "Noun", "Mechanical Engineering"))
    words.extend(load_group(ENGINEERING_VERBS, "Verb", "Mechanical Engineering"))
    words.extend(
        load_group(
            ENGINEERING_EXPRESSIONS,
            "Expression",
            "Mechanical Engineering"
        )
    )
    return words


def get_translation(word: Word, language: str) -> str:
    """Return a vocabulary item's translation in a selected language.

    Args:
        word (Word): Vocabulary record.
        language (str): English, Spanish, or Arabic.

    Returns:
        str: Translation or an empty string for an unsupported language.
    """
    if language == "English":
        return word.english
    elif language == "Spanish":
        return word.spanish
    elif language == "Arabic":
        return word.arabic

    return ""


def normalize_answer(answer: str) -> str:
    """Normalize a typed answer for basic comparison.

    Args:
        answer (str): Answer typed by the learner.

    Returns:
        str: Lowercase answer without surrounding spaces or final punctuation.
    """
    result = answer.strip().lower()

    while result.endswith((".", "!", "?", "،", ",")):
        result = result[:-1].strip()

    return result


def find_words(
    words: list[Word],
    domain: str,
    category: str,
    query: str
) -> list[Word]:
    """Filter vocabulary by topic, category, and search text.

    Args:
        words (list[Word]): All vocabulary records.
        domain (str): Selected domain or All.
        category (str): Selected category or All.
        query (str): Search text.

    Returns:
        list[Word]: Matching vocabulary records.
    """
    results = []
    search = query.strip().lower()

    for word in words:
        domain_matches = domain == "All" or word.domain == domain
        category_matches = category == "All" or word.category == category

        all_text = (
            word.english + " " + word.spanish + " " + word.arabic
        ).lower()

        query_matches = search in all_text

        if domain_matches and category_matches and query_matches:
            results.append(word)

    return results


def get_source_text(word: Word, state: State) -> str:
    """Get the question text in the selected source language.

    Args:
        word (Word): Current vocabulary item.
        state (State): Current website state.

    Returns:
        str: Question text.
    """
    return get_translation(word, state.source_language)


def get_translation_words(state: State) -> list[Word]:
    """Get vocabulary matching the selected translation-practice filters.

    Args:
        state (State): Current website state.

    Returns:
        list[Word]: Vocabulary matching the selected domain and category.
    """
    return find_words(
        state.words,
        state.quiz_domain,
        state.quiz_category,
        ""
    )


def get_dictionary_words(state: State) -> list[Word]:
    """Get dictionary results while respecting the engineering checkbox.

    Args:
        state (State): Current website state.

    Returns:
        list[Word]: Vocabulary matching the dictionary settings.
    """
    if not state.include_engineering:
        if state.dictionary_domain == "Mechanical Engineering":
            return []

        domain = "General"
    else:
        domain = state.dictionary_domain

    return find_words(
        state.words,
        domain,
        "All",
        state.dictionary_query
    )


def build_choices(state: State) -> list[str]:
    """Build randomized multiple-choice answers for the current question.

    Args:
        state (State): Current website state.

    Returns:
        list[str]: One correct answer and up to three distractors.
    """
    if not state.question_order:
        return []

    word_index = state.question_order[state.question_position]
    current_word = state.words[word_index]

    correct_answer = get_translation(
        current_word,
        state.target_language
    )

    choices = [correct_answer]

    distractor_indices = state.active_indices.copy()
    shuffle(distractor_indices)

    for other_index in distractor_indices:
        other_word = state.words[other_index]
        other_answer = get_translation(
            other_word,
            state.target_language
        )

        if other_answer not in choices:
            choices.append(other_answer)

        if len(choices) == 4:
            break

    shuffle(choices)
    return choices


def record_mistake(
    state: State,
    word: Word,
    selected_answer: str
) -> None:
    """Save an incorrect answer in the current-session mistake history.

    Args:
        state (State): Current website state.
        word (Word): Vocabulary item answered incorrectly.
        selected_answer (str): Learner's incorrect answer.

    Returns:
        None: Adds a Mistake record to the state.
    """
    mistake = Mistake(
        state.source_language,
        state.target_language,
        word.domain,
        word.category,
        get_source_text(word, state),
        selected_answer,
        get_translation(word, state.target_language)
    )

    state.mistakes.append(mistake)


def create_initial_state() -> State:
    """Create the starting state for a new study session.

    Args:
        None.

    Returns:
        State: Initial website state with all vocabulary loaded.
    """
    return State(
        load_all_words(),
        [],
        "English",
        "Spanish",
        [],
        [],
        [],
        0,
        0,
        "All",
        "All",
        "Welcome to Polyglot!",
        0,
        "",
        "All",
        True
    )


# ============================================================
# NAVIGATION HELPER
# ============================================================

def navigation(current_page: str) -> list:
    """Create links to useful pages except the current page.

    Args:
        current_page (str): Name of the page currently displayed.

    Returns:
        list: Navigation links to other pages.
    """
    links = []

    if current_page != "index":
        links.append(Link("Home", "index"))

    if current_page != "translation":
        links.append(Link("Translation Practice", "translation"))

    if current_page != "challenge":
        links.append(Link("Vocabulary Challenge", "challenge"))

    if current_page != "dictionary":
        links.append(Link("Dictionary", "dictionary"))

    if current_page != "mistakes":
        links.append(Link("Study Mistakes", "mistakes"))

    return links


# ============================================================
# HOME PAGE AND LANGUAGE SELECTION
# ============================================================

@route
def index(state: State) -> Page:
    """Display the home page and language settings.

    Args:
        state (State): Current website state.

    Returns:
        Page: Home page with language and activity choices.
    """
    content = [
        Header("Polyglot Language Learning Website"),
        "Practice English, Spanish, and Arabic.",
        Header("Choose your language pair", level=2),
        "Starting language:",
        SelectBox(
            "source_language",
            LANGUAGES,
            state.source_language
        ),
        "Language to practice:",
        SelectBox(
            "target_language",
            LANGUAGES,
            state.target_language
        ),
        Header("Choose a vocabulary set", level=2),
        "Vocabulary domain:",
        SelectBox("quiz_domain", DOMAINS, state.quiz_domain),
        "Vocabulary category:",
        SelectBox("quiz_category", CATEGORIES, state.quiz_category),
        Button("Save Language Choices", "save_languages"),
        Paragraph(
            "Current pair: " +
            state.source_language + " to " + state.target_language
        ),
        Header("Study activities", level=2),
        Button("Start Translation Practice", "translation"),
        Button("Start Vocabulary Challenge", "start_challenge"),
        Button("Open Dictionary", "dictionary"),
        Button("View Study Mistakes", "mistakes"),
        Paragraph(
            "Current-session mistakes: " + str(len(state.mistakes))
        ),
        Paragraph("Vocabulary records: " + str(len(state.words)))
    ]

    return Page(state, content)


@route
def save_languages(
    state: State,
    source_language: str,
    target_language: str,
    quiz_domain: str,
    quiz_category: str
) -> Page:
    """Save language selections and vocabulary filters.

    Args:
        state (State): Current website state.
        source_language (str): Starting language.
        target_language (str): Target language.
        quiz_domain (str): Selected vocabulary domain.
        quiz_category (str): Selected vocabulary category.

    Returns:
        Page: Updated home page or a language-selection message.
    """
    if source_language == target_language:
        return Page(state, [
            Header("Choose two different languages"),
            "The starting language and target language cannot be the same.",
            Button("Return Home", "index")
        ])

    state.source_language = source_language
    state.target_language = target_language
    state.quiz_domain = quiz_domain
    state.quiz_category = quiz_category
    state.feedback = "Language choices saved."

    return index(state)


# ============================================================
# TRANSLATION PRACTICE
# ============================================================

def translation_page(state: State) -> Page:
    """Build the current translation exercise.

    Args:
        state (State): Current website state.

    Returns:
        Page: Translation practice page.
    """
    available_words = get_translation_words(state)

    if len(available_words) == 0:
        content = [
            Header("Translation Practice"),
            "There are no vocabulary words in this selection.",
            "Please choose a different vocabulary set on the home page."
        ]
        content.extend(navigation("translation"))
        return Page(state, content)

    word = available_words[
        state.translation_index % len(available_words)
    ]

    content = [
        Header("Translation Practice"),
        "Translate from " + state.source_language +
        " into " + state.target_language + ".",
        Header(get_source_text(word, state), level=2),
        "Enter your translation:",
        TextBox("answer"),
        Button("Check Translation", "check_translation"),
        Paragraph(state.feedback),
        Paragraph(
            "Current-session mistakes: " + str(len(state.mistakes))
        )
    ]

    content.extend(navigation("translation"))
    return Page(state, content)


@route
def translation(state: State) -> Page:
    """Open translation practice.

    Args:
        state (State): Current website state.

    Returns:
        Page: Translation practice page.
    """
    return translation_page(state)


@route
def check_translation(state: State, answer: str) -> Page:
    """Check a translation and record an incorrect answer.

    Args:
        state (State): Current website state.
        answer (str): Answer entered by the learner.

    Returns:
        Page: Next translation exercise.
    """
    available_words = get_translation_words(state)

    if len(available_words) == 0:
        state.feedback = "There are no words in this vocabulary selection."
        return translation_page(state)

    word = available_words[
        state.translation_index % len(available_words)
    ]

    correct = get_translation(word, state.target_language)

    if normalize_answer(answer) == normalize_answer(correct):
        state.feedback = "Correct!"
    else:
        record_mistake(state, word, answer)
        state.feedback = "Suggested answer: " + correct

    state.translation_index += 1

    return translation_page(state)


# ============================================================
# VOCABULARY CHALLENGE
# ============================================================

def prepare_challenge(
    state: State,
    domain: str,
    category: str
) -> None:
    """Prepare a randomized challenge without deleting mistakes.

    Args:
        state (State): Current website state.
        domain (str): General, Mechanical Engineering, or All.
        category (str): Noun, Verb, Expression, or All.

    Returns:
        None: Updates the challenge information in State.
    """
    selected_words = find_words(
        state.words,
        domain,
        category,
        ""
    )

    state.active_indices = []

    for index_number in range(len(state.words)):
        if state.words[index_number] in selected_words:
            state.active_indices.append(index_number)

    state.question_order = state.active_indices.copy()
    shuffle(state.question_order)

    state.question_position = 0
    state.score = 0
    state.quiz_domain = domain
    state.quiz_category = category
    state.feedback = "A new randomized challenge has started."

    state.answer_choices = build_choices(state)


def challenge_page(state: State) -> Page:
    """Build the current question or challenge completion page.

    Args:
        state (State): Current website state.

    Returns:
        Page: Current question or final results.
    """
    if state.question_position >= len(state.question_order):
        total = len(state.question_order)
        perfect = total > 0 and state.score == total

        content = [
            Header("Vocabulary Challenge Complete!"),
            Paragraph("Correct answers: " + str(state.score)),
            Paragraph("Total questions: " + str(total))
        ]

        if perfect:
            content.append(
                Header("Excellent! You achieved a perfect score!")
            )
        else:
            content.append(
                "You can restart and practice the vocabulary again."
            )

        content.extend([
            Button("Restart and Randomize", "restart_challenge"),
            Button("View Study Mistakes", "mistakes"),
            Button("Return Home", "index")
        ])

        return Page(state, content)

    word_index = state.question_order[state.question_position]
    word = state.words[word_index]

    content = [
        Header("Vocabulary Challenge"),
        Paragraph(
            "Translate from " + state.source_language +
            " into " + state.target_language + "."
        ),
        Paragraph("Category: " + word.category),
        Paragraph("Topic: " + word.domain),
        Header(get_source_text(word, state), level=2),
        "Choose the correct translation:",
        SelectBox(
            "selected_answer",
            state.answer_choices,
            state.answer_choices[0]
        ),
        Button("Submit Answer", "answer_challenge"),
        Paragraph(state.feedback),
        Paragraph(
            "Question " + str(state.question_position + 1) +
            " of " + str(len(state.question_order))
        ),
        Paragraph("Correct answers so far: " + str(state.score)),
        Button("Restart and Randomize", "restart_challenge")
    ]

    content.extend(navigation("challenge"))
    return Page(state, content)


@route
def start_challenge(
    state: State,
    source_language: str,
    target_language: str,
    quiz_domain: str,
    quiz_category: str
) -> Page:
    """Start a challenge using the home-page selections.

    Args:
        state (State): Current website state.
        source_language (str): Starting language.
        target_language (str): Target language.
        quiz_domain (str): Selected vocabulary domain.
        quiz_category (str): Selected category.

    Returns:
        Page: First challenge question or an error message.
    """
    if source_language == target_language:
        return Page(state, [
            Header("Choose two different languages"),
            "Please select different starting and target languages.",
            Button("Return Home", "index")
        ])

    state.source_language = source_language
    state.target_language = target_language

    prepare_challenge(state, quiz_domain, quiz_category)

    return challenge_page(state)


@route
def challenge(state: State) -> Page:
    """Open the current vocabulary challenge.

    Args:
        state (State): Current website state.

    Returns:
        Page: Current challenge page.
    """
    if len(state.question_order) == 0:
        prepare_challenge(
            state,
            state.quiz_domain,
            state.quiz_category
        )

    return challenge_page(state)


@route
def answer_challenge(
    state: State,
    selected_answer: str
) -> Page:
    """Check a multiple-choice answer and advance the challenge.

    Args:
        state (State): Current website state.
        selected_answer (str): Answer selected by the learner.

    Returns:
        Page: Next question or final results.
    """
    if state.question_position >= len(state.question_order):
        return challenge_page(state)

    word_index = state.question_order[state.question_position]
    word = state.words[word_index]

    correct = get_translation(word, state.target_language)

    if selected_answer == correct:
        state.score += 1
        state.feedback = "Correct!"
    else:
        record_mistake(state, word, selected_answer)
        state.feedback = "Incorrect. Correct answer: " + correct

    state.question_position += 1

    if state.question_position < len(state.question_order):
        state.answer_choices = build_choices(state)

    return challenge_page(state)


@route
def restart_challenge(state: State) -> Page:
    """Restart a challenge with a new randomized question order.

    Args:
        state (State): Current website state.

    Returns:
        Page: First question of the restarted challenge.
    """
    prepare_challenge(
        state,
        state.quiz_domain,
        state.quiz_category
    )

    return challenge_page(state)


# ============================================================
# STUDY MISTAKES
# ============================================================

@route
def mistakes(state: State) -> Page:
    """Display incorrect answers grouped by language and category.

    Args:
        state (State): Current website state.

    Returns:
        Page: Current-session mistake history.
    """
    content = [
        Header("Study Mistakes"),
        Paragraph(
            "Total incorrect answers this session: " +
            str(len(state.mistakes))
        ),
        Paragraph(
            "Restarting a challenge does not erase your mistake history."
        )
    ]

    if len(state.mistakes) == 0:
        content.append("You have not recorded any mistakes yet.")

    else:
        for language in LANGUAGES:
            language_mistakes = []

            for mistake in state.mistakes:
                if mistake.target_language == language:
                    language_mistakes.append(mistake)

            if len(language_mistakes) > 0:
                content.append(Header(language, level=2))

                for domain in ["General", "Mechanical Engineering"]:
                    domain_mistakes = []

                    for mistake in language_mistakes:
                        if mistake.domain == domain:
                            domain_mistakes.append(mistake)

                    if len(domain_mistakes) > 0:
                        content.append(Header(domain, level=3))

                        for category in ["Noun", "Verb", "Expression"]:
                            category_mistakes = []

                            for mistake in domain_mistakes:
                                if mistake.category == category:
                                    category_mistakes.append(mistake)

                            if len(category_mistakes) > 0:
                                content.append(
                                    Header(
                                        category + " (" +
                                        str(len(category_mistakes)) + ")",
                                        level=4
                                    )
                                )

                                for mistake in category_mistakes:
                                    content.append(
                                        "Language pair: " +
                                        mistake.source_language + " to " +
                                        mistake.target_language
                                    )
                                    content.append(
                                        "Question: " + mistake.question
                                    )
                                    content.append(
                                        "Your answer: " +
                                        mistake.chosen_answer
                                    )
                                    content.append(
                                        "Correct answer: " +
                                        mistake.correct_answer
                                    )
                                    content.append(" ")

    content.append(
        Button("Erase All Study Mistakes", "clear_mistakes")
    )

    content.extend(navigation("mistakes"))

    return Page(state, content)


@route
def clear_mistakes(state: State) -> Page:
    """Erase all incorrect answers recorded during the current session.

    Args:
        state (State): Current website state.

    Returns:
        Page: Mistake history page showing that it is empty.
    """
    state.mistakes = []

    return Page(state, [
        Header("Study Mistakes"),
        "Your study mistake history has been erased.",
        Button("Return Home", "index"),
        Button("Start Vocabulary Challenge", "restart_challenge")
    ])


# ============================================================
# DICTIONARY
# ============================================================

def dictionary_results(state: State) -> Page:
    """Build dictionary search results.

    Args:
        state (State): Current website state.

    Returns:
        Page: Dictionary page with matching vocabulary.
    """
    content = [
        Header("Polyglot Dictionary"),
        "Search in English, Spanish, or Arabic:",
        TextBox("search_term", state.dictionary_query),
        "Choose a vocabulary topic:",
        SelectBox(
            "dictionary_domain",
            DOMAINS,
            state.dictionary_domain
        ),
        "Include mechanical engineering vocabulary:",
        CheckBox(
            "include_engineering",
            state.include_engineering
        ),
        Button("Search Dictionary", "search_dictionary"),
        Header("Search Results", level=2)
    ]

    results = get_dictionary_words(state)

    if len(results) == 0:
        content.append("No matching vocabulary was found.")

    else:
        for word in results:
            content.append(
                word.english + " | " +
                word.spanish + " | " +
                word.arabic
            )
            content.append(
                word.category + " - " + word.domain
            )

    content.extend(navigation("dictionary"))

    return Page(state, content)


@route
def dictionary(state: State) -> Page:
    """Open the multilingual dictionary.

    Args:
        state (State): Current website state.

    Returns:
        Page: Dictionary search page.
    """
    return dictionary_results(state)


@route
def search_dictionary(
    state: State,
    search_term: str,
    dictionary_domain: str,
    include_engineering: bool
) -> Page:
    """Save dictionary filters and display matching vocabulary.

    Args:
        state (State): Current website state.
        search_term (str): Text entered in the search field.
        dictionary_domain (str): Selected vocabulary domain.
        include_engineering (bool): Whether engineering terms are included.

    Returns:
        Page: Filtered dictionary results.
    """
    state.dictionary_query = search_term
    state.dictionary_domain = dictionary_domain
    state.include_engineering = include_engineering

    return dictionary_results(state)


# ============================================================
# UNIT TESTS
# ============================================================

def test_load_all_words() -> None:
    """Test vocabulary counts for all six vocabulary groups.

    Args:
        None.

    Returns:
        None: Assertions verify the vocabulary counts.
    """
    words = load_all_words()

    assert_equal(len(find_words(words, "General", "Noun", "")), 100)
    assert_equal(len(find_words(words, "General", "Verb", "")), 100)
    assert_equal(len(find_words(words, "General", "Expression", "")), 20)

    assert_equal(
        len(find_words(words, "Mechanical Engineering", "Noun", "")),
        40
    )
    assert_equal(
        len(find_words(words, "Mechanical Engineering", "Verb", "")),
        40
    )
    assert_equal(
        len(find_words(words, "Mechanical Engineering", "Expression", "")),
        20
    )

    assert_equal(len(words), 320)


def test_get_translation() -> None:
    """Test translations in English, Spanish, and Arabic.

    Args:
        None.

    Returns:
        None: Assertions verify translation selection.
    """
    word = Word("water", "agua", "ماء", "Noun", "General")

    assert_equal(get_translation(word, "English"), "water")
    assert_equal(get_translation(word, "Spanish"), "agua")
    assert_equal(get_translation(word, "Arabic"), "ماء")
    assert_equal(get_translation(word, "French"), "")


def test_normalize_answer() -> None:
    """Test answer normalization.

    Args:
        None.

    Returns:
        None: Assertions verify spaces, capitalization, and punctuation.
    """
    assert_equal(normalize_answer("  Hello! "), "hello")
    assert_equal(normalize_answer("WATER."), "water")
    assert_equal(normalize_answer("Gracias?"), "gracias")
    assert_equal(normalize_answer("  ¿Cómo estás?  "), "¿cómo estás")


def test_find_words() -> None:
    """Test dictionary filters and vocabulary searching.

    Args:
        None.

    Returns:
        None: Assertions verify category, domain, and text filters.
    """
    words = load_all_words()

    assert_equal(len(find_words(words, "General", "Noun", "")), 100)
    assert_equal(
        len(find_words(words, "Mechanical Engineering", "Noun", "")),
        40
    )
    assert_equal(len(find_words(words, "All", "All", "water")), 1)
    assert_equal(len(find_words(words, "All", "All", "notaword")), 0)


def test_translation_filter() -> None:
    """Test that translation practice uses the selected vocabulary filters.

    Args:
        None.

    Returns:
        None: Assertions verify domain and category filtering.
    """
    state = create_initial_state()

    state.quiz_domain = "General"
    state.quiz_category = "Noun"
    general_nouns = get_translation_words(state)

    assert_equal(len(general_nouns), 100)
    assert_equal(general_nouns[0].category, "Noun")
    assert_equal(general_nouns[0].domain, "General")

    state.quiz_domain = "Mechanical Engineering"
    state.quiz_category = "Verb"
    engineering_verbs = get_translation_words(state)

    assert_equal(len(engineering_verbs), 40)
    assert_equal(engineering_verbs[0].category, "Verb")
    assert_equal(engineering_verbs[0].domain, "Mechanical Engineering")


def test_dictionary_engineering_filter() -> None:
    """Test that dictionary settings control engineering vocabulary.

    Args:
        None.

    Returns:
        None: Assertions verify dictionary domain restrictions.
    """
    state = create_initial_state()

    state.dictionary_query = ""
    state.dictionary_domain = "All"
    state.include_engineering = False

    general_words = get_dictionary_words(state)

    assert_equal(len(general_words), 220)
    assert_equal(
        len(find_words(general_words, "Mechanical Engineering", "All", "")),
        0
    )

    state.dictionary_domain = "Mechanical Engineering"
    no_words = get_dictionary_words(state)

    assert_equal(len(no_words), 0)

    state.include_engineering = True
    engineering_words = get_dictionary_words(state)

    assert_equal(len(engineering_words), 100)


def test_record_mistake() -> None:
    """Test that incorrect answers are saved with the right details.

    Args:
        None.

    Returns:
        None: Assertions verify the mistake record.
    """
    state = create_initial_state()
    word = state.words[0]

    record_mistake(state, word, "incorrect")

    assert_equal(len(state.mistakes), 1)
    assert_equal(state.mistakes[0].chosen_answer, "incorrect")
    assert_equal(
        state.mistakes[0].target_language,
        state.target_language
    )


def test_prepare_challenge() -> None:
    """Test challenge setup and vocabulary filtering.

    Args:
        None.

    Returns:
        None: Assertions verify the quiz state.
    """
    state = create_initial_state()

    prepare_challenge(state, "General", "Noun")

    assert_equal(len(state.question_order), 100)
    assert_equal(state.question_position, 0)
    assert_equal(state.score, 0)
    assert_equal(state.quiz_domain, "General")
    assert_equal(state.quiz_category, "Noun")
    assert_equal(len(state.answer_choices), 4)


def test_language_selection() -> None:
    """Test that language choices are saved correctly.

    Args:
        None.

    Returns:
        None: Assertions verify the selected language pair.
    """
    state = create_initial_state()

    save_languages(
        state,
        "Arabic",
        "English",
        "General",
        "Noun"
    )

    assert_equal(state.source_language, "Arabic")
    assert_equal(state.target_language, "English")
    assert_equal(state.quiz_domain, "General")
    assert_equal(state.quiz_category, "Noun")


def test_same_language_selection() -> None:
    """Test that selecting the same language twice is rejected.

    Args:
        None.

    Returns:
        None: Assertions verify that invalid choices do not change state.
    """
    state = create_initial_state()

    save_languages(
        state,
        "Spanish",
        "Spanish",
        "General",
        "Verb"
    )

    assert_equal(state.source_language, "English")
    assert_equal(state.target_language, "Spanish")
    assert_equal(state.quiz_domain, "All")
    assert_equal(state.quiz_category, "All")


def test_restart_preserves_mistakes() -> None:
    """Test that challenge restarts preserve the mistake history.

    Args:
        None.

    Returns:
        None: Assertions verify that mistakes remain after restarting.
    """
    state = create_initial_state()

    prepare_challenge(state, "General", "Noun")

    word = state.words[state.question_order[0]]
    record_mistake(state, word, "incorrect")

    restart_challenge(state)

    assert_equal(len(state.mistakes), 1)
    assert_equal(state.question_position, 0)
    assert_equal(state.score, 0)
    assert_equal(len(state.question_order), 100)


def test_clear_mistakes() -> None:
    """Test that the clear-history route removes every mistake.

    Args:
        None.

    Returns:
        None: Assertions verify the mistake list is empty.
    """
    state = create_initial_state()
    word = state.words[0]

    record_mistake(state, word, "wrong")
    record_mistake(state, word, "also wrong")

    assert_equal(len(state.mistakes), 2)

    clear_mistakes(state)

    assert_equal(len(state.mistakes), 0)


def test_dictionary_search() -> None:
    """Test dictionary searching across different vocabulary domains.

    Args:
        None.

    Returns:
        None: Assertions verify dictionary search results.
    """
    state = create_initial_state()

    state.dictionary_query = "water"
    state.dictionary_domain = "General"
    state.include_engineering = True

    general_results = get_dictionary_words(state)

    state.dictionary_query = "gear"
    state.dictionary_domain = "Mechanical Engineering"
    engineering_results = get_dictionary_words(state)

    assert_equal(len(general_results), 1)
    assert_equal(general_results[0].english, "water")
    assert_equal(len(engineering_results), 1)
    assert_equal(engineering_results[0].english, "gear")


# ============================================================
# RUN TESTS BEFORE STARTING THE WEBSITE
# ============================================================

test_load_all_words()
test_get_translation()
test_normalize_answer()
test_find_words()
test_translation_filter()
test_dictionary_engineering_filter()
test_record_mistake()
test_prepare_challenge()
test_language_selection()
test_same_language_selection()
test_restart_preserves_mistakes()
test_clear_mistakes()
test_dictionary_search()


# ============================================================
# START THE WEBSITE
# ============================================================

start_server(
    create_initial_state(),
    site_title="Polyglot Language Learning Website"
)

