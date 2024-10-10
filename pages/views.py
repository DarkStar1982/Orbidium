from django.shortcuts import render
from django.http import JsonResponse
from pages.models import MinorPlanetBody

MAINBELT_ONES = [
    {
        "id": 1,
        "name": "(1) Ceres",
        "flags": "4000",
        "attrs": "0 0 0 0",
        "mag": 3.34,
        "semimajor_a": 2.7666197,
        "radius_a": 2.9856917143248,
        "radius_p": 2.5475476856752,
        "eccentricity": 0.079184,
        "inclination": 10.5879,
        "mean_anomaly": 145.84905,
        "argument_perihelion": 73.28579,
        "asc_node_longitude": 80.25414,
        "mean_daily_motion": 0.21418047
    },
    {
        "id": 2,
        "name": "(2) Pallas",
        "flags": "4000",
        "attrs": "0 0 0 0",
        "mag": 4.11,
        "semimajor_a": 2.7703442,
        "radius_a": 3.40873788489728,
        "radius_p": 2.13195051510272,
        "eccentricity": 0.2304384,
        "inclination": 34.92186,
        "mean_anomaly": 126.06756,
        "argument_perihelion": 10.89226,
        "asc_node_longitude": 72.90614,
        "mean_daily_motion": 0.2137487
    },
    {
        "id": 3,
        "name": "(3) Juno",
        "flags": "4000",
        "attrs": "0 0 0 0",
        "mag": 5.18,
        "semimajor_a": 2.6696851,
        "radius_a": 3.3536231827766803,
        "radius_p": 1.98574701722332,
        "eccentricity": 0.2561868,
        "inclination": 12.98975,
        "mean_anomaly": 82.18651,
        "argument_perihelion": 47.77597,
        "asc_node_longitude": 69.84069,
        "mean_daily_motion": 0.22595087
    },
    {
        "id": 4,
        "name": "(4) Vesta",
        "flags": "4000",
        "attrs": "0 0 0 0",
        "mag": 3.25,
        "semimajor_a": 2.3609252,
        "radius_a": 2.57341106501772,
        "radius_p": 2.14843933498228,
        "eccentricity": 0.0900011,
        "inclination": 7.14399,
        "mean_anomaly": 278.02316,
        "argument_perihelion": 51.67632,
        "asc_node_longitude": 3.70471,
        "mean_daily_motion": 0.27169443
    },
    {
        "id": 5,
        "name": "(5) Astraea",
        "flags": "4000",
        "attrs": "0 0 0 0",
        "mag": 6.99,
        "semimajor_a": 2.5758979,
        "radius_a": 3.05823658490353,
        "radius_p": 2.0935592150964704,
        "eccentricity": 0.1872507,
        "inclination": 5.35914,
        "mean_anomaly": 350.98291,
        "argument_perihelion": 59.23648,
        "asc_node_longitude": 41.46063,
        "mean_daily_motion": 0.23840266
    },
    {
        "id": 6,
        "name": "(6) Hebe",
        "flags": "4007",
        "attrs": "7 0 0 0",
        "mag": 5.61,
        "semimajor_a": 2.425968,
        "radius_a": 2.9172697022304,
        "radius_p": 1.9346662977696,
        "eccentricity": 0.2025178,
        "inclination": 14.73443,
        "mean_anomaly": 196.13462,
        "argument_perihelion": 39.62381,
        "asc_node_longitude": 38.6287,
        "mean_daily_motion": 0.26084137
    },
    {
        "id": 7,
        "name": "(7) Iris",
        "flags": "0000",
        "attrs": "0 0 0 0",
        "mag": 5.64,
        "semimajor_a": 2.3860452,
        "radius_a": 2.93449653897708,
        "radius_p": 1.8375938610229197,
        "eccentricity": 0.2298579,
        "inclination": 5.51948,
        "mean_anomaly": 314.75784,
        "argument_perihelion": 45.52013,
        "asc_node_longitude": 59.49897,
        "mean_daily_motion": 0.2674152
    },
    {
        "id": 8,
        "name": "(8) Flora",
        "flags": "0000",
        "attrs": "0 0 0 0",
        "mag": 6.61,
        "semimajor_a": 2.2010095,
        "radius_a": 2.5456444479138,
        "radius_p": 1.8563745520862,
        "eccentricity": 0.1565804,
        "inclination": 5.89031,
        "mean_anomaly": 78.15445,
        "argument_perihelion": 85.42967,
        "asc_node_longitude": 10.84574,
        "mean_daily_motion": 0.30183611
    },
    {
        "id": 9,
        "name": "(9) Metis",
        "flags": "0000",
        "attrs": "0 0 0 0",
        "mag": 6.34,
        "semimajor_a": 2.3857311,
        "radius_a": 2.6787024576766503,
        "radius_p": 2.09275974232335,
        "eccentricity": 0.1228015,
        "inclination": 5.5782,
        "mean_anomaly": 38.92985,
        "argument_perihelion": 5.72797,
        "asc_node_longitude": 68.86899,
        "mean_daily_motion": 0.26746801
    },
    {
        "id": 10,
        "name": "(10) Hygiea",
        "flags": "0000",
        "attrs": "0 0 0 0",
        "mag": 5.64,
        "semimajor_a": 3.1413261,
        "radius_a": 3.48826546325796,
        "radius_p": 2.79438673674204,
        "eccentricity": 0.1104436,
        "inclination": 3.83162,
        "mean_anomaly": 145.93643,
        "argument_perihelion": 12.63001,
        "asc_node_longitude": 83.14844,
        "mean_daily_motion": 0.17702497
    },
    {
        "id": 11,
        "name": "(11) Parthenope",
        "flags": "0000",
        "attrs": "0 0 0 0",
        "mag": 6.73,
        "semimajor_a": 2.4533692,
        "radius_a": 2.6973150596635995,
        "radius_p": 2.2094233403364,
        "eccentricity": 0.099433,
        "inclination": 4.63153,
        "mean_anomaly": 71.50262,
        "argument_perihelion": 96.07085,
        "asc_node_longitude": 25.50589,
        "mean_daily_motion": 0.25648366
    },
    {
        "id": 12,
        "name": "(12) Victoria",
        "flags": "0000",
        "attrs": "0 0 0 0",
        "mag": 7.3,
        "semimajor_a": 2.3341276,
        "radius_a": 2.84810436482208,
        "radius_p": 1.82015083517792,
        "eccentricity": 0.2202008,
        "inclination": 8.3741,
        "mean_anomaly": 271.07526,
        "argument_perihelion": 69.56953,
        "asc_node_longitude": 35.35583,
        "mean_daily_motion": 0.27638673
    },
    {
        "id": 13,
        "name": "(13) Egeria",
        "flags": "0000",
        "attrs": "0 0 0 0",
        "mag": 6.91,
        "semimajor_a": 2.5762429,
        "radius_a": 2.7966183244060603,
        "radius_p": 2.35586747559394,
        "eccentricity": 0.0855414,
        "inclination": 16.53658,
        "mean_anomaly": 257.49816,
        "argument_perihelion": 79.64431,
        "asc_node_longitude": 43.20753,
        "mean_daily_motion": 0.23835477
    },
    {
        "id": 14,
        "name": "(14) Irene",
        "flags": "0000",
        "attrs": "0 0 0 0",
        "mag": 6.54,
        "semimajor_a": 2.5896652,
        "radius_a": 3.01183785920092,
        "radius_p": 2.1674925407990795,
        "eccentricity": 0.1630221,
        "inclination": 9.12907,
        "mean_anomaly": 278.47409,
        "argument_perihelion": 98.05015,
        "asc_node_longitude": 86.01014,
        "mean_daily_motion": 0.23650409
    },
    {
        "id": 15,
        "name": "(15) Eunomia",
        "flags": "0000",
        "attrs": "0 0 0 0",
        "mag": 5.41,
        "semimajor_a": 2.6439524,
        "radius_a": 3.1399155670015997,
        "radius_p": 2.1479892329984,
        "eccentricity": 0.187584,
        "inclination": 11.75582,
        "mean_anomaly": 21.74829,
        "argument_perihelion": 98.76876,
        "asc_node_longitude": 92.88875,
        "mean_daily_motion": 0.22925754
    },
    {
        "id": 16,
        "name": "(16) Psyche",
        "flags": "0000",
        "attrs": "0 0 0 0",
        "mag": 6.21,
        "semimajor_a": 2.9230625,
        "radius_a": 3.3152945184812497,
        "radius_p": 2.53083048151875,
        "eccentricity": 0.1341853,
        "inclination": 3.09697,
        "mean_anomaly": 282.49326,
        "argument_perihelion": 29.50764,
        "asc_node_longitude": 50.02098,
        "mean_daily_motion": 0.19721817
    },
    {
        "id": 17,
        "name": "(17) Thetis",
        "flags": "0000",
        "attrs": "0 0 0 0",
        "mag": 7.93,
        "semimajor_a": 2.4705496,
        "radius_a": 2.7971723156924004,
        "radius_p": 2.1439268843076,
        "eccentricity": 0.1322065,
        "inclination": 5.5924,
        "mean_anomaly": 91.43731,
        "argument_perihelion": 35.68951,
        "asc_node_longitude": 25.53228,
        "mean_daily_motion": 0.25381291
    }
]
# Create your views here.

