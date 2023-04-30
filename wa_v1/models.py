import os.path

from django.shortcuts import render

from advise_agent.advise import Advise


PHYSICS = "physics"
MATH = "math"
CHEM = "chem"
BIO = "bio"
SOC_SCI = "soc_sci"
FOREIGN = "foreign"
GEO = "geo"
HIST_BEL = "hist_bel"
HIST_W = "hist_w"
ART = "art_ex"

AVIA = "avia"
VET = "vet"
WAR = "war"
DESIGN = "design"
JOURN = "journ"
ENGIN = "engin"
IT = "it"
HIST = "hist"
FOREST = "forest"
LINGO = "lingo"
MED = "med"
INT_COM = "int_com"
MUSIC = "music"
TEACH = "teach"
PSY = "psy"
COM = "com"
AGRI = "agri"
SS = "ss"
THEO = "theo"
TECHN = "techn"
TECHNL = "technl"
TOURISM = "turism"
PHYS_CULT = "phys_cult"
ECON = "econ"
LAW = "law"

R_TRANS = {
    PHYSICS: "физика",
    MATH: "математика",
    CHEM: "химия",
    BIO: "биология",
    SOC_SCI: "обществоведение",
    FOREIGN: "иностранный язык",
    GEO: "география",
    HIST_BEL: "история Беларуси",
    HIST_W: "всемирная история",
    ART: "творческий экзамен",

    AVIA: "авиация",
    VET: "ветеринария",
    WAR: "военное дело",
    DESIGN: "дизайн",
    JOURN: "журналистика",
    ENGIN: "инженерия",
    IT: "информационные технологии",
    HIST: "история",
    FOREST: "лесное хозяйство",
    LINGO: "лингвистика",
    MED: "медицина",
    INT_COM: "международные отношения",
    MUSIC: "музыка",
    TEACH: "преподавание",
    PSY: "психология",
    COM: "связь",
    AGRI: "сельское хозяйство",
    SS: "социальные науки",
    THEO: "теология",
    TECHN: "техника",
    TECHNL: "технология",
    TOURISM: "туризм",
    PHYS_CULT: "физическая культура",
    ECON: "экономика",
    LAW: "юридическое дело"
}


