import re
#ex1
# for str in ['abbbb', 'sdsadbasd', 'fdsoijaoisdk', 'a']:
#     if re.fullmatch(r'[a]{1}[b]*', str):
#         print(re.fullmatch(r'[a]{1}[b]*', str)[0])
#     else:
#         print("None")
#ex2
# for str in ['abbbb', 'sdsadbasd', 'fdsoijaoisdk', 'a', 'abb', 'abbb']:
#     if re.fullmatch(r'[a]{1}[b]{2,3}', str):
#         print(re.fullmatch(r'[a]{1}[b]{2,3}', str)[0])
#     else:
#         print("None")
#ex3
# for str in ['abbbb', 'dsadaa_bdasd fijsdjfsoij_oiajsdioajd', 'fdsoijaoisdk', 'a']:
#     print(re.findall(r'[a-z]*[_]{1}[a-z]*', str))
#ex4
# for str in ['abbbb', 'Asadaa Zijsdjfsoijoiajsdioajd', 'ZSdsoijaoisdk', 'a']:
#     print(re.findall(r'[A-Z]{1}[a-z]+', str))
#ex5
# for str in ['abbbb', 'adsaijdioiajdoifjoijfeoijefijwejb', 'fdsoijaoisdk', 'a']:
#     print(re.fullmatch(r'[a]+.*b$', str))
#ex6
# for str in ['ab bb .b', 'a,b', 'f,dsoijaoisdk', 'a']:
#     print(re.sub(r'[ .,]{1}', ';', str))
#ex7
# def snake_to_camel(snake_case):
#     return re.sub(r"_([a-z])", lambda s: s.group(1).upper(), snake_case)
# print(snake_to_camel("snake_case"))
#ex8
# for str in ['snakeTcase', 'a,b', 'fDFDSdsoijaoisdk', 'a']:
#     print(re.split(r'[A-Z]+', str))
#ex9
# print(re.sub(r'\B([A-Z])', lambda s: ' '+s.group(1), "AbcDefGdfF"))
#ex10
# def camelToSnake(camelCase):
#     return re.sub(r"\B([A-Z])", lambda s: '_'+s.group(1), camelCase).lower()
# print(camelToSnake("camelCase"))
