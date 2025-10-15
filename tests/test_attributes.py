import pytest 
from .test_pipeline import nlp


@pytest.mark.parametrize('test_ecog_entities_input, test_ecog_entities_attr_lab, attribute_label',
                         [('55f ecog4', ['ecog4'], 'ecog_status'),
                          ('Addit: ECOG=3', ['ECOG=3'], 'ecog_status'),
                          ('ecog ps 2', ['ecog ps 2'], 'ecog_status'),
                          ('ECOG performance status: 0\nbloodwork done', ['ECOG performance status: 0'], 'ecog_status'),
                          ('(ecog 0-1)', ['ecog 0-1'], 'ecog_status'),
                          ('o/e ECOG 2, seems well', ['ECOG 2'], 'ecog_status'),
                          ('ecog was 4 now 3', ['ecog was 4 now 3'], 'ecog_status'),
                          ('ecog between 3 and 4', ['ecog between 3 and 4'], 'ecog_status'),
                          ('ecog ~3', ['ecog ~3'], 'ecog_status'),
                          ('ecog ?4', ['ecog ?4'], 'ecog_status'),
                          ('ecog still at 2', ['ecog still at 2'], 'ecog_status'),
                          ('ecog currently 3', ['ecog currently 3'], 'ecog_status'),
                          ('ECOG PS 2-3', ['ECOG PS 2-3'], 'ecog_status'),
                          ('ECOG 3/4', ['ECOG 3/4'], 'ecog_status'),
                          ('ECOG1-2', ['ECOG1-2'], 'ecog_status'),
                          ('ECOG zero', ['ECOG zero'], 'ecog_status'),
                          ('ecog 3.', ['ecog 3'], 'ecog_status'),
                          ('ecog is 4', ['ecog is 4'], 'ecog_status'),
                          ('blood   marker stable, lfts ok, ct   , ecog =2', ['ecog =2'], 'ecog_status'),
                          ('On examination he was well looking and of ECOG performance status 0', ['ECOG performance status 0'], 'ecog_status'),
                          ('Appears well and has a performance status of zero', ['performance status of zero'], 'ecog_status'),
                          ('O/E ECOG 0', ['ECOG 0'], 'ecog_status'),
                          ('Well Remains ECOG 0', ['ECOG 0'], 'ecog_status'),
                          ('…woman of ECOG 0 performance status.', ['ECOG 0'], 'ecog_status'),
                          ('His ECOG performance status is zero.', ['ECOG performance status is zero'], 'ecog_status'),
                          ('She has an ECOG performance status of 0.', ['ECOG performance status of 0'], 'ecog_status'),
                          ('ECOG performance status 3', ['ECOG performance status 3'], 'ecog_status'),
                          ('ECOG - 1', ['ECOG - 1'], 'ecog_status'),
                          ('History: ECOG 2-3', ['ECOG 2-3'], 'ecog_status'),
                          ('ECOG now 3-4', ['ECOG now 3-4'], 'ecog_status'),
                          ('ECOG now 3 to 4', ['ECOG now 3 to 4'], 'ecog_status'),
                          ('ECOG Performance status 1', ['ECOG Performance status 1'], 'ecog_status'),
                          ('ECOG PS 1.', ['ECOG PS 1'], 'ecog_status'),
                          ('ECOG 3+', ['ECOG 3'], 'ecog_status'),
                          ('(ECOG 1)', ['ECOG 1'], 'ecog_status'),
                          ('ECOG status is 2', ['ECOG status is 2'], 'ecog_status'),
                          ('ECOG ~1', ['ECOG ~1'], 'ecog_status'),
                          ('ECOG1/2', ['ECOG1/2'], 'ecog_status'),
                          ('Poor PS-ECOG 3 (due to comorbidities)', ['ECOG 3'], 'ecog_status'),
                          ('Note ECOG now 0', ['ECOG now 0'], 'ecog_status'),
                          ('ECOG ?0', ['ECOG ?0'], 'ecog_status'),
                          ('ECOG0-1-very active', ['ECOG0-1'], 'ecog_status'),
                          ('Likely ECOG 0', ['ECOG 0'], 'ecog_status'),
                          ('ECOG PS 1.', ['ECOG PS 1'], 'ecog_status'),
                          ('Pt reviewed with partner, ECOG PS 2', ['ECOG PS 2'], 'ecog_status'),
                          ('Unlimited ET, ECOG - 0', ['ECOG - 0'], 'ecog_status'),
                          ('EtOH, ECOG1', ['ECOG1'], 'ecog_status'),
                          ('Social history ECOG 2', ['ECOG 2'], 'ecog_status'),
                          ('NKDA, SH – ECOG 0', ['ECOG 0'], 'ecog_status'),
                          ('Change in taste, ECOG 0', ['ECOG 0'], 'ecog_status'),
                          ('Independent with personal and instrumental ADLs, ECOG 0', ['ECOG 0'], 'ecog_status'),
                          ('OE: ECOG 0', ['ECOG 0'], 'ecog_status'),
                          ('Urine MCS - RCC normal, WCC 10-100. Culure NEG. \nECOG 1', ['ECOG 1'], 'ecog_status'),
                          ('OE, ECOG 1', ['ECOG 1'], 'ecog_status'),
                          ('Doing light house work\nECOG 1', ['ECOG 1'], 'ecog_status'),
                          ('OE, ECOG 1', ['ECOG 1'], 'ecog_status'),
                          ('O/E: ECOG 0', ['ECOG 0'], 'ecog_status'),
                          ('tires at shopping. son doing cleaning\nECOG 3', ['ECOG 3'], 'ecog_status'),
                          ('applying to Centrelink.\nECOG = 1', ['ECOG = 1'], 'ecog_status'),
                          ('OE: ECOG=0', ['ECOG=0'], 'ecog_status'),
                          ('Impression:\nECOG 0', ['ECOG 0'], 'ecog_status'),
                          ('current performance status of ECOG 3', ['ECOG 3'], 'ecog_status'),
                          ('Remains very active and working full time\nECOG 0', ['ECOG 0'], 'ecog_status'),
                          ('86M ECOG 3', ['ECOG 3'], 'ecog_status'),
                          ('ECOG 1/5', ['ECOG 1/5'], 'ecog_status'),
                          ('performance score 2.3 months ago…', ['performance score 2'], 'ecog_status'),])
