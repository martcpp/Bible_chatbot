from meta_ai_api import MetaAI

ai = MetaAI()


def bible_verse(verse):
    explanation_text = f" in a layman understanding explain \"{
        verse}\" not more than 250 characters"
    prayer_text = f"give a prayer point that fit the this bible verse {
        verse}not more than 250 characters"
    explanation = ai.prompt(message=explanation_text)
    prayer_point = ai.prompt(message=prayer_text)
    if explanation is not None and prayer_point is not None:
        explen = len(explanation_text)
        praylen = len(prayer_text)
        print(f"explanation length:{explen} praylen:{praylen}")
    print(explanation['message'])
    print("-----------------------------------")
    print(prayer_point['message'])
    return explanation['message'], prayer_point['message']


'''
if __name__ == "__main__":
    verse = "The Lord is far from the wicked, but he hears the prayer of the righteous."
    explanation, prayer_point = bible_verse(verse)
    print(explanation)
    print("-----------------------------------")
    print(prayer_point)





respons = ai.prompt(message=" in a layman understanding explain in pidgin \"The Lord is far from the wicked, but he hears the prayer of the righteous.\" not more than 250 characters")
pray= ai.prompt(message="give a prayer point in pidgin that fit the this bible verse The Lord is far from the wicked, but he hears the prayer of the righteous. not more than 250 characters don't translate and dont explain the terms of the pidgin")
print(response['message'])
print("-----------------------------------")
print(prayer['message'])
print("-----------------------------------")
print(pray['message'])
print("-----------------------------------")
print(respons['message'])
 
 '''