class HollandTest:
    questions = [
        ["инженер-техник", "инженер-контроллер"],
        ["вязальщик", "санитарный врач"],
        ["повар", "наборщик"],
        ["фотограф", "заведующий магазином"],
        ["чертежник", "дизайнер"],

        ["философ", "психиатр"],
        ["ученый-химик", "бухгалтер"],
        ["редактор научного журнала", "адвокат"],
        ["лингвист", "переводчик художественной литературы"],
        ["педиатр", "статистик"],

        ["организатор воспитательной работы", "председатель профсоюза"],
        ["спортивный врач", "фельетонист"],
        ["нотариус", "снабженец"],
        ["токарь", "карикатурист"],
        ["политический деятель", "писатель"],

        ["садовник", "метеоролог"],
        ["водитель", "медсестра"],
        ["инженер-электрик", "секретарь"],
        ["маляр", "художник"],
        ["биолог", "главный врач"],

        ["телеоператор", "режиссер"],
        ["гидролог", "ревизор"],
        ["зоолог", "зоотехник"],
        ["математик", "архитектор"],
        ["инспектор по делам несовершеннолетних", "счетовод"],

        ["учитель", "милиционер"],
        ["воспитатель", "художник"],
        ["экономист", "заведующий отделом"],
        ["корректор", "критик"],
        ["завхоз", "директор"],

        ["радиоинженер", "специалист по ядерной физике"],
        ["водопроводчик", "наборщик"],
        ["агроном", "председатель кооператива"],
        ["модельер", "декоратор"],
        ["археолог", "эксперт"],

        ["работник музея", "консультант"],
        ["ученый", "актер"],
        ["логопед", "наборщик"],
        ["врач", "дипломат"],
        ["главных бухгалтер", "директор"],

        ["поэт", "психолог"],
        ["архивариус", "скульптор"]
    ]
    __test_keys = {
        "realistic": [
            questions[0][0],
            questions[1][0],
            questions[2][0],
            questions[3][0],
            questions[4][0],

            questions[15][0],
            questions[16][0],
            questions[17][0],
            questions[18][0],
            questions[20][0],

            questions[30][0],
            questions[31][0],
            questions[32][0],
            questions[33][0]
        ],
        "intellectual": [
            questions[0][1],
            questions[5][0],
            questions[6][0],
            questions[7][0],
            questions[8][0],

            questions[15][1],
            questions[19][0],
            questions[21][1],
            questions[22][0],
            questions[23][0],

            questions[30][1],
            questions[34][0],
            questions[35][0],
            questions[36][0]
        ],
        "social": [
            questions[1][1],
            questions[5][1],
            questions[9][0],
            questions[10][0],
            questions[11][0],

            questions[16][1],
            questions[28][1],
            questions[24][0],
            questions[25][0],
            questions[26][0],

            questions[35][1],
            questions[37][0],
            questions[38][0],
            questions[40][1]
        ],
        "conventional": [
            questions[2][1],
            questions[6][1],
            questions[9][1],
            questions[12][0],
            questions[13][0],

            questions[17][1],
            questions[21][1],
            questions[25][1],
            questions[27][0],
            questions[28][0],

            questions[31][1],
            questions[37][1],
            questions[39][0],
            questions[41][0]
        ],
        "financial": [
            questions[3][1],
            questions[7][1],
            questions[10][1],
            questions[12][1],
            questions[14][0],

            questions[22][1],
            questions[27][1],
            questions[29][0],
            questions[32][1],
            questions[34][1],

            questions[36][1],
            questions[38][1],
            questions[39][1]
        ],
        "artistic": [
            questions[4][1],
            questions[8][1],
            questions[11][1],
            questions[13][1],
            questions[14][1],

            questions[18][1],
            questions[20][1],
            questions[23][0],
            questions[26][1],
            questions[28][1],

            questions[29][1],
            questions[33][1],
            questions[40][0],
            questions[41][1]
        ]
    }

    __description = {
        "realistic": [
            TECHN, AGRI, WAR, AVIA, ENGIN, GEO, VET, FOREST, COM, TECHNL, PHYS_CULT
        ],
        "intellectual": [
            MATH, PHYSICS, BIO, IT, CHEM
        ],
        "social": [
            TEACH, SS, PSY, ART, TOURISM
        ],
        "conventional": [
            TEACH, MED, SS, PSY, LINGO, THEO
        ],
        "financial": [
            ECON, MATH, JOURN, INT_COM, LAW
        ],
        "artistic": [
            ART, HIST, DESIGN, MUSIC
        ]
    }

    def get_result(self, user_input):
        result = {key: 0 for key in self.__test_keys.keys()}

        for u_in in user_input:
            for key, values in self.__test_keys.items():
                if u_in in values:
                    result[key] += 1

        user_type = max(result, key=result.get)
        return user_type, self.__description[user_type]