def test_ecog_entities(test_ecog_entities_input, test_ecog_entities_attr_lab, attribute_label):
    doc = nlp(test_ecog_entities_input)
    attrs = [t.text for t in doc if t._.ecog_status]
    assert attrs == test_ecog_entities_attr_lab, 'attribute test case failure: test_case, ecog_status'


@pytest.mark.parametrize('test_ecog_values_input, test_ecog_values_attr_lab, attribute_label',
                         [('55f ecog4', ['4'], 'ecog_status_value'),
                          ('Addit: ECOG=3', ['3'], 'ecog_status_value'),
                          ('ecog ps 2', ['2'], 'ecog_status_value'),
                          ('ECOG performance status: 0\nbloodwork done', ['0'], 'ecog_status_value'),
                          ('(ecog 0-1)', ['1'], 'ecog_status_value'),
                          ('o/e ECOG 2', ['2'], 'ecog_status_value'),
                          ('ecog between 3 and 4', ['4'], 'ecog_status_value'),
                          ('ecog ?4', ['4'], 'ecog_status_value'),
                          ('ecog still at 2', ['2'], 'ecog_status_value'),
                          ('ecog currently 3', ['3'], 'ecog_status_value'),
                          ('ECOG PS 2-3', ['3'], 'ecog_status_value'),
                          ('ECOG 3/4', ['4'], 'ecog_status_value'),
                          ('ECOG1-2', ['2'], 'ecog_status_value'),
                          ('ECOG zero', ['0'], 'ecog_status_value'),
                          ('ecog 3.', ['3'], 'ecog_status_value'),
                          ('ecog is 4', ['4'], 'ecog_status_value'),
                          ('blood   marker stable, lfts ok, ct   , ecog =2', ['2'], 'ecog_status_value'),
                          ('On examination he was well looking and of ECOG performance status 0', ['0'], 'ecog_status_value'),
                          ('Appears well and has a performance status of zero', ['0'], 'ecog_status_value'),
                          ('O/E ECOG 0', ['0'], 'ecog_status_value'),
                          ('Well Remains ECOG 0', ['0'], 'ecog_status_value'),
                          ('…woman of ECOG 0 performance status.', ['0'], 'ecog_status_value'),
                          ('His ECOG performance status is zero.', ['0'], 'ecog_status_value'),
                          ('She has an ECOG performance status of 0.', ['0'], 'ecog_status_value'),
                          ('ECOG performance status 3', ['3'], 'ecog_status_value'),
                          ('ECOG - 1', ['1'], 'ecog_status_value'),
                          ('History: ECOG 2-3', ['3'], 'ecog_status_value'),
                          ('ECOG now 3-4', ['4'], 'ecog_status_value'),
                          ('ECOG now 3 to 4', ['4'], 'ecog_status_value'),
                          ('ECOG Performance status 1', ['1'], 'ecog_status_value'),
                          ('ECOG PS 1.', ['1'], 'ecog_status_value'),
                          ('ECOG 3+', ['3'], 'ecog_status_value'),
                          ('(ECOG 1)', ['1'], 'ecog_status_value'),
                          ('ECOG status is 2', ['2'], 'ecog_status_value'),
                          ('ECOG ~1', ['1'], 'ecog_status_value'),
                          ('ECOG1/2', ['2'], 'ecog_status_value'),
                          ('Poor PS-ECOG 3 (due to comorbidities)', ['3'], 'ecog_status_value'),
                          ('Note ECOG now 0', ['0'], 'ecog_status_value'),
                          ('ECOG ?0', ['0'], 'ecog_status_value'),
                          ('ECOG0-1-very active', ['1'], 'ecog_status_value'),
                          ('Likely ECOG 0', ['0'], 'ecog_status_value'),
                          ('ECOG PS 1.', ['1'], 'ecog_status_value'),
                          ('Pt reviewed with partner, ECOG PS 2', ['2'], 'ecog_status_value'),
                          ('Unlimited ET, ECOG - 0', ['0'], 'ecog_status_value'),
                          ('EtOH, ECOG1', ['1'], 'ecog_status_value'),
                          ('Social history ECOG 2', ['2'], 'ecog_status_value'),
                          ('NKDA, SH – ECOG 0', ['0'], 'ecog_status_value'),
                          ('Change in taste, ECOG 0', ['0'], 'ecog_status_value'),
                          ('Independent with personal and instrumental ADLs, ECOG 0', ['0'], 'ecog_status_value'),
                          ('OE: ECOG 0', ['0'], 'ecog_status_value'),
                          ('Urine MCS - RCC normal, WCC 10-100. Culure NEG. \nECOG 1', ['1'], 'ecog_status_value'),
                          ('OE, ECOG 1', ['1'], 'ecog_status_value'),
                          ('Doing light house work\nECOG 1', ['1'], 'ecog_status_value'),
                          ('OE, ECOG 1', ['1'], 'ecog_status_value'),
                          ('O/E: ECOG 0', ['0'], 'ecog_status_value'),
                          ('tires at shopping. son doing cleaning\nECOG 3', ['3'], 'ecog_status_value'),
                          ('applying to Centrelink.\nECOG = 1', ['1'], 'ecog_status_value'),
                          ('OE: ECOG=0', ['0'], 'ecog_status_value'),
                          ('Impression:\nECOG 0', ['0'], 'ecog_status_value'),
                          ('current performance status of ECOG 3', ['3'], 'ecog_status_value'),
                          ('Remains very active and working full time\nECOG 0', ['0'], 'ecog_status_value'),
                          ('86M ECOG 3', ['3'], 'ecog_status_value'),
                          ('ECOG 1/5', ['1'], 'ecog_status_value'),
                          ('performance score 2.3 months ago…', ['2'], 'ecog_status_value'),])
