# ecog_nlp_demo
simple medspacy-based ecog nlp demo with disambiguation


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/gkennos/ecog_nlp_demo/HEAD?urlpath=%2Fdoc%2Ftree%2Fecog_disambiguation_demo.ipynb)



Known failure cases: 

| TestCase           | InputData                                  | ExpectedResult                | ActualResult | TargetEntity      | Comments                                                             |
|--------------------|--------------------------------------------|-------------------------------|--------------|-------------------|----------------------------------------------------------------------|
| test_ecog_entities | CurrentlyECOG 3 but improving              | ECOG 3                        | []           | ecog_status       | Could work around with 'ECOG' as special tokenisation case TBC?      |
| test_ecog_entities | History: ECOG From HCNH,  not mobile 4     | ECOG From HCNH,  not mobile 4 | []           | ecog_status       | Too far between label and value                                      |
| test_ecog_values   | ecog was 4 now 3                           | 3                             | 4            | ecog_status_value | Current specification takes the   highest number if a range provided |
| test_ecog_values   | History: ECOG From HCNH,  not mobile 4     | 4                             | []           | ecog_status_value | Too far between label and value                                      |                                                  |