class SubjectsProfilesConverter:
    subject = {
        PHYSICS, MATH, CHEM, BIO, SOC_SCI, FOREIGN, GEO, HIST_BEL, HIST_W, ART
    }

    profiles = {AVIA, BIO, VET, WAR,
                GEO, DESIGN, JOURN, ENGIN,
                IT, ART, HIST, FOREST,
                LINGO, MATH, MED, INT_COM,
                MUSIC, TEACH, PSY, COM,
                AGRI, SS, THEO, TECHN,
                TECHNL, TOURISM, PHYSICS, PHYS_CULT,
                CHEM, ECON, LAW}

    __corresponding_table = {
        PHYSICS: [AVIA, WAR, ENGIN, IT, COM, TECHN, TECHNL, TEACH, MATH],
        MATH: [ENGIN, IT, TEACH],
        CHEM: [BIO, VET, FOREST, MED, TEACH, TECHNL],
        BIO: [VET, AGRI, CHEM],
        SOC_SCI: [DESIGN, HIST, LINGO, PSY, SS, THEO, LAW],
        FOREIGN: [LINGO, TEACH, INT_COM, SS],
        GEO: [],
        HIST_BEL: [HIST, TEACH],
        HIST_W: [HIST, TEACH],
        ART: [DESIGN, ART, MUSIC],

        AVIA: [PHYSICS, MATH],
        VET: [BIO, CHEM],
        WAR: [PHYSICS, MATH, SOC_SCI, HIST_BEL],
        DESIGN: [SOC_SCI, HIST_BEL, ART],
        JOURN: [SOC_SCI, FOREIGN, HIST_BEL],
        ENGIN: [MATH, PHYSICS],
        IT: [PHYSICS, MATH, FOREIGN],
        HIST: [HIST_BEL, HIST_W],
        FOREST: [CHEM, MATH],
        LINGO: [FOREIGN, SOC_SCI, HIST_BEL],
        MED: [BIO, CHEM],
        INT_COM: [FOREIGN, SOC_SCI, HIST_BEL],
        MUSIC: [ART],
        TEACH: [PHYSICS, MATH, CHEM, BIO, SOC_SCI, FOREIGN, HIST_BEL],
        PSY: [SOC_SCI, HIST_BEL],
        COM: [MATH, PHYSICS],
        AGRI: [BIO, CHEM, MATH],
        SS: [SOC_SCI, HIST_BEL],
        THEO: [SOC_SCI, HIST_BEL],
        TECHN: [MATH, PHYSICS],
        TECHNL: [MATH, PHYSICS, CHEM],
        TOURISM: [SOC_SCI, BIO],
        PHYS_CULT: [BIO, SOC_SCI],
        ECON: [MATH, FOREIGN],
        LAW: [SOC_SCI, HIST_BEL]
    }

    def to_subjects(self, profiles):
        result = dict()

        for profile in profiles:
            result[profile] = set(self.__corresponding_table[profile])

        return result

    def to_profiles(self, subjects):
        result = dict()

        for subject in subjects:
            profs = set(self.__corresponding_table[subject])
            result[subject] = profs

        return result

    def to_russian(self, dct):
        result = dict()

        for key, values in dct.items():
            k = R_TRANS[key]
            vals = [R_TRANS[v] for v in values]

            result[k] = vals

        return result


class AdviseController:
    advisor = Advise()

    @staticmethod
    def render_page(request, *args, **kwargs):
        pass

    def advise_he(self, request, *args, **kwargs):
        pass


class TestController(AdviseController):
    holland_test = HollandTest()
    answers = []
    passed_questions = -1
    profiles = None

    spc = SubjectsProfilesConverter()

    @staticmethod
    def reset():
        TestController.answers = []
        TestController.passed_questions = -1
        TestController.profiles = None

    @staticmethod
    def render_preamble(request, *args, **kwargs):
        TestController.reset()

        return render(request,
                      os.path.join('preamble.html'),
                      {})

    @staticmethod
    def render_page(request, *args, **kwargs):

        if TestController.passed_questions == 41:
            # TestController.reset()
            return TestController.get_test_result(request, args, kwargs)

        answer = request.POST.get('preferred') or None

        TestController.answers.append(answer)
        TestController.passed_questions += 1

        opt1 = TestController.holland_test.questions[TestController.passed_questions][0]
        opt2 = TestController.holland_test.questions[TestController.passed_questions][1]

        return render(request,
                      os.path.join('prof_test_page.html'),
                      {
                          "opt1": opt1,
                          "opt2": opt2,
                          "passed": TestController.passed_questions + 1
                      })

    @staticmethod
    def get_test_result(request, *args, **kwargs):
        ans = TestController.answers[1:]

        user_type, profiles_en = TestController.holland_test.get_result(ans)
        TestController.profiles = profiles_en

        profiles = [R_TRANS[pr] for pr in profiles_en]

        return render(request,
                      os.path.join('test_result_page.html'),
                      {"result": user_type,
                       "profiles": profiles})

    def choose_city_dormitory(self, request, *args, **kwargs):
        return render(request,
                      os.path.join('dorm_city.html'),
                      {})

    def advise_he(self, request, *args, **kwargs):
        preferred = self.profiles

        context = {profile: [(1 if profile in preferred else None)] for profile in self.spc.profiles}
        context.update({"region": request.POST.get('region'),
                        "dormitory": request.POST.get('dormitory')})

        accuracy, result = self.advisor.advise(context)

        return render(request,
                      os.path.join('advise_result.html'),
                      {"accuracy": accuracy,
                       "he": result})


