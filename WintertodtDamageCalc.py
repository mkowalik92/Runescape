hitpoints_level = int(input('Hitpoints Level: '))
firemaking_level = int(input('Firemaking Level: '))
braziers_lit = int(input('Braziers Lit: '))

warm_items = 4

standard_attack = ((16 - warm_items - (2 * braziers_lit)) * (hitpoints_level + 1) ) / firemaking_level
brazier_attack = 2 * (((10 - warm_items) * (hitpoints_level + 1)) / firemaking_level)
area_attack = 3 * (((1- - warm_items) * (hitpoints_level + 1)) / firemaking_level)

print('Standard Attack: {}'.format(standard_attack))
print('Brazier Attack: {}'.format(brazier_attack))
print('Area Attack: {}'.format(area_attack))
