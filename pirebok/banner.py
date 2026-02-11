"""pirebok CLI banner — The Witch."""

from __future__ import annotations

import base64
import colorsys
import os
import sys

BANNER_WIDTH = 80
BANNER_PIXEL_HEIGHT = 48

BANNER_RGB_DATA = (
    "EklpDkNfCzpTBy1BBSk7BCg7AyY5Aic6Aic4AiY2BSM1BSI0Byc5DCxDETVSGT9gK1J6SGubRGKR"
    "PWCMMUx4HzFeHCpYHSxaHyxbHy9cHTJgHjZlHzdnIjtrLEd+JEBtKk9yQWKcMlSTNVOTNFOUMFKR"
    "OFqeHkNnQxUzZh5GHylBW4WxZpjSbprOk6PQj5vJkJe3g5GvX4G0VHy0Z4q7mqzPiK3Tbp3SeqLT"
    "r7W9v8C+wMLBxMXCrL3Nlbvlk7nlor3kcazGH7qoh9bUxdvvr9jqu9To1Mrktb/gsdXiX77LNYqh"
    "Jml+K1xpJEZNCSgtIlqDG01wEkRjDT9aCDVJBjFFBTJGBTNJBjZMBjVLBzJKBzBIBzBGCDBIDTdX"
    "F0xvImOAJFNwMFN8Wn2uPlmFHjFcGyxaHixbHS5aGS9fGjFiHjVmHzdoIzttKkF3KUJ2FTdTQnCg"
    "OlmVMlaXNVqcQGSmUHW0GTtRUxw9aiRKGzhPXprDY5LNZpfNjKHOkZ3Kj5S6lJiwkpqvboiyTn6v"
    "V4S2fJ3KeqbWjavPtra2uLWxt7u7wMG/uMHEjbjpkbjmmbvfm7veT7XBMMu9j8ncvNPp29Xousnk"
    "jsHjs9Hid8jTNY2lJml+JVRiJ0ZQDSwxKXWrKGmYJluDGkhrDkBfCz5XBzVLBzlPBzpRBzhPBzZN"
    "BzRLBzRLBzFKBy1HCjNRFk5sHl54QHuRP2qMS2iYIDVeHi1bHy1cGy5bGC9gHDRlHjlnIUFoJUpr"
    "Jk5uLlJ7EiI7LWeBS3CvQ2mwWIK/ZZTJVoW3Di06ZitKZiJHHFRlZLPYYIrHX5LKf5zMkp3KjZS6"
    "j5WxnJ6uoKCth5WyYIW0VHu2aI7DiqrQq7zOp7PEubu7wMC7qb/RjrbjjLPfkbTcl7nhpsnoVcXL"
    "O36ycIzIuMTjotDqk8Piq8XficzXNI6kKG2DGERRJ0dQEjA4NovCNojAMHirLWWTI052EkBkDUBd"
    "CjpSCjxUBzlRBjZNBjVMBzRLBzJKBzFKCDFKCDVPJGuEbq/GbJSoNFp+Mkh2Hi5bHy9dGy9fHDRj"
    "HzxqIU11Jlp7Klx+Kl5/PHWbLTtfIyk8UYyzWXrFZpTHaJzLU4exCy45cDJNbSdGIGd3YbXaXYPD"
    "W47JcpTJkJvJi5O7jZKxkZiwoqe1oKOxnaS9e5nFWIC6V3u0eJrHnr3jnLvfjLXgiLXplLjfl7rf"
    "m77gncHhpsblkLncSXarOXCkTJi/jLvjeKvbha7WntLbPZSoJmqADjtHIEBKFzQ8Pny7PYK9PovA"
    "OYa4M3WkKVeCFUJoD0RiCj1WCD1UBjlQBzdNBzVMBjdNBzNMBzFJBzdRGlt3XJuyjK3DPGSHQ12P"
    "ITJgIDZjHzZnHjllIEVxI1R5IklpHVBrJF57PYGsQm2aMxMsQG5/bqbaZ5TIZ53LZpnIE0JSZzNI"
    "jzlNRXqDU7TbXX7CXY7KZ5LNh5nHh4+4houyho6xZG6GXmF0p6/JoK7LeaHQZI3BT3WrZYa1hqfR"
    "g6nVhKbOe57IcpjDapK/Y43AYpDFa6jVbqLKTIuxLsnKUtfNjcbeosDiqtPgTqCxKGmBCzlFFzlD"
    "GTY+VJTLVY3ISofBQozAPYK5N3mrLFuHFkJqD0VkCTtWBzpTBjhQBzdRBjtTBjlRBzZQCTlUFl14"
    "VJiubZiuL2OEVXWnJzttJTpwK0J5JUBxIkdwIlBxGR07QxxbMilZKzhdKE1mJic5VitFYai2ir7s"
    "YpfIdabYMnCPSjZCpElUUnp/RrbZYoHEVoG8U324VXesYm6VWGOFOkVhFBota3OCpbDBpbHLi6nS"
    "hKXUeqLSW4K2VnqrWX2vU3qtVX6xXIW5aZTFganRpbTasbnesdPsqNfve9DhN9fNNdrFedTRm8vX"
    "WqG0L2+HEj9ODzQ+FDM8VJrPWp7RWJjNU5DHToe+P3myOX+wK1uHFkNsED1gCzFWFTBfCzRaBjVW"
    "BjlZBjtaCjxdDUZrRYqlPIGYLmWHY4u5OFGGKkN/L0mAJURzI0pwK1t8IVJrPCJZkDWrgS6fQhdc"
    "Gg8tLRQnLkhVe87ihsH0bKHPYJrIKkZYo1FRUnF1JJmyLTZbGChMHSdRIStRGyRDHCZBERgrNjlF"
    "pq25o6m5n6HHlZfLh6PWirbjibPeWYK1ZYi5eKHPgqnUjbPZnMfnzdDnzMDhvsvlqtTtn9XwsNXu"
    "tNTibszSKcS8MMC1N46eI2F4E0JUCC85BycvTpLKWZ7TXJ/SVJPMX6TRRHy4Pn61OYWxKFeBF0dy"
    "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"
    "Yq7JW5iyPGqbVHKwMVuJNWSQOGSRTIG1WorDSXm6aIzBgpvCsbDIpKjCn2LYiofxWcbwL6GqOnd+"
    "YHV0VVRXW09YXi01BT9QA1JuCmCEEHOaDnOhFHKhHW6NM6nCevf/js34gqjxdXnKZWynW5bEXIi8"
    "XYW4Woa6kanO3dC77ejR3tvEq8XTq7bYsbLVrK7UsrvWw8vescTkntDtms7tq8vircfcqLnXrM/b"
    "P5ejHlpsFVBbInm4PoLIcpXeYp3mWajnjb3tb5DTK3a1HnqsLZjJLaXXKbnaK7/eLrvdMqvQJYKm"
    "HXWaF2mKEXKLHXmVQ5SyPIejL1yMSmepMG2UMn2dPoOiTYysQ36lSHqvi5rBkZ/CqKrJtLXKuqPW"
    "rIHtcLX7NbDBE2NnY01NkmZjmWRbf2JjDV9zBk9pC1FxDkFhSVRsS2iIGGKPOlqRZHGbkV+WmWGk"
    "Z2ukZ4y9iKHUiJPMd5DKV4O8VYS+pbnR59vB0cq0tLvLt7jQt7jXs7bZsbbesLPcusXgos7rn8/r"
    "odnkltPbmcfVr9LcS6ewG2JtFVBaJIC8LH3CP43UUpzfW6TkZrLmYJPSLna0IXWuLpDEKqTVJ67X"
    "LL3bMMHgOsTjPrvaOrPUNabGKZm2KZOzMouvNoapLVqJQlmeKWWNHnqWHnuXRJSwh63KN4ChkJvD"
    "lZ/FlqHDnqnG0cjatabff6H5ZtTwJpmXY2ZppW9qnnJoooqFQFtgE2V1ClVyQ1ZunF9kkWh2eGCC"
    "XCRhmDl+q1GY3LHQy9fkx9fp6eT1lKXXfozPoqfEYYy1UYK/o7bNw8DBp6/Yvbrar7Tds7jbqrLb"
    "m7/Vwtfgp9LpntroktPZgMHOd7HEoMnWVbm9F3ByFVdcJYa+KH3AOYfNRZHWUZ/eUqfgW6raL32z"
    "HXmtKoe8I57QI6nZK7fZOLLcQbfdN7vdOr7fQsPjPsLhPMLkQL7hSL/iRLHWR5/SNWybHXqTIXqW"
    "I4CajbjVRZm0hJnAoKXKo63LpbrPwcDQsbnOg5TUhMLpOZ6pS3x5sJaPsHx4v5CCd1VJMmZhCENY"
    "ZHiNtH56iml6tKfCl1SZmlOTq6jJzOzyy9XnvcbdzNjk3enxmq/cwcHCvczHXoy5UYu/ka7ep67i"
    "oajZtq/Zn7nbj9PejNzaltrelt3gis3XicbTgbzPaJjDirPSVcfFDoN3DWhcIIO5NI/ENYrIPI7Q"
    "RZrVP5jSP5rKJXyoKZXDNp7RLqDXVrTac8zia9LvNrvxHrLrMbjkRb/fOb7eLb/fLMDiPMfkTcfo"
    "VNHzQoCxInyVKYKeJoqjdLnTWLXMeJ7BsK/QoqvIp6zJeo6yU3qna6TUdavif8D2KKawIoSKh42Q"
    "aWNmWWFpUldnKjYzcX6AwZKQinF4ilWKoYG0w77T9PL2usbadI3Db4S+eo7Djp3MmLPVn7XEvLzG"
    "jabHV4zCW43AkrDcsbferLbZj8ree77Rh8/WfbvOf7fVdaPVd6HUe6DUg6HLeJ7MTcXFCpN4CXJe"
    "F4C2OZTEM4/GMZDJM5LNPJzQMHqsF2uUJZLAOqHbSJ7Rcrvjf9j0jdb2odnxVLroRLzmUsfjOsLg"
    "KsLkLcPoMMLiPb/eUMnsTpPHOoynNJeuMpmsUJyuToqjXo+6do+9XHuuSXmyKWmgU22kc6DUjNf9"
    "kc/0b8DaEIGEAkxfC0liDUpkQ1uF4KeSwpFntJeOfVNqWk6Asszl6vj34uvw2Obu4PH3q8Dkg5jQ"
    "f5XMe6THoK7TjZfReJzTcpHIWIzBV4vClrPemM3fdLDMfLfPeLPIdKTJdZTUtsbXx9faxNjdvNHV"
    "jKvHQ7u/D55+B2xZGoS3IJLELJXGK5TIL5HCLY+8OKHNLXubJ4y5UangZKTejtbwtNr1xcP428z1"
    "wMzteL7kYMblQsTjLLTfYLjqa7vobLPkaMzvVLLdSX+mQn2iOHuxK3W9KWafT3yyXYbHUXKtUnmz"
    "RG+lX3yurMDdfcb4mtf/aL/RBWtqG2x3IF9oNVBXpoxl2ZKhyYx7kG5rakBzaZTGoL7ktcreu9Pl"
    "xOHu4O730uTzi6DUh6TNkazNnKDPiqDTg5/SfZbKkKPTXYnBWIrEha/ZhbfQcqfHeqjGc5/RfJ3U"
    "tMvYk7HVdprMXITEVHC6O7C6D5d8CltUK3mgFnWbIpDBJYawJI7AH3ykFHigM4eiMpG5dLLhibbo"
    "1uD398v27r702r/51r77zcrvYLvnMcjtTdjrZLDlb7DlfafigZ/gXnG6T0ePQUeNHDVkGj5lN2ya"
    "HDlRTWWEk6HFl6HClqHDm6a+ysnansbovNbaa6auSoKZF1ZfPFxRvINOnVsyy4RpxKiOXkBQc3+y"
    "lLzxWniznLLV2vD4x+Tz2+j47/j5p7rdkafNnKzNlJ7NiabYdZ/RiJ3RjpjNdqHTXI/FWonChq3X"
    "hq7UgKjTcJnUY43TWYbSVoDNU3zHUHq/Tmq1PZy7FI+FC1xXJmaMDlBwIY+6G2uQGW2QGXGWB1N4"
    "GGeJP5S9p8bpzcfx99H19cTj9b7J3MLWn7jy29b5ocPvOavnccXslbTniILSk4LQhYXOVYCtUY2x"
    "QoizLmF4J16BNnzDJ01hOk5or7TWtLXSxb7TyMLWy8TL7ObM9PDV6Ojde6m7GV1jqJZp/5tQqmox"
    "uZFxdGFRYWBthq7faoK9W3Guvtzr5fH43ebxwdfyy9nv1OPtorXMmKbOmaXMfKPTlr/juNLoocXp"
    "h7jfXpLBV4jAWonCYpDFYY/RYY7WYYzWXYfQV3/FUHa+SW62RF6vPIS2GaSVDWVdGF+IClF2FF2A"
    "EFZ3ClBzDVyDCluGD2SNVqDP29bt7dP48czw+MvM+9fF+NTMt7XVv8LP5KvkhZTpYIzahMTpd6rj"
    "hbrqksruhOL3Y6PMXp24YKvQR4upSqDiIk9jHDBDoqnMrK/PtLTPwbzSzsTQ2M6+5d7E497MhqG5"
    "O0Zec4Nw8Lh2sYNLXGibXVNSdJGhVnu0Y3m6hKHass/o3ez65OjwvtDruMvoutLlprfQnKrQlqjM"
    "iKfNoN/stPj2s/T0tOnwn87hZZTEVIO7WYXJWYLTWIDRU3rOUHbITXHBTW68T263S2W0QXK1Ha2i"
    "EHxuCleECliDCVZ7Cll9CVqACmKMC1yGFG2bXZbK28rh6tL778jr+9TL9/zl/fbs5bDLxbfW8sPz"
    "dsLxK7vhSrnofbDkh7Tmi7jqXsrvUq7ZVpy0aq7KabrHSpHBIk93FC4/jZq8trbWs7PMvLbRwLXZ"
    "v73Xv8O/0tK9eIeqazJbdURGYVE9b1U8W268mpyeUnWcY3vAkKLkdZrYutPpy+j25e/1xdLpzd7w"
    "pL3dmKzPkqvQip/Hgr3Tb8vaeM7fhtvlj97lqerso9zpWInASnW/TXXGT3TJT3TJUHTEUHPAT2+6"
    "Tmu2RWKwQmOtLqKzGZKSClqNC12PC16JCWCGCF6CC2KLC2CHDFqES3unzcPn6cX06cTq+srk/Oni"
    "/+Xq0bDsusj29eb5eLLiTczuQ7rmQrLaJLfgKMDnUNLuo46sXJSuXKi+Yp24gK/BNVpsBx0xOldz"
    "j5e2wL/YzMTa0MbZzMbbmsDhhb7lP1F5TTllhTxWYzxIIh8iP3GvVHqSR2GRfJbXhJzcaYi9l6zJ"
    "gqTHtr3U2ObwzN7wpb/fjqHQ0NXjytfqlsvcUa7EUK/GaMLUccfWd8nWkNzhjsncSni8Qmi5Sm6/"
    "TXLFTHLDSWu6Smi1Sme1R2ezTGWxO6G+HaChCVuNDWGTDmKNCl+FBll8BV6DEXCZFmuUQY+4prbg"
    "2L3u4bjh07bx6MDv7b/lrLX0wOH86ez1ZqXYFZjTI6PZIKjVJbXlFr7uKcfp1pKVloqYQp63Upis"
    "lcLRg8bMKmV7ARgqHC9HgYGgg4WXnp6yzcLRlr3iXZjJRXigYXacUkJ3TCpMISIlHDBMEzxuN1mN"
    "YpDKV32xeYu3rGaapGugvMXe8vf0wtLmor/ovYyh64iJ86GQ4bLDyc3ZiK/CWJ+2U6vBZrnLc8HQ"
    "ktrgb6XOPWC0SGi5SWe3S2y7TG+7Tm65UXC7T3O8VGu7RaTDIK+sGmmdEF+REWGNEWWLFHCWHn6p"
    "I4avHI63O5/IdKLPmKvg4bjlzarhp7/6uL/wn7Px0uH3t9TsQJ7UJKzTHbDXCLXXXbXjwa7yWMrv"
    "icbIlLi5Nay+YKDBgL3Ni8jOX7jOM1d3ABYmCQ4iDAweER4pcn6Xv87iT3WgR4GoT4KtUoCqOE96"
    "Eh0lAwMEFCtRK05+RG2nbYy5bo6yw1ybxmKbmLTR5/P6sL7dy9nz89fK77uM8IVQ4Gt70pS85LXI"
    "lYyjXJm0Vqe+WKvAbLrKic3XV3/BQV+yRWGvSWSwUXG6UnK4UnK3UnO4U2u1T5PAK8jFJZbJHom6"
    "GX6nIYquKJG5IZG6HpzHIJ3JL5zGRYitWpjMiaPYrp7Wiq7sstv0jMHth8DicLTfP5/UKbHYHbHX"
    "EbbYObng3qvw27Lzpq/hlqXCoa7c4ajkfrHFkMnPXbnJh6vWQFdsABAeBAIKCxAXKj1TtsrdZW+Z"
    "P2uXVI6zT4+2R3anLkxyCREaAgcQKUJpSH+ySGafZpC6bpC/iJ27w9LeztflhpbP0t/u8f//foal"
    "mWdnzG50mEx1qmSCcW6KY4Kba4uoWIqoS522b77JYpjCRV+vSGGsUGuzVXK2VnGyWXO0WHSzW3O3"
    "VX+2IXd7OqXSRMDkP77hNbfdLLXbI7PdH6nVIaLLJIutMoKfNoOsQ4e6YIG3WqLWj8/nQb3jacvm"
    "TqnbX7HZK6fOGarQILbYILnbm63q56bw7qfx8qTv16Dgz6Xbcqm+iL3GYb3DcazYMUBOAxQhAw0b"
    "ChAVGzA/cYquXWGNRlR9QXCXPWiMOFyGPVyPPlWHFxg1NFJ6WJnUVG2qeJDChajoucjw7vn95Ojv"
    "cYS4usfdgJq6XYOzTFiGVlB5YmOMS1N8PUpyRVR2S1x5YnWSiLbKUqa6Uoy4X2OxVGWwVXS4WnO1"
    "Yny+aYbJaojLW3m3FylFBhAlKVWMOXmhY6DGZaLRW6nUVKvWP6/WIZWzKIiiHnyZHGiHIW+YJ2+e"
    "SajJgsrgZrbQXrPRQanVO6/VNK3RLq/SLrbXLrndUMDe3bDo7aDt9ajt457h5rDnY6W2da+6Z8LD"
    "X6zQFiw3AQMIDhsqBRMWKj5PVXiiSFuIWld7OFWCMUp6MEZvKz1tK0F7GydlMEyIWJDIXHaxg6nd"
    "mK3zrMvytNPw7fr8jJioGytNIDBTOk52fY6vcYCqanmiaHicSFJ/MTlpKTdlYVRrwZ+hUKC0UIO4"
    "TWGtUW21XXq7Z4HAf5fUkqXbpLPiip7HBhcnChwuK1aDJVKHUnuuc5fLaY/CjpG7u7PVcLLTGX6Z"
    "DGN+E2F/F2mMEWeMG5m8VcDZY7HTNqXRJabOKKjSKqXPJ6rQKLLVLLbcKcDdo9Ln4aXt8Z7v7Zve"
    "lrTLPaCqd6u4asLBXLPNL1VpCx4gBhcXBBMVS2OLT22ZRlqFUGKORluKQWGQNU17HCZfOT9za2+Q"
    "UWyXUXiza4HAi6riuNDnrtvmtdjw1O/6y9viICdJODlrTkeOZ2Cxc3C9aGiybHasi5q2d4SnUVOA"
    "wHhemYh6O5C0V369UG22VHa7g5TKtrrasbfWsLbWv8Xjs8LlIDVOAxEjJ1B7IE51RG2bZ5DDXoe4"
    "aX6teoOxY469SoyvE153DmB8EWuJEmmHIp2+Rr3cjrLfZ67YI6rPKqrQI6XMIavPJLHVJLfbKL3h"
    "W9HlicndkLLhepStM5edNZamW5WkWKitWLbEUYyqNl9yGTE+PF17S2qVQViDS2GQSm2dRlqPQ2CW"
    "GihePEh6qrvVz9HdcYapQGenWnm2rrfPwcfcr87dor/irr/pYGyaW0eJgnHHuqTwtqXzn5nznZf1"
    "goHkbXi1gIyqy83X09TZrcbYeqfNVnnBUXG5ZITIt7zaztLksr7cpLPWwcnhvMrmJz9ZBBQoFjlc"
    "Gz9iPmKOUHinXIu7UYm8PXuuJWmbNnCdLGqDDFxzEmiGEGiEGpe0QsbhT7jaPLDUMLPVNLDVMq/T"
    "M7XYOb7ePsLjPsnmSNHqLsneJMbdM4yeN4mUPpKdOoCMRpCcVb7FQniWQW+XSHOfQWSSP1iCQlyJ"
    "SWaWPViKRFWPL0R7LDVolqvMm7zMur/NdIWjOXiqT3+xmqnGeoKvg468majYYHirKSNLUDZthWm/"
    "3Lv5kIDETEmeUE+fYGK9hordSmOaLTpsq63E3uHrxtjkpL7dW4TNhJ/Vxszkxs7jvMbgrLfbys/i"
    "vsrfHzhPBhgsBA0kCBw4HDtePmiURnGfS3yuQ4GxKGmUGFZ/H22GFmyAEGaCDmF/DG+KHIijF4qn"
    "DYqnFIqpD3mbD3ebF5atJae7JKm/K7/SONTsKsnhG8vlOJevPYWNNoiPNnF9S3uNVKiyY6G+VWaR"
    "QU2QQk2JQFmOP1uOO1OCNUuAMkN/JjVthJe9orzSnLTKvsLTna+/PmyeNE5xKDtSGik5GCU2KTtN"
    "GChBLCtJRShVdFGawIrebVSbRD2CRD6CMipkOzd+WmqmFy9mCBdIa3KWvcPYyNvkosnlrbvdyM3j"
    "yc7iw8rhsr3fzM/jucbZFzBHBxgtChYsECEwEidDKlmBKliAHlB5JmCGIGGEGFF3Fmd/GXOIHIWZ"
    "GIKcFneUFXqVEXaTD2uLC1x+D1+EDl5/GYaRKJKbGJSdM6uufM3ZW6y4I4mmPZGuNoCJMl5rMVBj"
    "Um6Agp6pYqDBpK7Pg4W9TGyrQGWaN1GGNE6BNE6BRmWMc5++j8DVgLO/dpOyX3ShPlWJJDZeJjhE"
    "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"
    "BgsTBAoR"
)