def test_ecog_values(test_ecog_values_input, test_ecog_values_attr_lab, attribute_label):
    doc = nlp(test_ecog_values_input)
    attrs = [str(t._.ecog_status_value) for t in doc if t._.ecog_status_value != -1]
    assert attrs == test_ecog_values_attr_lab, 'attribute test case failure: test_case, ecog_status_value'

@pytest.mark.parametrize('test_feeding_tube_entity_input, test_feeding_tube_entity_attr_lab, attribute_label',
                         [('PEG', ['PEG'], 'feeding_tube'),
                          ('I/O PEG', ['I/O PEG'], 'feeding_tube'),
                          ('R/O PEG', ['R/O PEG'], 'feeding_tube'),
                          ('percutaneous endoscopic gastrostomy', ['percutaneous endoscopic gastrostomy'], 'feeding_tube'),
                          ('RIG', ['RIG'], 'feeding_tube'),
                          ('I/O RIG', ['I/O RIG'], 'feeding_tube'),
                          ('R/O RIG', ['R/O RIG'], 'feeding_tube'),
                          ('radiologically inserted gastrostomy', ['radiologically inserted gastrostomy'], 'feeding_tube'),
                          ('radiological inserted gastrostomy', ['radiological inserted gastrostomy'], 'feeding_tube'),
                          ('NGT', ['NGT'], 'feeding_tube'),
                          ('I/O NGT', ['I/O NGT'], 'feeding_tube'),
                          ('R/O NGT', ['R/O NGT'], 'feeding_tube'),
                          ('nasogastric tube', ['nasogastric tube'], 'feeding_tube'),
                          ('g-tube', ['g-tube'], 'feeding_tube'),
                          ('G-tube', ['G-tube'], 'feeding_tube'),
                          ('gastrostomy', ['gastrostomy'], 'feeding_tube'),
                          ('balloon gastrostomy', ['balloon gastrostomy'], 'feeding_tube'),
                          ('surgical gastrostomy', ['surgical gastrostomy'], 'feeding_tube'),
                          ('PEJ', ['PEJ'], 'feeding_tube'),
                          ('jejunostomy', ['jejunostomy'], 'feeding_tube'),])