def asteroids(request):
    if request.method == 'GET':
        return render(request, "pages/asteroids.html", {})

    if request.method == 'POST':
        return render(request, "pages/asteroids.html", {})

def api(request):
    # load from DB
    asteroid_list = []
    subset = request.GET.get('subset', None)
    resultset = None
    if subset == 'mba':
        return JsonResponse({"pha":[],"mba":MAINBELT_ONES}, safe=False)
    if subset == 'pha':
        resultset = MinorPlanetBody.objects.filter(attributes__contains='>1km PHA')
    if subset == 'nea':
        resultset = MinorPlanetBody.objects.filter(attributes__contains='NEO')
    if subset == 'kbo':
        resultset = MinorPlanetBody.objects.filter(radius_p__gte=30.33, radius_a__lte=55.0)
    if subset == 'sdo':
        resultset = MinorPlanetBody.objects.filter(radius_p__gte=30.33, radius_a__gte=55.0)
    if subset == 'dto':
        resultset = MinorPlanetBody.objects.filter(radius_p__gte=55.00)
    if subset == 'cnt':
        resultset = MinorPlanetBody.objects.filter(radius_p__gte=5.45, radius_a__lte=30.0)
    if subset == 'all':
        resultset = MinorPlanetBody.objects.all()
    # resultset = MinorPlanetBody.objects.filter(radius_a__gte=200.0)

    for x in resultset:
        obj_data = {}
        obj_data["id"] = x.asteroid_id
        obj_data["name"] = x.asteroid_name
        obj_data["flags"] = x.flags_short
        obj_data["attrs"] = x.attributes
        obj_data["mag"] = x.magnitude
        obj_data["semimajor_a"] = x.semimajor_a
        obj_data["radius_a"] = x.radius_a
        obj_data["radius_p"]= x.radius_p
        obj_data["eccentricity"] = x.eccentricty
        obj_data["inclination"] = x.inclination
        obj_data["mean_anomaly"] = x.mean_anomaly
        obj_data["argument_perihelion"] = x.argument_perihelion
        obj_data["asc_node_longitude"] = x.asc_node_longitude
        obj_data["mean_daily_motion"] = x.mean_daily_motion
        asteroid_list.append(obj_data)
    return JsonResponse({"pha":asteroid_list,"mba":[]}, safe=False)