BANNER_ALPHA_DATA = (
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////"
)

PLAIN_BANNER = """
FSHGOOQQQQQQOGHSkmwqkHDHHHHAAShFkwdddbpFGSDzff1lrfxnj>itr~/??\\~<\\lv/}{{{/]1upbFQ
bESADGGGDDGGGGHEdkbnpHDHHHHAASEEHapdpwuAHFAcvclltrrjnxrli~~\\?/<<~~tr\\{([~]<nphFO
mqbFAADDHDDDDGGDEbowmAHHHHASFEhkOpomxcxGEFhljvrlttl1tznv1\\<\\/\\<>>~?1uv?[\\/\\nqSFG
nnaqhSAHHHDDDGGGDplvdhHHHAShbddaFDzncfxGkEdlzjflttri11txnt\\~>><~~\\/<omj<1i?xpHSD
uuxnmbSSHHDDDDDGDkciqqAAASEkEhbumOwrcfcShdarxjcrfcfow<>rvoz11lrfcvvrtxr>\\\\[vpDHH
vjxxuadSSHHDDHDDHkjcpuFSEFEhQHHShDFt~clwFmorzxnuomhKu<<1lrxnnunzc1~\\]]\\ii\\/cwADD
cfcjxoodFADHDDHHHSnopjbEhEEbhHqdDXQE\\~tcEaaxSGDDGGKS>i1rl>>xjr1>/{[]][]]<ttndSGQ
jffvtuuubFASAHHHDEwmzvaFEEkbpbFqadSQSi~iqdmpKESGGXKcifr<i>>xt\\<<~~\\][?};|/ruEHOQ
dmxccrouohFASSHHHFEvrnxSEkbdqxpGmoaodXkuDGqEFjfwQSvtctl~~\\ini/1<><~}}[])){[>mSGQ
hbpwmffonqEFhhFAAAhriazhbdpwaonwuomz1rA@WWHApuovwffctttri~rzi1lil<///~/]][??zhAG
bqpqwmtzoubhEhbkEEdc<anhhbpwoojtqnmzr]!b#BXXpvanvxzvcflltrvj1trr>/\\<<[[[[[<?ckAD
oznwqqutuzmbhEEkdkdz\\oodEkqoujrluxox1]jdhQQKhxvcr11llfambvjv1ft1<>1i[}][[/<[lpAH
vjftfmwozvxpbhEEbdbu~xaakbacufjjxovn<tEdwFDHDXKGExfxaFSqpczcrfiirt1/]}}[/?~/<wFF
nvrt~jwwnvjmpbkbkddmicanbdqvuuxjtxjv<obwFAADFSSGDOGFknfnotzfl<}?1<\\/\\?[??/\\\\/okE
oc~r1>omovvzowpdbdqwrvwudqqnjuvt~izt>zmoddFHFkqqqpv}/1zuvzzzi{!(/~~<\\]?????~[zkE
mnftt~cmmzvfttcawdpwzudmwauxuurl>~<rickduuakFEAdmdpuuxuvltcxx~)]\\\\\\\\\\~???]?\\[cbE
aozct1cawnjvtrlrfvxnnudqpwwz1orl1i]<l~nmzzfdbEdunaFqu?}}!ifijx<?</~\\~~{[]/<1/rph
oanjcttomuzvffttrlllrltvwwma>jti>~?\\t~zolcrqpAncn>uo>|}[}!>?[jz><>~~/?[[\\~>c>1wk
oxnxvjjaxjjr~~rctlrttli<umaoirt~>>cur1<zacmwpAxlxaf?,?cjcl<</1jj>\\~\\>\\>irrrlt1ab
mzxxxjapnvvi??]llilrrrrijnxxvxjcnuqor[?>wSSFp~rlwp[,;|;/ttr>rtcjz</1i1rf?}}]1tok
anxxxnvautt?{]}]>>lf1i1<ruooaqnzouax/~]ibpbkfirndc\\[{(;|lli1lrt1jzi>rltr[>tzucaE
mqnoumwux1>))}]]{1l<l11ludbASwAwl111]/{tuhdcat>kz~n<;)!,\\1>l1rlrrjziilfvzxnnajah
pEuppqEdz?]|}{]~)/f<<cfcnznddohk~\\?[[!:!lkt<nrmwizu}:!}()<iil~]/>vzzvvvvjxuawunk
bEkhEkkbf()((|)\\??rv~1</[tcrxchD><~/[{))rhx?vapvnxl[;!][]~>i1]||(?cxzzznuooomazq
hhhhhbkpc{)()..?/}<tli><>tvl1zhGr\\~\\/??{vkddqurox1t{|;{(\\>il><~?[(]zuuuuuuoawwzo
kkkkkbkhu]}})::?[;iirtft>tvtc1dKdr?[]]\\<bhdkOauwtrjil/|(\\l}}/tti<<[\\umouuaaammjx
kbbkhkppx~][[{{\\(;tnjjffrifjj~<pXDjvl[~coubSOHAdvnvzj[,{\\li\\?]1cf1>[rwaaaooouocj
pbbbpmoujr>]\\/?~){vvvjl\\>~>vf>~lbBBBQx]ounnbK%Dkavvjv<:/()[lf>[fvft1\\xwwmouuuojr
xomonuxxznc1i>{~<1vcvvt?[<1</1\\l1dW%BS[umzzohB#Enmvcr{}t) vncaxuxjzvicwwauuuuunq
vlrtfcjzuounzf/r<flvjcc<???\\\\r>1lFBWBDvmdmwppdQbcoc1[.!j[txqpapkdqu>fzaauuxjvnGB
baftttfnomdqwf~llcfccff1?/[\\[flirG%KBSuqqdkhFEDkjn1<[].tDHbczxndFSqivxmonzt1~lXK
bknfvt\\1mbbddn1lvjvjvcft[//\\>jlirkKXBwapwqqkDhuauzi]{{!(DFdaxuxrjpvcxxout/\\\\[?AB
khmvzxjvxkkddxl>ljvjjcct<\\>cxxjfrzdDpmpwaqqDk\\{jmn~[[\\/odz~~11cxc]}?lnoj/}/<][FB
ASqujzoqmqhddn1rffccfrl1>lruuxoxlamawppmpphSi~/janijfinDhx]cdpofwF<|}\\zl]{[\\{[AX
WKSwauuqkpdbkdaaaaqqujjtirrzuuwoffmddppdkhSt~<?>mkSGOSGHSm1mhhAEoHKu?}?\\{{]/{?DX
XQGbbhddhdqamqwqdkkkmuuv~toxadkatf<cawbkkwt~1cudAAGQXX#GGkzcbpFDEFDGai]/]{{?{/DK
BGGkhFFFFESbaqmaaambmoxr\\rwjmwax\\c>>vrvjr~lubSGOGK#%#WWDODprSGpbSSGwnkc/?\\]]}~OB
#KOhkdwmdEDAFSFhbpapkquxr>japwqartlrjltllohAGQQQQKB#BB#SGXFjkAbdAHDxphkc[rtlltK#
##XDAhdocfjxuwdhEhFEEdmqv>oopbwmfrcczvzubAOXQDDDDDK%XB%FDXHoFXHxaAFxEhbhflvvvcb#
##WXGDHSkuxxzjnamaqFSFAm1jmzvxqwxaxvnvwSDGOSHDSSAhFBQQWHDXGbGBDacaawEEkEdclicvlA
GGGDDDDGASFFEkkbbdqpFHkzomphqtrvmwuuxuSFFAGdpOKAAQXQKX#QDXOFKWXEmovvqFFSEo>czxvS
GHGDSFFGAbdpqqqqqqpqqqaoxfvwEbnrccfzjdKDGQWKqwAOKKKKXW%BGXQDXW#Kbc\\cdFAHSbzjzxcb
WW##KAAODEEhbdpqwwwwwqpdhkuzkhkn\\i1lxaOKQQQBObkBQDKXBB#WGXKKBKBOqpvupAHGHFjfnj1w
W#W%%BGGODHHASFEhkbbbdddpkDwpEkkottfxuwAOKXKBDOKOXXWW##%OXXBSupdpotaFGGOHAxzzuAW
BBBB#WWOOOGDDHAASEEhhhhhhhSHDDGDHSSdaaunnzophGXBW##%%#W%KKBXGAHFhujoQOOQDAuoqKBB
BBBB#BKXGGGGOOOOOQQKKXXBBWWWXQHWKWDkqaaunncroGQ%%%%%%%%%XKBXBOOOSkmbXOKOGSamOKKX
W#####WWWWW###%%%%%%%##WOXXQOODQBdwAEmounnujqODKBBBBBXB%BKBBkoFQSSFGKQQGObuhWB##
####%%%W#%%%%%%%%%##WWWBGQBKKQGOOzuHEkounxnnbOHAAHHHDhH%BKBBkwFKODDGQQOGDntSWWWW
"""