def test_feeding_tube_entity(test_feeding_tube_entity_input, test_feeding_tube_entity_attr_lab, attribute_label):
    doc = nlp(test_feeding_tube_entity_input)
    attrs = [t.text for t in doc if t._.feeding_tube]
    assert attrs == test_feeding_tube_entity_attr_lab, 'attribute test case failure: test_case, feeding_tube'


@pytest.mark.parametrize('test_negative_ecog_status_input, test_negative_ecog_status_attr_lab, attribute_label',
                         [('karnofsky performance status of 80', [], 'ecog_status'),
                          ('nodal status: 2', [], 'ecog_status'),
                          ('nutrition status 4.', [], 'ecog_status'),
                          ('ECOG 7', [], 'ecog_status'),])
def test_negative_ecog_status(test_negative_ecog_status_input, test_negative_ecog_status_attr_lab, attribute_label):
    doc = nlp(test_negative_ecog_status_input)
    attrs = [t.text for t in doc if t._.ecog_status]
    assert attrs == test_negative_ecog_status_attr_lab, 'attribute test case failure: test_case, ecog_status'


@pytest.mark.parametrize('test_pgsga_entity_input, test_pgsga_entity_attr_lab, attribute_label',
                         [('PG-SGA: C24 (severe malnutrition)', ['PG-SGA: C24'], 'pgsga'),
                          ('PGSGA: C24 (severe malnutrition)', ['PGSGA: C24'], 'pgsga'),
                          ('PG-SGA=A13', ['PG-SGA=A13'], 'pgsga'),
                          ('PGSGA = B/11', ['PGSGA = B/11'], 'pgsga'),
                          ('PG-SGA = B/11', ['PG-SGA = B/11'], 'pgsga'),
                          ('PG-SGA 1A (well-nourished)', ['PG-SGA 1A'], 'pgsga'),
                          ('(PG-SGA=A13)', ['PG-SGA=A13)'], 'pgsga'),
                          ('PG-SGA rating B/21', ['PG-SGA rating B/21'], 'pgsga'),])
def test_pgsga_entity(test_pgsga_entity_input, test_pgsga_entity_attr_lab, attribute_label):
    doc = nlp(test_pgsga_entity_input)
    attrs = [t.text for t in doc if t._.pgsga]
    assert attrs == test_pgsga_entity_attr_lab, 'attribute test case failure: test_case, pgsga'


@pytest.mark.parametrize('test_pgsga_value_input, test_pgsga_value_attr_lab, attribute_label',
                         [('PG-SGA: C24 (severe malnutrition)', ['C24'], 'pgsga_value'),
                          ('PGSGA: C24 (severe malnutrition)', ['C24'], 'pgsga_value'),
                          ('PG-SGA=A13', ['A13'], 'pgsga_value'),
                          ('PGSGA = B/11', ['B/11'], 'pgsga_value'),
                          ('PG-SGA = B/11', ['B/11'], 'pgsga_value'),
                          ('PG-SGA 1A (well-nourished)', ['1A'], 'pgsga_value'),
                          ('(PG-SGA=A13)', ['A13'], 'pgsga_value'),
                          ('PG-SGA rating B/21', ['B/21'], 'pgsga_value'),])
