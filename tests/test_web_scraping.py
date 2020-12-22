from web_scraping.scraper import *




def test_count():
    call = count = get_citations_needed_count()
    assert call == 2


def test_report():
    call = get_citations_needed_report()
    assert call == "ALL PARTS THAT NEED CITATION:"

'1. In the complete edition of Dostoevsky\'s writings published in the Soviet Union, the editors reassembled the writer\'s notebooks for Crime and Punishment in a sequence roughly corresponding to the various stages of composition.[citation needed] As a result, there exists a fragmentary working draft of the novella, as initially conceived, as well as two other versions of the text. These have been distinguished as the Wiesbaden edition, the Petersburg edition, and the final plan, involving the shift from a first-person narrator to Dostoevsky’ innovative use of third-person narrative to achieve first-person narrative perspectives.[14] Dostoevsky initially considered four first-person plans: a memoir written by Raskolnikov, his confession recorded eight days after the murder, his diary begun five days after the murder, and a mixed form in which the first half was in the form of a memoir, and the second half in the form of a diary.[15] The Wiesbaden edition concentrates entirely on the moral and psychological reactions of the narrator after the murder. It coincides roughly with the story that Dostoevsky described in his letter to Katkov and, written in the form of a diary or journal, corresponds to what eventually became part 2 of the finished work.[16]'

'2. The title refers to Italian criminologist and philosopher Cesare Beccaria\'s "Dei delitti e delle pene" (On Crimes and Punishment, 1764), a text known in Russia due to an 1803 translation.[citation needed]'

'None'