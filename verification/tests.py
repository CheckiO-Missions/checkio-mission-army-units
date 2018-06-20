init_code = """
if not "AbstractArmy" in USER_GLOBAL:
    raise NotImplementedError("Where is 'AbstractArmy'?")

AbstractArmy = USER_GLOBAL['AbstractArmy']

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
my_army.add_swordsman("Jaks")
my_army.add_swordsman("Brin")
my_army.add_lancer("Harold")
my_army.add_archer("Robin")
my_army.add_archer("May")''',
                     test="my_army.show_army()",
                     answer={"Knights": 2, "Raubritters": 1, "Rangers": 2, "Total": 5})
        ],
    "2. My army": [
        prepare_test(middle_code='''my_army = EuropeanArmy()
my_army.add_swordsman("Jaks")
my_army.add_swordsman("Brin")
my_army.add_lancer("Harold")
my_army.add_archer("Robin")
my_army.add_archer("May")''',
                     test="my_army.show_swordsmans()",
                     answer=["Knight Jaks", "Knight Brin"])
        ],
    "3. My army": [
        prepare_test(middle_code='''my_army = EuropeanArmy()
my_army.add_swordsman("Jaks")
my_army.add_swordsman("Brin")
my_army.add_lancer("Harold")
my_army.add_archer("Robin")
my_army.add_archer("May")''',
                     test="my_army.show_lancers()",
                     answer=["Raubritter Harold"])
        ],
    "4. My army": [
        prepare_test(middle_code='''my_army = EuropeanArmy()
my_army.add_swordsman("Jaks")
my_army.add_swordsman("Brin")
my_army.add_lancer("Harold")
my_army.add_archer("Robin")
my_army.add_archer("May")''',
                     test="my_army.show_archers()",
                     answer=["Ranger Robin", "Ranger May"])
        ]
}