def test_pgsga_value(test_pgsga_value_input, test_pgsga_value_attr_lab, attribute_label):
    doc = nlp(test_pgsga_value_input)
    attrs = [str(t._.pgsga_value) for t in doc if t._.pgsga_value != -1]
    assert attrs == test_pgsga_value_attr_lab, 'attribute test case failure: test_case, pgsga_value'

# @pytest.mark.parametrize('test_time_entities_input, test_time_entities_attr_lab, attribute_label',
#                          [('vs @9:00am BP', ['@9:00am'], 'time'),
#                           ('urinalysis @ 11:10 am SG', ['@ 11:10 am'], 'time'),
#                           ('picked up 1530hr', ['1530hr'], 'time'),
#                           ('seen@04:00hr', ['@04:00hr'], 'time'),
#                           ('1415hrs pt returned', ['1415hrs'], 'time'),
#                           ('9 oct - 1:30pm dr smith', ['1:30pm'], 'time'),
#                           ('at 2pm.', ['2pm'], 'time'),
#                           ('excision scan at 12o\'clock', ['12o\'clock'], 'time'),
#                           ('6 oclock position', ['6 oclock'], 'time'),
#                           ('3-5 o clock', ['3-5 o clock'], 'time'),
#                           ('at 11 \'o\'clock,', ['11 \'o\'clock,'], 'time'),])
# def test_time_entities(test_time_entities_input, test_time_entities_attr_lab, attribute_label):
#     doc = nlp(test_time_entities_input)
#     attrs = [t.text for t in doc if t._.time]
#     assert attrs == test_time_entities_attr_lab, 'attribute test case failure: test_case, time'


@pytest.mark.parametrize('test_unit_entities_input, test_unit_entities_attr_lab, attribute_label',
                         [('Medication: valaciclovir 500mg daily', ['500mg'], 'unit'),
                          ('wt 86.5kg stable', ['86.5kg'], 'unit'),
                          ('Fe 56 mol/L', ['56 mol/L'], 'unit'),
                          ('19.5x10^9/L', ['19.5x10^9/L'], 'unit'),
                          ('Hb nadir 92 g/L and there has been', ['92 g/L'], 'unit'),
                          ('Plt-256 x10^9/L', ['256 x10^9/L'], 'unit'),
                          ('plt 1,097/L', ['1,097/L'], 'unit'),
                          ('targeting >9g/l', ['9g/l'], 'unit'),
                          ('the 10mg/ml 0.2ml every 4-6', ['10mg/ml', '0.2ml'], 'unit'),])
def test_unit_entities(test_unit_entities_input, test_unit_entities_attr_lab, attribute_label):
    doc = nlp(test_unit_entities_input)
    attrs = [t.text for t in doc if t._.unit]
    assert attrs == test_unit_entities_attr_lab, 'attribute test case failure: test_case, unit'

@pytest.mark.parametrize('test_unit_norm_input, test_unit_norm_attr_lab, attribute_label',
                         [('Medication: valaciclovir 500mg daily', ['mg'], 'unit_value_norm'),
                          ('wt 86.5kg stable', ['kg'], 'unit_value_norm'),
                          ('Fe 56 mol/L', ['mol/L'], 'unit_value_norm'),
                          ('19.5x10^9/L', ['/L'], 'unit_value_norm'),
                          ('Hb nadir 92 g/L and there has been', ['g/L'], 'unit_value_norm'),
                          ('Plt-256 x10^9/L', ['/L'], 'unit_value_norm'),
                          ('plt 1,097/L', ['/L'], 'unit_value_norm'),
                          ('targeting >9g/l', ['g/l'], 'unit_value_norm'),])
def test_unit_norm(test_unit_norm_input, test_unit_norm_attr_lab, attribute_label):
    doc = nlp(test_unit_norm_input)
    attrs = [t.norm_ for t in doc if t._.unit_value != -1]
    assert attrs == test_unit_norm_attr_lab, 'attribute test case failure: test_case, unit_value_norm'


@pytest.mark.parametrize('test_unit_value_input, test_unit_value_attr_lab, attribute_label',
                         [('Medication: valaciclovir 500mg daily', ['500'], 'unit_value'),
                          ('wt 86.5kg stable', ['86.5'], 'unit_value'),
                          ('Fe 56 mol/L', ['56'], 'unit_value'),
                          ('19.5x10^9/L', ['19.5x10^9'], 'unit_value'),
                          ('Hb nadir 92 g/L and there has been', ['92'], 'unit_value'),
                          ('Plt-256 x10^9/L', ['256 x10^9'], 'unit_value'),
                          ('plt 1,097/L', ['1097'], 'unit_value'),
                          ('targeting >9g/l', ['9'], 'unit_value'),
                          ('the 10mg/ml 0.2ml every 4-6', ['10', '0.2'], 'unit_value'),])
