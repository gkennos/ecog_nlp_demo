import pytest 
from cava_nlp import CaVaLang, CaVaRetokenizer

nlp = CaVaLang()
nlp.tokenizer = CaVaRetokenizer(nlp)
nlp.add_pipe('ecog_status', first=True)
nlp.add_pipe('unit_value')
nlp.add_pipe('weight_value')
nlp.add_pipe('pgsga_value')
nlp.add_pipe('feeding_tube_value')