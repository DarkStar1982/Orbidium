from django.core.management.base import BaseCommand, CommandError
import argparse
import urllib.request
import os
from pages.models import MinorPlanetBody 

URL_PATH = "https://www.minorplanetcenter.net/iau/MPCORB/MPCORB.DAT"
FILE_PATH = 'MPCORB.DAT'

class Command(BaseCommand):
    help = 'Add all asteroids'

    def unpack_epoch(self, packed):
        unpacked_year_prefix = {'I':'18', "J":'19', "K":'20'}
        unpacked_month_day = { 
            '1':'01','2':'02', '3':'03', '4':'04', '5':'05', '6':'06', '7':'07', '8':'08',
            '9':'09', 'A':'10', 'B':'11', 'C':'12', 'D':'13', 'E':'14', 'F':'15', 'G':'16',
            'H':'17', 'I':'18', 'J':'19', 'K':'20', 'L':'21', 'M':'22', 'N':'23', 'O':'24',
            'P':'25', 'Q':'26', 'R':'27', 'S':'28', 'T':'29', 'U':'30', 'V':'31'
        }
        year = packed[0]
        month = packed[3]
        day = packed[4]
        unpacked = unpacked_year_prefix[year]+packed[1:3]+unpacked_month_day[month]+unpacked_month_day[day]
        return unpacked

    def parse_flags(self, str_flag):
        families = ['','Atira', 'Aten', 'Apollo', 'Amor', 'q<1.665', 'Hungaria', '', 'Hilda', 'Jupiter Trojan', 'Distant Object']
        str_flax = "%s%s" % ("0x", str_flag)
        hex_value = int(str_flag, 16)
        family = hex_value & 0x00FF
        is_neo = (hex_value & 0x0800)>>11
        is_large_neo = (hex_value & 0x1000)>>12
        is_pha = (hex_value & 0x8000)>>15
        if is_neo>0:
            neo_flag = 'NEO'
        else:
            neo_flag = ''
        if is_large_neo>0:
            large_neo = '>1km'
        else:
            large_neo = ''
        if is_pha>0:
            pha = 'PHA'
        else:
            pha = ''
        return ("%s %s %s %s" % (families[family], neo_flag, large_neo, pha))


    def parse_line(self, str_line):
        values = str_line.split()
        if len(values)<1:
            return None
        mpc_description = {
            'id': str_line[0:7], # just a numerical id
            'H': str_line[9:13], # absolute magnitude H
            'G': str_line[15:19], # slope parameter G, ignore it
            'Epoch':self.unpack_epoch(str_line[20:25]), #unpack_epoch(values[3]),
            'M':str_line[26:35], # Mean anomaly at epoch
            'P':str_line[38:46], # Argument of perihelion, J2000.0 (degrees) 
            'N':str_line[49:57], # Longitude of the ascending node, J2000.0 (degrees)
            'I':str_line[60:68], # Inclination
            'E':str_line[70:79], # Eccentricity
            'D':str_line[81:91], # Mean daily motion (degrees per day)
            'A':str_line[92:103], # semi-major axis in au, A
            'U':str_line[105], # Uncertaity?
            'R':str_line[107:116], # Reference
            'O':str_line[118:122], # number of observations
            'OPP':str_line[123:126], # number of oppositions of observation arc 
            'ARC':str_line[127:136], # Observartion arc
            'RMS':str_line[137:141], # Residual error
            'PRT1':str_line[142:145], # perturbations, coarse
            'PRT2':str_line[146:149], # perturbations, precise
            'COMP':str_line[150:158], # perturbations, precise
            'FLAG':str_line[161:165], #
            'NAME':str_line[166:194],
            'DATE':str_line[194:202]
        }
        return(mpc_description)

    def add_mpc(self, p_data_line, p_id):
        if p_data_line is None:
            return
        mpc = MinorPlanetBody()
        mpc.asteroid_id = p_id
        mpc.asteroid_name = p_data_line["NAME"].lstrip().rstrip()
        mpc.flags_short = p_data_line["FLAG"]
        mpc.attributes = self.parse_flags(p_data_line["FLAG"])
        if p_data_line["H"].lstrip().rstrip() =='':
            return
        else:
            mpc.magnitude = p_data_line["H"].lstrip().rstrip()
        mpc.semimajor_a = p_data_line["A"]
        mpc.eccentricty = p_data_line["E"]
        mpc.inclination = p_data_line["I"]
        mpc.radius_a = float(mpc.semimajor_a)*(1.0+float(mpc.eccentricty))
        mpc.radius_p = float(mpc.semimajor_a)*(1.0-float(mpc.eccentricty))  
        mpc.mean_anomaly = p_data_line["M"]
        mpc.argument_perihelion = p_data_line["P"]
        mpc.asc_node_longitude = p_data_line["N"]
        mpc.mean_daily_motion = p_data_line["D"]
        mpc.save()

    def read_file(self):
        print ("Processing a file into the DB...")
        f = open(FILE_PATH)
        x = 0
        while x<43:
            x = x + 1
            f.readline()
        line = f.readline()
        i = 0
        while line:
            data_line = self.parse_line(line)
            self.add_mpc(data_line, i)
            # insert_data(data_line, cursor)
            line = f.readline()
            i = i + 1

    # create mpc record
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting procesing...'))
        url = URL_PATH
        file_name = FILE_PATH
        if os.path.exists(file_name):
            print ("File already exists, skipping download!")
        else:
            print ("Downloading file from MPC database website...")
            urllib.request.urlretrieve(url, file_name)
        self.read_file()
        self.stdout.write(self.style.SUCCESS('Ending processing...'))