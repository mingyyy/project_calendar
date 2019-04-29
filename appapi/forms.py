from django.forms import Form, ChoiceField
import requests, json
# in total 222 countries
DESTINATION_LIST = ['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AO', 'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA',
           'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW',
           'BY', 'BZ', 'CA', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU',
           'CV', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ER', 'ES', 'ET',
           'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GH', 'GI', 'GL', 'GM',
           'GN', 'GP', 'GQ', 'GR', 'GT', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL',
           'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN',
           'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV',
           'LY', 'MA', 'MC', 'MD', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MQ', 'MR', 'MS',
           'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO',
           'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR',
           'PS', 'PT', 'PW', 'PY', 'QA', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG',
           'SH', 'SI', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SY', 'SZ', 'TD', 'TG', 'TH',
           'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ',
           'VA', 'VC', 'VE', 'VI', 'VN', 'VU', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']

# DESTINATION_CHOICE = (('AD', 'AD'), ('AE', 'AE'), ('AF', 'AF'), ('AG', 'AG'), ('AI', 'AI'), ('AL', 'AL'), ('AM', 'AM'), ('AO', 'AO'), ('AR', 'AR'), ('AS', 'AS'), ('AT', 'AT'), ('AU', 'AU'), ('AW', 'AW'), ('AZ', 'AZ'), ('BA', 'BA'), ('BB', 'BB'), ('BD', 'BD'), ('BE', 'BE'), ('BF', 'BF'), ('BG', 'BG'), ('BH', 'BH'), ('BI', 'BI'), ('BJ', 'BJ'), ('BM', 'BM'), ('BN', 'BN'), ('BO', 'BO'), ('BR', 'BR'), ('BS', 'BS'), ('BT', 'BT'), ('BW', 'BW'), ('BY', 'BY'), ('BZ', 'BZ'), ('CA', 'CA'), ('CD', 'CD'), ('CF', 'CF'), ('CG', 'CG'), ('CH', 'CH'), ('CI', 'CI'), ('CK', 'CK'), ('CL', 'CL'), ('CM', 'CM'), ('CN', 'CN'), ('CO', 'CO'), ('CR', 'CR'), ('CU', 'CU'), ('CV', 'CV'), ('CY', 'CY'), ('CZ', 'CZ'), ('DE', 'DE'), ('DJ', 'DJ'), ('DK', 'DK'), ('DM', 'DM'), ('DO', 'DO'), ('DZ', 'DZ'), ('EC', 'EC'), ('EE', 'EE'), ('EG', 'EG'), ('ER', 'ER'), ('ES', 'ES'), ('ET', 'ET'), ('FI', 'FI'), ('FJ', 'FJ'), ('FK', 'FK'), ('FM', 'FM'), ('FO', 'FO'), ('FR', 'FR'), ('GA', 'GA'), ('GB', 'GB'), ('GD', 'GD'), ('GE', 'GE'), ('GF', 'GF'), ('GH', 'GH'), ('GI', 'GI'), ('GL', 'GL'), ('GM', 'GM'), ('GN', 'GN'), ('GP', 'GP'), ('GQ', 'GQ'), ('GR', 'GR'), ('GT', 'GT'), ('GW', 'GW'), ('GY', 'GY'), ('HK', 'HK'), ('HN', 'HN'), ('HR', 'HR'), ('HT', 'HT'), ('HU', 'HU'), ('ID', 'ID'), ('IE', 'IE'), ('IL', 'IL'), ('IN', 'IN'), ('IO', 'IO'), ('IQ', 'IQ'), ('IR', 'IR'), ('IS', 'IS'), ('IT', 'IT'), ('JM', 'JM'), ('JO', 'JO'), ('JP', 'JP'), ('KE', 'KE'), ('KG', 'KG'), ('KH', 'KH'), ('KI', 'KI'), ('KM', 'KM'), ('KN', 'KN'), ('KP', 'KP'), ('KR', 'KR'), ('KW', 'KW'), ('KY', 'KY'), ('KZ', 'KZ'), ('LA', 'LA'), ('LB', 'LB'), ('LC', 'LC'), ('LI', 'LI'), ('LK', 'LK'), ('LR', 'LR'), ('LS', 'LS'), ('LT', 'LT'), ('LU', 'LU'), ('LV', 'LV'), ('LY', 'LY'), ('MA', 'MA'), ('MC', 'MC'), ('MD', 'MD'), ('MF', 'MF'), ('MG', 'MG'), ('MH', 'MH'), ('MK', 'MK'), ('ML', 'ML'), ('MM', 'MM'), ('MN', 'MN'), ('MO', 'MO'), ('MQ', 'MQ'), ('MR', 'MR'), ('MS', 'MS'), ('MT', 'MT'), ('MU', 'MU'), ('MV', 'MV'), ('MW', 'MW'), ('MX', 'MX'), ('MY', 'MY'), ('MZ', 'MZ'), ('NA', 'NA'), ('NC', 'NC'), ('NE', 'NE'), ('NF', 'NF'), ('NG', 'NG'), ('NI', 'NI'), ('NL', 'NL'), ('NO', 'NO'), ('NP', 'NP'), ('NR', 'NR'), ('NU', 'NU'), ('NZ', 'NZ'), ('OM', 'OM'), ('PA', 'PA'), ('PE', 'PE'), ('PF', 'PF'), ('PG', 'PG'), ('PH', 'PH'), ('PK', 'PK'), ('PL', 'PL'), ('PM', 'PM'), ('PN', 'PN'), ('PR', 'PR'), ('PS', 'PS'), ('PT', 'PT'), ('PW', 'PW'), ('PY', 'PY'), ('QA', 'QA'), ('RO', 'RO'), ('RS', 'RS'), ('RU', 'RU'), ('RW', 'RW'), ('SA', 'SA'), ('SB', 'SB'), ('SC', 'SC'), ('SD', 'SD'), ('SE', 'SE'), ('SG', 'SG'), ('SH', 'SH'), ('SI', 'SI'), ('SK', 'SK'), ('SL', 'SL'), ('SM', 'SM'), ('SN', 'SN'), ('SO', 'SO'), ('SR', 'SR'), ('ST', 'ST'), ('SV', 'SV'), ('SY', 'SY'), ('SZ', 'SZ'), ('TD', 'TD'), ('TG', 'TG'), ('TH', 'TH'), ('TJ', 'TJ'), ('TK', 'TK'), ('TL', 'TL'), ('TM', 'TM'), ('TN', 'TN'), ('TO', 'TO'), ('TR', 'TR'), ('TT', 'TT'), ('TV', 'TV'), ('TZ', 'TZ'), ('UA', 'UA'), ('UG', 'UG'), ('US', 'US'), ('UY', 'UY'), ('UZ', 'UZ'), ('VA', 'VA'), ('VC', 'VC'), ('VE', 'VE'), ('VI', 'VI'), ('VN', 'VN'), ('VU', 'VU'), ('WS', 'WS'), ('YE', 'YE'), ('YT', 'YT'), ('ZA', 'ZA'), ('ZM', 'ZM'), ('ZW', 'ZW'),)

DESTINATION_CHOICE = (('AF', 'Afghanistan'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AS', 'American Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AG', 'Antigua and Barbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia (Plurinational State of)'), ('BA', 'Bosnia and Herzegovina'), ('BW', 'Botswana'), ('BR', 'Brazil'), ('IO', 'British Indian Ocean Territory'), ('VI', 'Virgin Islands (U.S.)'), ('BN', 'Brunei Darussalam'), ('BG', 'Bulgaria'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('KH', 'Cambodia'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('CV', 'Cabo Verde'), ('KY', 'Cayman Islands'), ('CF', 'Central African Republic'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CG', 'Congo'), ('CD', 'Congo (Democratic Republic of the)'), ('CK', 'Cook Islands'), ('CR', 'Costa Rica'), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('ET', 'Ethiopia'), ('FK', 'Falkland Islands (Malvinas)'), ('FO', 'Faroe Islands'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GF', 'French Guiana'), ('PF', 'French Polynesia'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'), ('GP', 'Guadeloupe'), ('GT', 'Guatemala'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('VA', 'Holy See'), ('HN', 'Honduras'), ('HK', 'Hong Kong'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('CI', "Côte d'Ivoire"), ('IR', 'Iran (Islamic Republic of)'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', "Lao People's Democratic Republic"), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macao'), ('MK', 'Macedonia (the former Yugoslav Republic of)'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'), ('FM', 'Micronesia (Federated States of)'), ('MD', 'Moldova (Republic of)'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('NC', 'New Caledonia'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'), ('NF', 'Norfolk Island'), ('KP', "Korea (Democratic People's Republic of)"), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestine, State of'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PN', 'Pitcairn'), ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('MF', 'Saint Martin (French part)'), ('PM', 'Saint Pierre and Miquelon'), ('VC', 'Saint Vincent and the Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'), ('KR', 'Korea (Republic of)'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SZ', 'Swaziland'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syrian Arab Republic'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania, United Republic of'), ('TH', 'Thailand'), ('TL', 'Timor-Leste'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('US', 'United States of America'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('VN', 'Viet Nam'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe'))

#DESTINATION_CHOICE = (('AF', 'AF - Afghanistan'), ('AL', 'AL - Albania'), ('DZ', 'DZ - Algeria'), ('AS', 'AS - American Samoa'), ('AD', 'AD - Andorra'), ('AO', 'AO - Angola'), ('AI', 'AI - Anguilla'), ('AG', 'AG - Antigua and Barbuda'), ('AR', 'AR - Argentina'), ('AM', 'AM - Armenia'), ('AW', 'AW - Aruba'), ('AU', 'AU - Australia'), ('AT', 'AT - Austria'), ('AZ', 'AZ - Azerbaijan'), ('BS', 'BS - Bahamas'), ('BH', 'BH - Bahrain'), ('BD', 'BD - Bangladesh'), ('BB', 'BB - Barbados'), ('BY', 'BY - Belarus'), ('BE', 'BE - Belgium'), ('BZ', 'BZ - Belize'), ('BJ', 'BJ - Benin'), ('BM', 'BM - Bermuda'), ('BT', 'BT - Bhutan'), ('BO', 'BO - Bolivia (Plurinational State of)'), ('BA', 'BA - Bosnia and Herzegovina'), ('BW', 'BW - Botswana'), ('BR', 'BR - Brazil'), ('IO', 'IO - British Indian Ocean Territory'), ('VI', 'VI - Virgin Islands (U.S.)'), ('BN', 'BN - Brunei Darussalam'), ('BG', 'BG - Bulgaria'), ('BF', 'BF - Burkina Faso'), ('BI', 'BI - Burundi'), ('KH', 'KH - Cambodia'), ('CM', 'CM - Cameroon'), ('CA', 'CA - Canada'), ('CV', 'CV - Cabo Verde'), ('KY', 'KY - Cayman Islands'), ('CF', 'CF - Central African Republic'), ('TD', 'TD - Chad'), ('CL', 'CL - Chile'), ('CN', 'CN - China'), ('CO', 'CO - Colombia'), ('KM', 'KM - Comoros'), ('CG', 'CG - Congo'), ('CD', 'CD - Congo (Democratic Republic of the)'), ('CK', 'CK - Cook Islands'), ('CR', 'CR - Costa Rica'), ('HR', 'HR - Croatia'), ('CU', 'CU - Cuba'), ('CY', 'CY - Cyprus'), ('CZ', 'CZ - Czech Republic'), ('DK', 'DK - Denmark'), ('DJ', 'DJ - Djibouti'), ('DM', 'DM - Dominica'), ('DO', 'DO - Dominican Republic'), ('EC', 'EC - Ecuador'), ('EG', 'EG - Egypt'), ('SV', 'SV - El Salvador'), ('GQ', 'GQ - Equatorial Guinea'), ('ER', 'ER - Eritrea'), ('EE', 'EE - Estonia'), ('ET', 'ET - Ethiopia'), ('FK', 'FK - Falkland Islands (Malvinas)'), ('FO', 'FO - Faroe Islands'), ('FJ', 'FJ - Fiji'), ('FI', 'FI - Finland'), ('FR', 'FR - France'), ('GF', 'GF - French Guiana'), ('PF', 'PF - French Polynesia'), ('GA', 'GA - Gabon'), ('GM', 'GM - Gambia'), ('GE', 'GE - Georgia'), ('DE', 'DE - Germany'), ('GH', 'GH - Ghana'), ('GI', 'GI - Gibraltar'), ('GR', 'GR - Greece'), ('GL', 'GL - Greenland'), ('GD', 'GD - Grenada'), ('GP', 'GP - Guadeloupe'), ('GT', 'GT - Guatemala'), ('GN', 'GN - Guinea'), ('GW', 'GW - Guinea-Bissau'), ('GY', 'GY - Guyana'), ('HT', 'HT - Haiti'), ('VA', 'VA - Holy See'), ('HN', 'HN - Honduras'), ('HK', 'HK - Hong Kong'), ('HU', 'HU - Hungary'), ('IS', 'IS - Iceland'), ('IN', 'IN - India'), ('ID', 'ID - Indonesia'), ('CI', "CI - Côte d'Ivoire"), ('IR', 'IR - Iran (Islamic Republic of)'), ('IQ', 'IQ - Iraq'), ('IE', 'IE - Ireland'), ('IL', 'IL - Israel'), ('IT', 'IT - Italy'), ('JM', 'JM - Jamaica'), ('JP', 'JP - Japan'), ('JO', 'JO - Jordan'), ('KZ', 'KZ - Kazakhstan'), ('KE', 'KE - Kenya'), ('KI', 'KI - Kiribati'), ('KW', 'KW - Kuwait'), ('KG', 'KG - Kyrgyzstan'), ('LA', "LA - Lao People's Democratic Republic"), ('LV', 'LV - Latvia'), ('LB', 'LB - Lebanon'), ('LS', 'LS - Lesotho'), ('LR', 'LR - Liberia'), ('LY', 'LY - Libya'), ('LI', 'LI - Liechtenstein'), ('LT', 'LT - Lithuania'), ('LU', 'LU - Luxembourg'), ('MO', 'MO - Macao'), ('MK', 'MK - Macedonia (the former Yugoslav Republic of)'), ('MG', 'MG - Madagascar'), ('MW', 'MW - Malawi'), ('MY', 'MY - Malaysia'), ('MV', 'MV - Maldives'), ('ML', 'ML - Mali'), ('MT', 'MT - Malta'), ('MH', 'MH - Marshall Islands'), ('MQ', 'MQ - Martinique'), ('MR', 'MR - Mauritania'), ('MU', 'MU - Mauritius'), ('YT', 'YT - Mayotte'), ('MX', 'MX - Mexico'), ('FM', 'FM - Micronesia (Federated States of)'), ('MD', 'MD - Moldova (Republic of)'), ('MC', 'MC - Monaco'), ('MN', 'MN - Mongolia'), ('MS', 'MS - Montserrat'), ('MA', 'MA - Morocco'), ('MZ', 'MZ - Mozambique'), ('MM', 'MM - Myanmar'), ('NA', 'NA - Namibia'), ('NR', 'NR - Nauru'), ('NP', 'NP - Nepal'), ('NL', 'NL - Netherlands'), ('NC', 'NC - New Caledonia'), ('NZ', 'NZ - New Zealand'), ('NI', 'NI - Nicaragua'), ('NE', 'NE - Niger'), ('NG', 'NG - Nigeria'), ('NU', 'NU - Niue'), ('NF', 'NF - Norfolk Island'), ('KP', "KP - Korea (Democratic People's Republic of)"), ('NO', 'NO - Norway'), ('OM', 'OM - Oman'), ('PK', 'PK - Pakistan'), ('PW', 'PW - Palau'), ('PS', 'PS - Palestine, State of'), ('PA', 'PA - Panama'), ('PG', 'PG - Papua New Guinea'), ('PY', 'PY - Paraguay'), ('PE', 'PE - Peru'), ('PH', 'PH - Philippines'), ('PN', 'PN - Pitcairn'), ('PL', 'PL - Poland'), ('PT', 'PT - Portugal'), ('PR', 'PR - Puerto Rico'), ('QA', 'QA - Qatar'), ('RO', 'RO - Romania'), ('RU', 'RU - Russian Federation'), ('RW', 'RW - Rwanda'), ('SH', 'SH - Saint Helena, Ascension and Tristan da Cunha'), ('KN', 'KN - Saint Kitts and Nevis'), ('LC', 'LC - Saint Lucia'), ('MF', 'MF - Saint Martin (French part)'), ('PM', 'PM - Saint Pierre and Miquelon'), ('VC', 'VC - Saint Vincent and the Grenadines'), ('WS', 'WS - Samoa'), ('SM', 'SM - San Marino'), ('ST', 'ST - Sao Tome and Principe'), ('SA', 'SA - Saudi Arabia'), ('SN', 'SN - Senegal'), ('RS', 'RS - Serbia'), ('SC', 'SC - Seychelles'), ('SL', 'SL - Sierra Leone'), ('SG', 'SG - Singapore'), ('SK', 'SK - Slovakia'), ('SI', 'SI - Slovenia'), ('SB', 'SB - Solomon Islands'), ('SO', 'SO - Somalia'), ('ZA', 'ZA - South Africa'), ('KR', 'KR - Korea (Republic of)'), ('ES', 'ES - Spain'), ('LK', 'LK - Sri Lanka'), ('SD', 'SD - Sudan'), ('SR', 'SR - Suriname'), ('SZ', 'SZ - Swaziland'), ('SE', 'SE - Sweden'), ('CH', 'CH - Switzerland'), ('SY', 'SY - Syrian Arab Republic'), ('TJ', 'TJ - Tajikistan'), ('TZ', 'TZ - Tanzania, United Republic of'), ('TH', 'TH - Thailand'), ('TL', 'TL - Timor-Leste'), ('TG', 'TG - Togo'), ('TK', 'TK - Tokelau'), ('TO', 'TO - Tonga'), ('TT', 'TT - Trinidad and Tobago'), ('TN', 'TN - Tunisia'), ('TR', 'TR - Turkey'), ('TM', 'TM - Turkmenistan'), ('TV', 'TV - Tuvalu'), ('UG', 'UG - Uganda'), ('UA', 'UA - Ukraine'), ('AE', 'AE - United Arab Emirates'), ('GB', 'GB - United Kingdom of Great Britain and Northern Ireland'), ('US', 'US - United States of America'), ('UY', 'UY - Uruguay'), ('UZ', 'UZ - Uzbekistan'), ('VU', 'VU - Vanuatu'), ('VE', 'VE - Venezuela (Bolivarian Republic of)'), ('VN', 'VN - Viet Nam'), ('YE', 'YE - Yemen'), ('ZM', 'ZM - Zambia'), ('ZW', 'ZW - Zimbabwe'))
CITIZENSHIP_CHOICE = DESTINATION_CHOICE


class EntryRequirementForm(Form):
    # citizenship = CharField(max_length=2,widget=Textarea(attrs={'placeholder': 'US'}),
    #                         help_text="Country code: US for The United States")
    # destination = CharField(max_length=2, widget=Textarea(attrs={'placeholder': 'VN'}),
    #                         help_text="Country code: VN for Vietname")

    citizenship = ChoiceField(label='Passport issued by which country?',
                              choices=CITIZENSHIP_CHOICE)

    destination = ChoiceField(label='Which country are you visiting as a tourist?',
                              choices=DESTINATION_CHOICE)


def collect_names():
    name_map = []
    info = requests.get(f"https://restcountries.eu/rest/v2/all").json()
    for country in info:
        if country["alpha2Code"] in DESTINATION_LIST:
            name_map.append((country["alpha2Code"], f"{country['alpha2Code']} - {country['alpha2Code']}"))
    print(name_map)
