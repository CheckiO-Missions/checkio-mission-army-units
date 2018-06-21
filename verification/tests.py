init_code = """
if not "Army" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Army'?")

Army = USER_GLOBAL['Army']

if not "AsianArmy" in USER_GLOBAL:
    raise NotImplementedError("Where is 'AsianArmy'?")

AsianArmy = USER_GLOBAL['AsianArmy']

if not "EuropeanArmy" in USER_GLOBAL:
    raise NotImplementedError("Where is 'EuropeanArmy'?")

EuropeanArmy = USER_GLOBAL['EuropeanArmy']

if not "Swordsman" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Swordsman'?")

Swordsman = USER_GLOBAL['Swordsman']

if not "Lancer" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Lancer'?")

Lancer = USER_GLOBAL['Lancer']

if not "Archer" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Archer'?")

Archer = USER_GLOBAL['Archer']

if not issubclass(AsianArmy, Army):
    raise Warning("AsianArmy should be the subclass of the Army")

if not issubclass(EuropeanArmy, Army):
    raise Warning("EuropeanArmy should be the subclass of the Army")
"""

run_test = """
RET['code_result'] = {}
"""

def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}


TESTS = {
    "1. My army": [
        prepare_test(middle_code='''my_army = EuropeanArmy()
soldier_1 = my_army.train_swordsman("David")''',
                     test="soldier_1.introduce()",
                     answer="Knight David, European swordsman")
        ],
    "2. My army": [
        prepare_test(middle_code='''my_army = EuropeanArmy()
soldier_2 = my_army.train_lancer("Nicklaus")''',
                     test="soldier_2.introduce()",
                     answer="Raubritter Nicklaus, European lancer")
        ],
    "3. My army": [
        prepare_test(middle_code='''my_army = EuropeanArmy()
soldier_3 = my_army.train_archer("Beleron")''',
                     test="soldier_3.introduce()",
                     answer="Ranger Beleron, European archer")
        ],
    "4. My army": [
        prepare_test(middle_code='''my_army = AsianArmy()
soldier_4 = my_army.train_swordsman("Han")''',
                     test="soldier_4.introduce()",
                     answer="Samurai Han, Asian swordsman")
        ],
    "5. My army": [
        prepare_test(middle_code='''my_army = AsianArmy()
soldier_5 = my_army.train_lancer("Ayanami")''',
                     test="soldier_5.introduce()",
                     answer="Ronin Ayanami, Asian lancer")
        ],
    "6. My army": [
        prepare_test(middle_code='''my_army = AsianArmy()
soldier_6 = my_army.train_archer("Kitsune")''',
                     test="soldier_6.introduce()",
                     answer="Shinobi Kitsune, Asian archer")
        ],
    "7. My army": [
        prepare_test(middle_code='''my_army = EuropeanArmy()
soldier_7 = my_army.train_swordsman("Blake")''',
                     test="soldier_7.introduce()",
                     answer="Knight Blake, European swordsman")
        ],
    "8. My army": [
        prepare_test(middle_code='''my_army = EuropeanArmy()
soldier_8 = my_army.train_lancer("Howard")''',
                     test="soldier_8.introduce()",
                     answer="Raubritter Howard, European lancer")
        ],
    "9. My army": [
        prepare_test(middle_code='''my_army = EuropeanArmy()
soldier_9 = my_army.train_archer("Alice")''',
                     test="soldier_9.introduce()",
                     answer="Ranger Alice, European archer")
        ],
    "10. My army": [
        prepare_test(middle_code='''my_army = AsianArmy()
soldier_10 = my_army.train_swordsman("Miyagi")''',
                     test="soldier_10.introduce()",
                     answer="Samurai Miyagi, Asian swordsman")
        ],
    "11. My army": [
        prepare_test(middle_code='''my_army = AsianArmy()
soldier_11 = my_army.train_lancer("Misa")''',
                     test="soldier_11.introduce()",
                     answer="Ronin Misa, Asian lancer")
        ],
    "12. My army": [
        prepare_test(middle_code='''my_army = AsianArmy()
soldier_12 = my_army.train_archer("Heroki")''',
                     test="soldier_12.introduce()",
                     answer="Shinobi Heroki, Asian archer")
        ]
}