def test_unit_value(test_unit_value_input, test_unit_value_attr_lab, attribute_label):
    doc = nlp(test_unit_value_input)
    attrs = [str(t._.unit_value) for t in doc if t._.unit_value != -1]
    assert attrs == test_unit_value_attr_lab, 'attribute test case failure: test_case, unit_value'


@pytest.mark.parametrize('test_weight_entities_input, test_weight_entities_attr_lab, attribute_label',
                         [('Anthro: 51.2kg (16/2/20)', ['51.2kg'], 'weight'),
                          ('Wt=81.1kg (weight gain 2kg in past week)', ['81.1kg', '2kg'], 'weight'),
                          ('weight stable (60kilos)', ['60kilos'], 'weight'),
                          ('weight ~70kg', ['70kg'], 'weight'),
                          ('weight is 45 kg', ['45 kg'], 'weight'),
                          ('Wt approx 75-80kg', ['80kg'], 'weight'),
                          ('Wt ~65kg', ['65kg'], 'weight'),
                          ('Wt 123.55Kg', ['123.55Kg'], 'weight'),
                          ('BMI 31.1', ['BMI 31.1'], 'weight'),
                          ('BMI 31.1 kg/m2', ['BMI 31.1'], 'weight'),
                          ('BMI: 31.1 (obese)', ['BMI: 31.1'], 'weight'),
                          ('BMI = 21.6 (Rec\'d BMI 22-27 for > 65 yrs)', ['BMI = 21.6', 'BMI 22'], 'weight'),
                          ('BMI 24.8kg/m2 ie within HWR', ['BMI 24.8'], 'weight'),
                          ('BMI > 27', ['BMI > 27'], 'weight'),
                          ('BMI 18.6 ie underwt', ['BMI 18.6'], 'weight'),
                          ('6/6/13 91.3kg', ['91.3kg'], 'weight'),
                          ('123lbs-stable', ['123lbs'], 'weight'),
                          ('gained 10 pounds', ['10 pounds'], 'weight'),
                          ('eating 50g protein', ['50g'], 'weight'),
                          ('44lb +/- 2lb', ['44lb', '2lb'], 'weight'),
                          ('son reports 5 kilogram loss', ['5 kilogram'], 'weight'),
                          ('weight up 49.2 kg. (clinic scale)', ['49.2 kg'], 'weight'),
                          ('wt83kg (dec 1.5kg over last 3 wk)', ['83kg', '1.5kg'], 'weight'),
                          ('wt83kg (dec 1.5kg past 3/52)', ['83kg', '1.5kg'], 'weight'),
                          ('Wt: 85kg (reported)', ['85kg'], 'weight'),])
def test_weight_entities(test_weight_entities_input, test_weight_entities_attr_lab, attribute_label):
    doc = nlp(test_weight_entities_input)
    attrs = [t.text for t in doc if t._.weight]
    assert attrs == test_weight_entities_attr_lab, 'attribute test case failure: test_case, weight'


