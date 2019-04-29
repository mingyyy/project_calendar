from django.forms import Form, ChoiceField

# in total 222 countries
# DESTINATION_LIST = ['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AO', 'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA',
#            'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW',
#            'BY', 'BZ', 'CA', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU',
#            'CV', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ER', 'ES', 'ET',
#            'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GH', 'GI', 'GL', 'GM',
#            'GN', 'GP', 'GQ', 'GR', 'GT', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL',
#            'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN',
#            'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV',
#            'LY', 'MA', 'MC', 'MD', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MQ', 'MR', 'MS',
#            'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO',
#            'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR',
#            'PS', 'PT', 'PW', 'PY', 'QA', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG',
#            'SH', 'SI', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SY', 'SZ', 'TD', 'TG', 'TH',
#            'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ',
#            'VA', 'VC', 'VE', 'VI', 'VN', 'VU', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']

DESTINATION_CHOICE = (('AD', 'AD'), ('AE', 'AE'), ('AF', 'AF'), ('AG', 'AG'), ('AI', 'AI'), ('AL', 'AL'), ('AM', 'AM'), ('AO', 'AO'), ('AR', 'AR'), ('AS', 'AS'), ('AT', 'AT'), ('AU', 'AU'), ('AW', 'AW'), ('AZ', 'AZ'), ('BA', 'BA'), ('BB', 'BB'), ('BD', 'BD'), ('BE', 'BE'), ('BF', 'BF'), ('BG', 'BG'), ('BH', 'BH'), ('BI', 'BI'), ('BJ', 'BJ'), ('BM', 'BM'), ('BN', 'BN'), ('BO', 'BO'), ('BR', 'BR'), ('BS', 'BS'), ('BT', 'BT'), ('BW', 'BW'), ('BY', 'BY'), ('BZ', 'BZ'), ('CA', 'CA'), ('CD', 'CD'), ('CF', 'CF'), ('CG', 'CG'), ('CH', 'CH'), ('CI', 'CI'), ('CK', 'CK'), ('CL', 'CL'), ('CM', 'CM'), ('CN', 'CN'), ('CO', 'CO'), ('CR', 'CR'), ('CU', 'CU'), ('CV', 'CV'), ('CY', 'CY'), ('CZ', 'CZ'), ('DE', 'DE'), ('DJ', 'DJ'), ('DK', 'DK'), ('DM', 'DM'), ('DO', 'DO'), ('DZ', 'DZ'), ('EC', 'EC'), ('EE', 'EE'), ('EG', 'EG'), ('ER', 'ER'), ('ES', 'ES'), ('ET', 'ET'), ('FI', 'FI'), ('FJ', 'FJ'), ('FK', 'FK'), ('FM', 'FM'), ('FO', 'FO'), ('FR', 'FR'), ('GA', 'GA'), ('GB', 'GB'), ('GD', 'GD'), ('GE', 'GE'), ('GF', 'GF'), ('GH', 'GH'), ('GI', 'GI'), ('GL', 'GL'), ('GM', 'GM'), ('GN', 'GN'), ('GP', 'GP'), ('GQ', 'GQ'), ('GR', 'GR'), ('GT', 'GT'), ('GW', 'GW'), ('GY', 'GY'), ('HK', 'HK'), ('HN', 'HN'), ('HR', 'HR'), ('HT', 'HT'), ('HU', 'HU'), ('ID', 'ID'), ('IE', 'IE'), ('IL', 'IL'), ('IN', 'IN'), ('IO', 'IO'), ('IQ', 'IQ'), ('IR', 'IR'), ('IS', 'IS'), ('IT', 'IT'), ('JM', 'JM'), ('JO', 'JO'), ('JP', 'JP'), ('KE', 'KE'), ('KG', 'KG'), ('KH', 'KH'), ('KI', 'KI'), ('KM', 'KM'), ('KN', 'KN'), ('KP', 'KP'), ('KR', 'KR'), ('KW', 'KW'), ('KY', 'KY'), ('KZ', 'KZ'), ('LA', 'LA'), ('LB', 'LB'), ('LC', 'LC'), ('LI', 'LI'), ('LK', 'LK'), ('LR', 'LR'), ('LS', 'LS'), ('LT', 'LT'), ('LU', 'LU'), ('LV', 'LV'), ('LY', 'LY'), ('MA', 'MA'), ('MC', 'MC'), ('MD', 'MD'), ('MF', 'MF'), ('MG', 'MG'), ('MH', 'MH'), ('MK', 'MK'), ('ML', 'ML'), ('MM', 'MM'), ('MN', 'MN'), ('MO', 'MO'), ('MQ', 'MQ'), ('MR', 'MR'), ('MS', 'MS'), ('MT', 'MT'), ('MU', 'MU'), ('MV', 'MV'), ('MW', 'MW'), ('MX', 'MX'), ('MY', 'MY'), ('MZ', 'MZ'), ('NA', 'NA'), ('NC', 'NC'), ('NE', 'NE'), ('NF', 'NF'), ('NG', 'NG'), ('NI', 'NI'), ('NL', 'NL'), ('NO', 'NO'), ('NP', 'NP'), ('NR', 'NR'), ('NU', 'NU'), ('NZ', 'NZ'), ('OM', 'OM'), ('PA', 'PA'), ('PE', 'PE'), ('PF', 'PF'), ('PG', 'PG'), ('PH', 'PH'), ('PK', 'PK'), ('PL', 'PL'), ('PM', 'PM'), ('PN', 'PN'), ('PR', 'PR'), ('PS', 'PS'), ('PT', 'PT'), ('PW', 'PW'), ('PY', 'PY'), ('QA', 'QA'), ('RO', 'RO'), ('RS', 'RS'), ('RU', 'RU'), ('RW', 'RW'), ('SA', 'SA'), ('SB', 'SB'), ('SC', 'SC'), ('SD', 'SD'), ('SE', 'SE'), ('SG', 'SG'), ('SH', 'SH'), ('SI', 'SI'), ('SK', 'SK'), ('SL', 'SL'), ('SM', 'SM'), ('SN', 'SN'), ('SO', 'SO'), ('SR', 'SR'), ('ST', 'ST'), ('SV', 'SV'), ('SY', 'SY'), ('SZ', 'SZ'), ('TD', 'TD'), ('TG', 'TG'), ('TH', 'TH'), ('TJ', 'TJ'), ('TK', 'TK'), ('TL', 'TL'), ('TM', 'TM'), ('TN', 'TN'), ('TO', 'TO'), ('TR', 'TR'), ('TT', 'TT'), ('TV', 'TV'), ('TZ', 'TZ'), ('UA', 'UA'), ('UG', 'UG'), ('US', 'US'), ('UY', 'UY'), ('UZ', 'UZ'), ('VA', 'VA'), ('VC', 'VC'), ('VE', 'VE'), ('VI', 'VI'), ('VN', 'VN'), ('VU', 'VU'), ('WS', 'WS'), ('YE', 'YE'), ('YT', 'YT'), ('ZA', 'ZA'), ('ZM', 'ZM'), ('ZW', 'ZW'),)

CITIZENSHIP_CHOICE = DESTINATION_CHOICE


class EntryRequirementForm(Form):
    # citizenship = CharField(max_length=2,widget=Textarea(attrs={'placeholder': 'US'}),
    #                         help_text="Country code: US for The United States")
    # destination = CharField(max_length=2, widget=Textarea(attrs={'placeholder': 'VN'}),
    #                         help_text="Country code: VN for Vietname")

    citizenship = ChoiceField(label='You passport issued by which country?',
                              choices=CITIZENSHIP_CHOICE)

    destination = ChoiceField(label='Which country are you going?',
                              choices=DESTINATION_CHOICE)
