import os
import folium
import webbrowser
from meteor import Meteor
from popup import Popup

# general lat lon for US EAST and PA
US_EAST_LAT = (19.0, 67.0)
US_EAST_LON = (-82.0, -69.0)
US_PA_LAT = 41.0
US_PA_LON = -77.0

# dir path to this file
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

# Output file - HTML meteorites map
METEORS_HTML_FILE = DIR_PATH + '\\assets\\meteors.html'

# Input file - meteorite landings csv file
METEORS_CSV_FILE = DIR_PATH + '\\assets\\Meteorite_Landings.csv'


def main():

    # read/load the meteorite landings csv file
    Meteor.instantiate_from_csv(METEORS_CSV_FILE)

    # create a folium map instance with a focus over PA
    m = folium.Map(location=[US_PA_LAT, US_PA_LON], zoom_start=6, tiles="cartodb positron")

    # for each meteorite in the csv file
    for this_meteor in Meteor.all:
        # proper formatting of the lat and lon coordinates
        coords = tuple(map(float, this_meteor.geo_loc.split(', ')))

        # if the meteorite landed on the US East Coast, mark it on the map
        if (US_EAST_LAT[0] < coords[0] < US_EAST_LAT[1]) and \
                (US_EAST_LON[0] < coords[1] < US_EAST_LON[1]):

            # print coordinates and meteor name to console
            print(f"{str(coords)} {this_meteor.meteor_name}")

            # create an HTML formatted popup box containing the meteorites information
            h = Popup(this_meteor)
            popup = folium.Popup(folium.Html(h.mhtml, script=True), max_width=500)

            # mark the meteorites landing on the map
            m.add_child(folium.CircleMarker(location=coords,
                                            popup=popup,
                                            radius=5,
                                            fill_color='blue'))
            del h
            del popup

    # save the map to an html file
    m.save(METEORS_HTML_FILE)

    print("----------")
    print(f"Map has been saved to {METEORS_HTML_FILE}")
    print("----------")

    del m

    webbrowser.get().open_new_tab(METEORS_HTML_FILE)


if __name__ == '__main__':
    main()
