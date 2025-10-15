import pytest 
from .test_pipeline import nlp


@pytest.mark.parametrize('test_ecog_entities_input, test_ecog_entities_ent_lab, entity_label',
                         [('55f ecog4', 'ecog4', 'ECOG_STATUS'),
                          ('Addit: ECOG=3', 'ECOG=3', 'ECOG_STATUS'),
                          ('ecog ps 2', 'ecog ps 2', 'ECOG_STATUS'),
                          ('ECOG performance status: 0\nbloodwork done', 'ECOG performance status: 0', 'ECOG_STATUS'),
                          ('(ecog 0-1)', 'ecog 0-1', 'ECOG_STATUS'),
                          ('o/e ECOG 2, seems well', 'ECOG 2', 'ECOG_STATUS'),
                          ('ecog was 4 now 3', 'ecog was 4 now 3', 'ECOG_STATUS'),
                          ('ecog between 3 and 4', 'ecog between 3 and 4', 'ECOG_STATUS'),
                          ('ecog ~3', 'ecog ~3', 'ECOG_STATUS'),
                          ('ecog ?4', 'ecog ?4', 'ECOG_STATUS'),
                          ('ecog still at 2', 'ecog still at 2', 'ECOG_STATUS'),
                          ('ecog currently 3', 'ecog currently 3', 'ECOG_STATUS'),
                          ('ECOG PS 2-3', 'ECOG PS 2-3', 'ECOG_STATUS'),
                          ('ECOG 3/4', 'ECOG 3/4', 'ECOG_STATUS'),
                          ('ECOG1-2', 'ECOG1-2', 'ECOG_STATUS'),
                          ('ECOG zero', 'ECOG zero', 'ECOG_STATUS'),
                          ('ecog 3.', 'ecog 3', 'ECOG_STATUS'),
                          ('ecog is 4', 'ecog is 4', 'ECOG_STATUS'),
                          ('blood   marker stable, lfts ok, ct   , ecog =2', 'ecog =2', 'ECOG_STATUS'),
                          ('On examination he was well looking and of ECOG performance status 0', 'ECOG performance status 0', 'ECOG_STATUS'),
                          ('Appears well and has a performance status of zero', 'performance status of zero', 'ECOG_STATUS'),
                          ('O/E ECOG 0', 'ECOG 0', 'ECOG_STATUS'),
                          ('Well Remains ECOG 0', 'ECOG 0', 'ECOG_STATUS'),
                          ('…woman of ECOG 0 performance status.', 'ECOG 0', 'ECOG_STATUS'),
                          ('His ECOG performance status is zero.', 'ECOG performance status is zero', 'ECOG_STATUS'),
                          ('She has an ECOG performance status of 0.', 'ECOG performance status of 0', 'ECOG_STATUS'),
                          ('ECOG performance status 3', 'ECOG performance status 3', 'ECOG_STATUS'),
                          ('ECOG - 1', 'ECOG - 1', 'ECOG_STATUS'),
                          ('History: ECOG 2-3', 'ECOG 2-3', 'ECOG_STATUS'),
                          ('ECOG now 3-4', 'ECOG now 3-4', 'ECOG_STATUS'),
                          ('ECOG now 3 to 4', 'ECOG now 3 to 4', 'ECOG_STATUS'),
                          ('ECOG Performance status 1', 'ECOG Performance status 1', 'ECOG_STATUS'),
                          ('ECOG PS 1.', 'ECOG PS 1', 'ECOG_STATUS'),
                          ('ECOG 3+', 'ECOG 3', 'ECOG_STATUS'),
                          ('(ECOG 1)', 'ECOG 1', 'ECOG_STATUS'),
                          ('ECOG status is 2', 'ECOG status is 2', 'ECOG_STATUS'),
                          ('ECOG ~1', 'ECOG ~1', 'ECOG_STATUS'),
                          ('ECOG1/2', 'ECOG1/2', 'ECOG_STATUS'),
                          ('Poor PS-ECOG 3 (due to comorbidities)', 'ECOG 3', 'ECOG_STATUS'),
                          ('Note ECOG now 0', 'ECOG now 0', 'ECOG_STATUS'),
                          ('ECOG ?0', 'ECOG ?0', 'ECOG_STATUS'),
                          ('ECOG0-1-very active', 'ECOG0-1', 'ECOG_STATUS'),
                          ('Likely ECOG 0', 'ECOG 0', 'ECOG_STATUS'),
                          ('ECOG PS 1.', 'ECOG PS 1', 'ECOG_STATUS'),
                          ('Pt reviewed with partner, ECOG PS 2', 'ECOG PS 2', 'ECOG_STATUS'),
                          ('Unlimited ET, ECOG - 0', 'ECOG - 0', 'ECOG_STATUS'),
                          ('EtOH, ECOG1', 'ECOG1', 'ECOG_STATUS'),
                          ('Social history ECOG 2', 'ECOG 2', 'ECOG_STATUS'),
                          ('NKDA, SH – ECOG 0', 'ECOG 0', 'ECOG_STATUS'),
                          ('Change in taste, ECOG 0', 'ECOG 0', 'ECOG_STATUS'),
                          ('Independent with personal and instrumental ADLs, ECOG 0', 'ECOG 0', 'ECOG_STATUS'),
                          ('OE: ECOG 0', 'ECOG 0', 'ECOG_STATUS'),
                          ('Urine MCS - RCC normal, WCC 10-100. Culure NEG. \nECOG 1', 'ECOG 1', 'ECOG_STATUS'),
                          ('OE, ECOG 1', 'ECOG 1', 'ECOG_STATUS'),
                          ('Doing light house work\nECOG 1', 'ECOG 1', 'ECOG_STATUS'),
                          ('OE, ECOG 1', 'ECOG 1', 'ECOG_STATUS'),
                          ('O/E: ECOG 0', 'ECOG 0', 'ECOG_STATUS'),
                          ('tires at shopping. son doing cleaning\nECOG 3', 'ECOG 3', 'ECOG_STATUS'),
                          ('applying to Centrelink.\nECOG = 1', 'ECOG = 1', 'ECOG_STATUS'),
                          ('OE: ECOG=0', 'ECOG=0', 'ECOG_STATUS'),
                          ('Impression:\nECOG 0', 'ECOG 0', 'ECOG_STATUS'),
                          ('current performance status of ECOG 3', 'ECOG 3', 'ECOG_STATUS'),
                          ('Remains very active and working full time\nECOG 0', 'ECOG 0', 'ECOG_STATUS'),
                          ('86M ECOG 3', 'ECOG 3', 'ECOG_STATUS'),])
