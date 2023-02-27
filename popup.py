class Popup:

    def __init__(self, meteor):
        self.__mname = meteor.meteor_name
        self.__myear = meteor.meteor_year
        self.__mclass = meteor.meteor_class
        self.__mmass = meteor.meteor_mass
        self.__mhtml = """<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="meteor_styles.css">
<H4>{}""".format(self.__mname) + """</h4>
</head>
<table>
<tbody>
<tr><td>Name</td><td>{}""".format(self.__mname) + """</td></tr>
<tr><td>Year</td><td>{}""".format(self.__myear) + """</td></tr>
<tr><td>Class</td><td>{}""".format(self.__mclass) + """</td></tr>
<tr><td>Weight</td><td>{}""".format(self.__mmass) + """</td></tr>
</tbody>
</table>
</html>
"""

    @property
    def mhtml(self):
        return self.__mhtml

    @property
    def mname(self):
        return self.__mname

    @property
    def myear(self):
        return self.__myear

    @property
    def mclass(self):
        return self.__mclass

    def __str__(self):
        return f"{self.mhtml}"