def _is_terminal() -> bool:
    try:
        return os.isatty(sys.stderr.fileno())
    except (AttributeError, ValueError, OSError):
        return False


def _mono_cool(r: int, g: int, b: int) -> tuple[int, int, int]:
    """Desaturate to near-monochrome with slight cool blue tint."""
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
    new_h = 0.6 + (h - 0.6) * 0.15
    new_s = s * 0.12
    new_v = v * 0.85
    nr, ng, nb = colorsys.hsv_to_rgb(new_h % 1.0, min(1.0, new_s), min(1.0, new_v))
    return int(nr * 255), int(ng * 255), int(nb * 255)


def _render_color_banner() -> str:
    try:
        rgb = base64.b64decode(BANNER_RGB_DATA)
        alpha = base64.b64decode(BANNER_ALPHA_DATA)
    except Exception:
        return PLAIN_BANNER

    expected_rgb = BANNER_WIDTH * BANNER_PIXEL_HEIGHT * 3
    expected_alpha = BANNER_WIDTH * BANNER_PIXEL_HEIGHT
    if len(rgb) != expected_rgb or len(alpha) != expected_alpha:
        return PLAIN_BANNER

    lines: list[str] = []
    char_h = BANNER_PIXEL_HEIGHT // 2
    for row in range(char_h):
        parts: list[str] = []
        for col in range(BANNER_WIDTH):
            top_idx = (row * 2 * BANNER_WIDTH + col) * 3
            bot_idx = ((row * 2 + 1) * BANNER_WIDTH + col) * 3
            top_a = row * 2 * BANNER_WIDTH + col
            bot_a = (row * 2 + 1) * BANNER_WIDTH + col

            tr, tg, tb = _mono_cool(
                rgb[top_idx], rgb[top_idx + 1], rgb[top_idx + 2]
            )
            br, bg, bb = _mono_cool(
                rgb[bot_idx], rgb[bot_idx + 1], rgb[bot_idx + 2]
            )
            ta = alpha[top_a]
            ba = alpha[bot_a]

            if ta < 30 and ba < 30:
                parts.append(" ")
            elif ta < 30:
                parts.append(f"\033[38;2;{br};{bg};{bb}m\u2584\033[0m")
            elif ba < 30:
                parts.append(f"\033[38;2;{tr};{tg};{tb}m\u2580\033[0m")
            else:
                parts.append(
                    f"\033[38;2;{tr};{tg};{tb};48;2;{br};{bg};{bb}m\u2580\033[0m"
                )
        lines.append("".join(parts).rstrip())

    return "\n".join(lines)


def _version_label() -> str:
    try:
        from pirebok._version import version
        return f"pirebok {version}"
    except Exception:
        return "pirebok"


def banner() -> str:
    """Return the banner string (colored if terminal, plain otherwise)."""
    label = _version_label()
    pad = max(0, (BANNER_WIDTH - len(label)) // 2)
    suffix = " " * pad + label
    if _is_terminal():
        return _render_color_banner() + "\n" + suffix
    return PLAIN_BANNER + suffix