class SubjectController(AdviseController):
    spc = SubjectsProfilesConverter()

    @staticmethod
    def render_page(request, *args, **kwargs):
        return render(request,
                      os.path.join('subjects_page.html'),
                      {})

    def advise_he(self, request, *args, **kwargs):
        preferred = request.POST.getlist('preferred')

        preferred = self.spc.to_profiles(preferred)

        context = {profile: [(1 if profile in preferred else None)] for profile in self.spc.profiles}
        context.update({"region": request.POST.get('region'),
                        "dormitory": request.POST.get('dormitory')})

        accuracy, result = self.advisor.advise(context)

        return render(request,
                      os.path.join('advise_result.html'),
                      {"accuracy": accuracy,
                       "he": result})


class ProfileController(AdviseController):
    spc = SubjectsProfilesConverter()

    @staticmethod
    def render_page(request, *args, **kwargs):
        return render(request,
                      os.path.join('profiles_page.html'),
                      {})

    @staticmethod
    def convert(request, *args, **kwargs):
        subj = request.POST.getlist('subj') or []
        profs = request.POST.getlist('profs') or []

        subj_to_profs_en = ProfileController.spc.to_profiles(subj)
        profs_to_subj_en = ProfileController.spc.to_subjects(profs)

        subj_to_profs = ProfileController.spc.to_russian(subj_to_profs_en)
        profs_to_subj = ProfileController.spc.to_russian(profs_to_subj_en)

        ProfileController.join_list(subj_to_profs)
        ProfileController.join_list(profs_to_subj)

        return render(request,
                      os.path.join('convertion.html'),
                      {
                          "stp": subj_to_profs,
                          "pts": profs_to_subj}
                      )

    def advise_he(self, request, *args, **kwargs):
        preferred = request.POST.getlist('preferred')

        context = {profile: [(1 if profile in preferred else None)] for profile in self.spc.profiles}
        context.update({"region": request.POST.get('region'),
                        "dormitory": request.POST.get('dormitory')})

        accuracy, result = self.advisor.advise(context)

        return render(request,
                      os.path.join('advise_result.html'),
                      {"accuracy": accuracy,
                       "he": result})

    @staticmethod
    def join_list(dct):
        for key, values in dct.items():
            dct[key] = ",\n".join(values)


class HomeController:
    tc = TestController()
    sc = SubjectController()
    pc = ProfileController()

    @staticmethod
    def render_page(request, *args, **kwargs):
        return render(request,
                      os.path.join('home_page.html'),
                      {})

    def pass_test(self, request, *args, **kwargs):
        # HomeController.tc.reset()
        return self.tc.render_page(request,
                                   *args,
                                   **kwargs)

    def select_profiles(self, request, *args, **kwargs):
        return self.sc.render_page(request,
                                   *args,
                                   **kwargs)

    def select_subjects(self, request, *args, **kwargs):
        return self.pc.render_page(request,
                                   *args,
                                   **kwargs)


class SubjectsProfilesController:
    converter = SubjectsProfilesConverter()

    @staticmethod
    def render_page(request, *args, **kwargs):
        return render(request,
                      os.path.join("profiles_subjects_page.html"),
                      {})

    def accord(self, request, *args, **kwargs):
        return render(request,
                      os.path.join("profiles_subjects_page.html"),
                      {})
