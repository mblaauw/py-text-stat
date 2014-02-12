from readability_score.calculators.fleschkincaid import *
from readability_score.calculators.dalechall import *
from readability_score.calculators.ari import *

from readability_score.calculators.colemanliau import *
from readability_score.calculators.flesch import *
from readability_score.calculators.smog import *

locale = 'nl_NL'
text = open('./data/nl/Anna Karenina - Leo Nikolaj Tolstoj.txt').read()

fk = FleschKincaid(text, locale='nl_NL')
dc = DaleChall(text, simplewordlist=[], locale='nl_NL')
ar = ARI(text, locale='nl_NL')
cl = ColemanLiau(text, locale='nl_NL')
fl = Flesch(text, locale='nl_NL')
sm = SMOG(text, locale='nl_NL')


print fk.us_grade
print dc.us_grade
print ar.us_grade
print cl.us_grade
print fl.us_grade
print sm.us_grade
