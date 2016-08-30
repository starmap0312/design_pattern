import xmltodict

xml = """
<mydocument has="an attribute">
  <and>
    <many>elements</many>
    <many>more elements</many>
  </and>
  <plus a="complex">
    element as well
  </plus>
</mydocument>
"""

doc = xmltodict.parse(xml)

print(doc['mydocument']['@has'])          # == 'an attribute'
print(doc['mydocument']['and']['many'])   # == ['elements', 'more elements']
print(doc['mydocument']['plus']['@a'])    # == 'complex'
print(doc['mydocument']['plus']['#text']) # == 'element as well'

