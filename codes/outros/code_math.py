import math

an=float(input('digite o angulo que voce deseja:'))
cosseno= math.cos(math.radians(an))
tangente= math.atan(math.radians(an))
seno= math.sin(math.radians(an))
print('o cosseno vai ser {:.2f}'.format(seno))
print('o cosseno vai ser {:.2f}'.format(cosseno))
print('o tangente vai ser {:.2f}'.format(tangente))
