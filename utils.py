import re

re_tag = "\.\d{3}\.\W{1,3}\||\.\d{3}\.\W{1}\d{1,2}\W{1}\||\.\d{3}\.\d{1,2}\W{1,2}\|"
re_dollar = "\|.{1}"

def dict_mapper(record: str) -> dict:
    result = {}
    tag_coincidence = 0
    old_tag = None
    try:
        for line in re.split("\n(?=\.\d{3}\.)", record):
            tag, value = line.split("|", 1)
            tag = f"{tag[1:4]}:"
            if old_tag == tag:
                tag_coincidence += 1
                tag = f"{tag[0:3]}:{tag_coincidence}"
            else:
                tag_coincidence = 0
            result[tag] = f"|{value}"
            old_tag = tag
        return result
    except Exception as e:
        pass

# def dict_mapper(record: str) -> dict:
#     result = {}
#     # for i,s in enumerate(record):
#     #     if s == ".":
#     #         try:
#     #             tag = f"{record[i]}{record[i+1]}{record[i+2]}{record[i+3]}{record[i+4]}"
#     #             if re.search("\.\d{3}\.", tag):
#     #                 value = re.split("\.\d{3}\.", record[i+5:], 1)
#     #                 if len(value) >= 1:
#     #                     result[tag] = value[0]
#     #         except Exception as e:
#     #             pass
#     tag = record[1:4]
#     def r_tag_v(record: str):
#         value = re.search("\.\d{3}\.", record)
#         tag = record[value.start():value.end()]
#         record = record[value.end():]
#         if value:
#             value = re.search("\.\d{3}\.", record) 
#             result[tag] = record[4:value.start()]
#             tag = record[value.start():value.end()]
#             record = record[value.end():]
#         if len(record) >= 1:
#             r_tag_v(record)
#     r_tag_v(record)
#     # print(value)
#     # print(tag)
#     return result

def dollar_replacer(subfield: str, replacer:str = " "):
    '''
    |a2010|22020 -> 2010 2020
    Every string should be in explicit-mode (starting with |)
    '''
    try:
        return re.sub(re_dollar, replacer, subfield).strip()
    except TypeError:
        return subfield

def csv_mapper(record: dict) -> tuple:
    '''
    This function will take a dict as an argument and will return the current expected fields to fill the geographic csv
    tags considered: 001, 024, 034... 
    '''
    bne_id = record.get("001:").replace("\n", "") if record.get("001:") else None
    bne_id = dollar_replacer(bne_id)

    '''
    024
    '''
    other_codes = ""
    for k, v in filter(lambda k: k[0].startswith("024"), record.items()):
        other_codes += f"{dollar_replacer(v)} ** "

    coord = record.get("034:").replace("\n", "") if record.get("034:") else None
    coord = dollar_replacer(coord)
    cdu = record.get("080:").replace("\n", "") if record.get("080:") else None
    cdu = dollar_replacer(cdu)
    header_geo = record.get("151:").replace("\n", "") if record.get("151:") else None
    header_geo = dollar_replacer(header_geo)
    '''
    451
    '''
    not_accepted_term = ""
    for k, v in filter(lambda k: k[0].startswith("451"), record.items()):
        other_codes += f"{dollar_replacer(v)} "
    related_geo_term = record.get("550:").replace("\n", "") if record.get("550:") else None
    related_geo_term = dollar_replacer(related_geo_term)
    return tuple([bne_id, other_codes, coord, cdu, header_geo, not_accepted_term, related_geo_term])

if __name__ == "__main__":
    a = dict_mapper('''.000. |az n 0cza
.001. |aXX102734
.003. |aSpMaBN
.005. |a20160615000000.4
.008. |a950120 n aiznnbabn          |a ana
.010.   |aXX102734
.016.   |aBNE19950048978
.024. 7 |ahttp://id.loc.gov/authorities/names/n96077394|2lcnaf
.024. 7 |ahttp://viaf.org/viaf/315538112|2viaf
.034.   |dE0020143|eE0020143|fN0412156|gN0412156|2geonames
.040.   |aSpMaBN|bspa|cSpMaBN|erdc|fembne
.042.   |a20141021
.080.   |a(460.235-21 Santa Coloma de Cervelló)|22015
.151.   |aCòlonia Güell (Santa Coloma de Cervelló)
.550.   |aBarrios|zSanta Coloma de Cervelló
.670.   |aLCSH|b[Colònia Güell S.A. (Santa Coloma de Cervelló, Spain)]
.670.   |aGeoNames|b(Còlonia Güell)
.670.   |aWWW Còlonia Güell, 21-10-2014|b(Còlonia Güell, Santa Coloma de
Cervelló. La Colonia Güell se inició en el año 1.890 a iniciativa del
empresario Eusebi Güell en su finca Can Soler de la Torre, situada en el
término municipal de Santa Coloma de Cervelló, actual Comarca del Baix\nLlobregat)|uhttp://www.gaudicoloniaguell.org/
''')
    print(a)