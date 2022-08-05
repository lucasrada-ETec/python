database={"Modelo":"Max L4",
          "Fábrica":"Bangho",
          "Color":"Negro",
          "Número de Serie":"AR020000882127"
          }
post = lambda ref1, ref2 : database.update({ref1 : ref2})
get = lambda ref1 : database[ref1]
put = lambda ref1 : [database[ref1]=ref2]