def test_ecog_entities(test_ecog_entities_input, test_ecog_entities_ent_lab, entity_label):
    doc = nlp(test_ecog_entities_input)
    assert 'ECOG_STATUS' in [e.label_ for e in doc.ents], 'entity test case failure: test_ecog_entities, ECOG_STATUS'
    assert test_ecog_entities_ent_lab in [e.text for e in doc.ents], 'entity test case failure: test_ecog_entities, ECOG_STATUS'


# test known valid dates
@pytest.mark.parametrize(
    'text,tokens',
    [('test done Jan 1st 2020', ['Jan 1st 2020']),
     ('test done Oct 1 1993 blah', ['Oct 1 1993']),
     ('blah blah 1/2/2020 /sdlkf ', ['1/2/2020']),
     ('return 3/12 for followup', ['3/12']),
     ('03/03/02: diagnosis ', ['03/03/02']),
     ('(something February 2020)', ['February 2020']),
     ('(1) Progression Mar 2016', ['Mar 2016']),
     ('1998-02-01 cool people write dates like this', ['1998-02-01']),]
)
def test_date_entities(text, tokens):
    doc = nlp.tokenizer(text)
    dates = [t for t in doc if t._.date]
    assert len(dates) == len(tokens)
    assert [t.text for t in dates] == tokens


# tests strings that might look like dates that shouldn't be
@pytest.mark.parametrize(
    'text,tokens',
    [('EUC 140/3', []),
     ]
)
def test_negative_date_entities(text, tokens):
    doc = nlp.tokenizer(text)
    dates = [t for t in doc if t._.date]
    assert len(dates) == len(tokens)
    assert [t.text for t in dates] == tokens
    