@pytest.mark.parametrize('test_weight_value_input, test_weight_value_attr_lab, attribute_label',
                         [('Anthro: 51.2kg (16/2/20)', ['51.2'], 'unit_value'),
                          ('Wt=81.1kg (weight gain 2kg in past week)', ['81.1', '2'], 'unit_value'),
                          ('weight stable (60kilos)', ['60'], 'unit_value'),
                          ('weight ~70kg', ['70'], 'unit_value'),
                          ('weight is 45 kg', ['45'], 'unit_value'),
                          ('Wt approx 75-80kg', ['80'], 'unit_value'),
                          ('Wt ~65kg', ['65'], 'unit_value'),
                          ('Wt 123.55Kg', ['123.55'], 'unit_value'),
                          ('BMI 31.1', ['31.1'], 'unit_value'),
                          ('BMI 31.1 kg/m2', ['31.1'], 'unit_value'),
                          ('BMI: 31.1 (obese)', ['31.1'], 'unit_value'),
                          ('BMI = 21.6 (Rec\'d BMI 22-27 for > 65 yrs)', ['21.6', '22'], 'unit_value'),
                          ('BMI 24.8kg/m2 ie within HWR', ['24.8'], 'unit_value'),
                          ('BMI > 27', ['27'], 'unit_value'),
                          ('BMI 18.6 ie underwt', ['18.6'], 'unit_value'),
                          ('6/6/13 91.3kg', ['91.3'], 'unit_value'),
                          ('123lbs-stable', ['123'], 'unit_value'),
                          ('gained 10 pounds', ['10'], 'unit_value'),
                          ('eating 50g protein', ['50'], 'unit_value'),
                          ('44lb +/- 2lb', ['44', '2'], 'unit_value'),
                          ('son reports 5 kilogram loss', ['5'], 'unit_value'),
                          ('weight up 49.2 kg. (clinic scale)', ['49.2'], 'unit_value'),
                          ('wt83kg (dec 1.5kg over last 3 wk)', ['83', '1.5'], 'unit_value'),
                          ('wt83kg (dec 1.5kg past 3/52)', ['83', '1.5'], 'unit_value'),
                          ('Wt: 85kg (reported)', ['85'], 'unit_value'),])
def test_weight_value(test_weight_value_input, test_weight_value_attr_lab, attribute_label):
    doc = nlp(test_weight_value_input)
    attrs = [str(t._.unit_value) for t in doc if t._.unit_value != -1]
    assert attrs == test_weight_value_attr_lab, 'attribute test case failure: test_case, unit_value'


@pytest.mark.parametrize('test_weight_value_unit_input, test_weight_value_unit_attr_lab, attribute_label',
                         [('Anthro: 51.2kg (16/2/20)', ['kg'], 'unit_value_norm'),
                          ('Wt=81.1kg (weight gain 2kg in past week)', ['kg', 'kg'], 'unit_value_norm'),
                          ('weight stable (60kilos)', ['kilos'], 'unit_value_norm'),
                          ('weight ~70kg', ['kg'], 'unit_value_norm'),
                          ('weight is 45 kg', ['kg'], 'unit_value_norm'),
                          ('Wt approx 75-80kg', ['kg'], 'unit_value_norm'),
                          ('Wt ~65kg', ['kg'], 'unit_value_norm'),
                          ('Wt 123.55Kg', ['Kg'], 'unit_value_norm'),
                          ('BMI 31.1', ['BMI'], 'unit_value_norm'),
                          ('BMI 31.1 kg/m2', ['BMI'], 'unit_value_norm'),
                          ('BMI: 31.1 (obese)', ['BMI'], 'unit_value_norm'),
                          ('BMI = 21.6 (Rec\'d BMI 22-27 for > 65 yrs)', ['BMI', 'BMI'], 'unit_value_norm'),
                          ('BMI 24.8kg/m2 ie within HWR', ['BMI'], 'unit_value_norm'),
                          ('BMI > 27', ['BMI'], 'unit_value_norm'),
                          ('BMI 18.6 ie underwt', ['BMI'], 'unit_value_norm'),
                          ('6/6/13 91.3kg', ['kg'], 'unit_value_norm'),
                          ('123lbs-stable', ['lbs'], 'unit_value_norm'),
                          ('gained 10 pounds', ['pounds'], 'unit_value_norm'),
                          ('eating 50g protein', ['g'], 'unit_value_norm'),
                          ('44lb +/- 2lb', ['lb', 'lb'], 'unit_value_norm'),
                          ('son reports 5 kilogram loss', ['kilogram'], 'unit_value_norm'),
                          ('weight up 49.2 kg. (clinic scale)', ['kg'], 'unit_value_norm'),
                          ('wt83kg (dec 1.5kg over last 3 wk)', ['kg', 'kg'], 'unit_value_norm'),
                          ('wt83kg (dec 1.5kg over last 3 wk)', ['kg', 'kg'], 'unit_value_norm'),
                          ('wt83kg (dec 1.5kg past 3/52)', ['kg', 'kg'], 'unit_value_norm'),
                          ('Wt: 85kg (reported)', ['kg'], 'unit_value_norm'),])
def test_weight_value_unit(test_weight_value_unit_input, test_weight_value_unit_attr_lab, attribute_label):
    doc = nlp(test_weight_value_unit_input)
    attrs = [t.norm_ for t in doc if t._.unit_value != -1]
    assert attrs == test_weight_value_unit_attr_lab, 'attribute test case failure: test_case, unit_value_norm'

