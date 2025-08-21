import arrow
from collections import namedtuple

brewing_time =arrow.utcnow()
brewing_time.to("Europe/Paris")

chaiProfile = namedtuple("chaiprofile", ["flavor", "aroma"])