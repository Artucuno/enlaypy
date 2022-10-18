from enlaypy import EnlayClient

a = EnlayClient('')

print(a.get_advertisers())

print('\n\n\n')
ads = a.create_placements('ecf47899-a850-44a2-9f9b-8173f79fdf98')
adl = []
for f in ads:
    print(f)
    print(a.click_placement(f['id']))
    adl += [{'id': f['id']}]
    print(adl)

a.view_placement(adl)
