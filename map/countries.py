from pygal_maps_world.i18n import COUNTRIES
from pygal_maps_world import i18n
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
