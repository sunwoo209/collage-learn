items = 'zero-one-two-three'.split('-') #스플릿 괄호 기준으로 구분//문자열 '' 포함해야됨
print(items)


example="theteamlab.univ.edu"
subdomain,domain,tld = example.split('.') #나누어서 각각 리스트 순번대로 배분
print(subdomain,"과",domain,"and",tld)
