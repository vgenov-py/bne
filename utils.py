import re
"(?<=\.\d{3}\..)\|"
re_tag = "\.\d{3}\.\W{1,3}\||\.\d{3}\.\W{1}\d{1,2}\W{1}\||\.\d{3}\.\d{1,2}\W{1,2}\|"
re_dollar = "\|.{1}"
n1 = '''.000. |az n 0cza
.001. |aXX460733
.003. |aSpMaBN
.005. |a20191028142628.2
.008. |a031022 n anznnbabn          |a ana
.010.   |aXX460733
.016.   |aBNE20032766540
.024. 7 |ahttp://viaf.org/viaf/316734806|2viaf
.024. 7 |ahttp://viaf.org/viaf/316734806|2viaf
.024. 7 |ahttp://viaf.org/viaf/316734806|2viaf
.024. 7 |ahttp://viaf.org/viaf/316734806|2viaf
.024. 7 |ahttp://viaf.org/viaf/316734806|2viaf
.024. 7 |ahttp://viaf.org/viaf/316734806|2viaf
.034.   |dW0055846|eW0055846|fN0425318|gN0425318|2ngn
.040.   |aSpMaBN|bspa|cSpMaBN|erdc|fembne
.042.   |a200310291444PCMPBC  BNEP 00
.080.   |a(460.181 Abelgas de Luna)|2mrf12
.151.   |aAbelgas de Luna
.451.   |aAbelgas de Luna (Entidad local menor)
.551.   |wg|aSena de Luna
.551.   |OTRA COSA
.670.   |aELE|b(Abelgas de Luna)
.670.   |aNGN|b(Abelgas de Luna)
.781.   |zEspaña|zCastilla y León|zLeón (Provincia)|zSena de Luna|zAbelgas de Luna
.856.   |uhttps://maps.google.es/maps?q=W005+58'46''N042+53'18'''''

n2 ='''.000. |az n 0cza
.001. |aXX458594
.003. |aSpMaBN
.005. |a20180716090104.2
.008. |a990927 n anznnbabn          |a ana    ##
.010.   |aXX458594
.016.   |aBNE19999847525
.024. 7 |ahttp://viaf.org/viaf/316734302|2viaf
.024. 7 |ahttps://www.wikidata.org/wiki/Q26000764|2wikidata
.034.   |dW0013820|eW0013820|fN0425624|gN0425624|2ngn
.040.   |aSpMaBN|bspa|cSpMaBN|erdc|fembne
.042.   |a20120320
.080.   |a(460.16 Ripa)|22015
.151.   |aRipa
.451.   |aErripa
.451.   |aRipa/Erripa
.451.   |aRipa (Entidad local menor)
.551.   |wg|aOdieta
.670.   |aNGN|b(Ripa/Erripa)
.670.   |aINEBASE. Nomenclátor|b(Ripa)
.781.   |zEspaña|zNavarra (Comunidad Autónoma)|zOdieta|zRipa
.856.   |uhttps://maps.google.es/maps?q=W001+38'20''N042+56'24'''''

def dollar_parser(subfields: str) -> tuple:
    for i, text in enumerate(subfields[5:]):
        dollars = re.findall(re_dollar, text)
        dollars = map(lambda dollar: dollar.replace("|", ""), dollars)
        dollar_texts = re.split(re_dollar, text)[1:]
        subfields[i + 5] = tuple(zip(dollars, dollar_texts))

def dict_mapper(record: str) -> dict:
    tags = list(map(lambda tag: f"{tag[1:4]}:", re.findall(re_tag, record)))
    tag_coincidence = 0
    for i, tag in enumerate(tags):
        if tags[i-1][0:4] == tag:
            tag_coincidence += 1
            tags[i] += f"{tag_coincidence}"
        else:
            tag_coincidence = 0

    texts = re.split(re_tag, record)[1:]
    texts = map(lambda text:f"|{text}", texts)
    # texts = map(lambda text:text.replace("\n",""), texts)
    result = dict(zip(tags,texts))
    return result

def dict_mapper(record: str) -> dict:
    result = {}
    tag_coincidence = 0
    old_tag = None
    for line in re.split("\n(?=\.\d{3}\.)", record):
        tag, value = line.split("|", 1)
        tag = f"{tag[1:4]}:"
        if old_tag == tag:
            tag_coincidence += 1
            tag = f"{tag[0:3]}:{tag_coincidence}"
        else:
            tag_coincidence = 0
        result[tag] = value
        old_tag = tag
    return result

def dollar_replacer(subfield: str, replacer:str = " "):
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
    a = dict_mapper(n2)
    # print(a)
    # print(csv_mapper({"001:": "a", "024:": "b","034:": "c"}))