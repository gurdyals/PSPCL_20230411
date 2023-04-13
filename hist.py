#!/usr/bin/env python3

########################################################################
# Started writing on October 15, '2015                                 #
########################################################################

########################################################################
##### id(obj), eval(obj), dir(obj), type(obj), str(obj)
########################################################################
######################     Function Definitions   ######################
def print_this(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    print(str([k for k, v in callers_local_vars if v is var][0]) + ": " + str(var))


# Defining Functions
def fib(n):
    """Print a Fibonacci Series up to n."""
    print("Printing a Fibonacci Series up to n")
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, b + a
    print()


# Return a list of Fibonacci List of Numbers instead of Printing it
def fib2(n):  # Return Fibonacci Series up to n
    """Return a list containing the Fibonacci Series up to n."""
    print("Returning a LIST of Fibonacci Series up to n")
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)  # See Below
        a, b = b, b + a
    print("result : ", result)
    return result


def test_f(fl):
    try:
        result = float(fl)
    except ValueError:
        result = 0.0
    return result


def test_f1(fl):
    if not fl:
        result = 0
    else:
        result = fl
    return float(result)


def CnvDate(Dt):
    result = parse(Dt, ignoretz=True)
    # print ( " CnvDate :", Dt, ":", result, ":", type(result), ":", type(Dt), ":" )
    return result


def prnt_header(row):
    print(
        fmt_str0.format(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
        )
    )
    result = fmt_str0.format(
        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
    )
    return result


def prnt_row(row):
    result = fmt_str1.format(
        row[0],
        str(CnvDate(row[1]).strftime("%a %b %d %H:%M:%S IST %Y")),
        row[2].strip("- "),
        row[3].strip(" -"),
        row[4].strip(" -"),
        row[5].strip("- "),
        test_f(row[6]),
        test_f(row[7]),
        test_f(row[8]),
    )
    print(
        fmt_str1.format(
            row[0],
            str(CnvDate(row[1])),
            row[2].strip("- "),
            row[3].strip(" -"),
            row[4].strip(" -"),
            row[5].strip("- "),
            test_f(row[6]),
            test_f(row[7]),
            test_f(row[8]),
        )
    )
    return result


fmt_str15 = "{0:>5},{1:^28},{3:<13},{5:<31},{6:9.2f},{7:7.2f},{8:7.2f}"


def prnt_row15(row):
    result = fmt_str15.format(
        row[0],
        str(CnvDate(row[1])),
        row[2].strip("- "),
        row[3].strip(" -"),
        row[4].strip(" -"),
        row[5].strip("- "),
        test_f(row[6]),
        test_f(row[7]),
        test_f(row[8]),
    )
    # print( fmt_str1.format( row[0], str( CnvDate(row[1]) ), row[2].strip('- '), row[3].strip(' -'), row[4].strip(' -'), row[5].strip('- '), test_f( row[6] ), test_f( row[7] ), test_f( row[8] ) ) )
    return result

def image_invert(file, path='~/Pictures'):
    sep = '.'
    file_split = file.split(sep)
    file_inverted = file_split[0] + '_inverted' + sep + file_split[1]
    img = Image.open(file)
#####    PIL.ImageOps.invert(img).save('/home/guest/Pictures/266141460_527998739245323_8906606535663857657_n_inverted.jpg')
    PIL.ImageOps.invert(img).save(file_inverted)
    print("sep: ", sep, "file: ", file)
    print("path: ", path)
    print("file_split: ", file_split)
    print('file_inverted: ', file_inverted)
    return file_inverted

def image_test(file, path='~/Pictures'):
    sep = '.'
    file_split = file.split(sep)
    file_BW = file_split[0] + '_BW' + sep + file_split[1]
    print("sep: ", sep, "file: ", file)
    print("path: ", path)
    print("file_split: ", file_split)
    print('file_BW: ', file_BW)
    return file_BW

def image_BW(file, path='~/Pictures'):
    sep = '.'
    file_split = file.split(sep)
    file_BW = file_split[0] + '_BW' + sep + file_split[1]
    img = Image.open(file)
#####    img.convert('L').save('/home/guest/Pictures/266141460_527998739245323_8906606535663857657_n_BW.jpg')
    img.convert('L').save(file_BW)
    print("sep: ", sep, "file: ", file)
    print("path: ", path)
    print("file_split: ", file_split)
    print('file_BW: ', file_BW)
    return file_BW


######################     Function Definitions   ######################
########################################################################

########################################################################
######################     Built-IN Utilities     ######################
import os                               # for OS related utilities     # 5
import argparse                         # for parsing Command line Arguments
import inspect                          # for inspecting variables and program code
import csv                              # 11, 12, 13
import sys                              # 13
import locale                           # 11
import PIL.ImageOps

from datetime import date               # for date related utilities
from datetime import datetime           # for datetime related
from datetime import timedelta          # for timedelta related
from dateutil import parser             # parser for date
from dateutil import relativedelta as rdelta
from dateutil.parser import parse       # 11, 12
from subprocess import check_output     # for Shell Commands
from subprocess import run, call, time  # Importing for hist.py
from sys import argv                    # command line arguments
from PIL import Image

######################     Built-IN Utilities     ######################
########################################################################

########################################################################
########################################################################

if sys.version_info[1] == 9:
    print("SYS.VERSION_INFO := ", sys.version_info)
    #####l1=['bdb', 'csv', 'logging', 'os', 'pdb', 'pathlib', 'subprocess', 'platform', 'importlib', 'datetime', 'pandas', 'numpy', 'PyPDF2']
    import string, black, time, datetime, decimal, fractions, logging, pandas as pd, numpy as np, os, pdb, pathlib, subprocess, platform, camelot, PyPDF2
elif sys.version_info[1] == 10:
    print("SYS.VERSION_INFO := ", sys.version_info)
    import string, subprocess
elif sys.version_info[1] == 11:
    print("SYS.VERSION_INFO := ", sys.version_info)
    import black, string, pandas as pd, numpy as np, subprocess
else:
    print("SYS.VERSION_INFO := ", sys.version_info)

os.chdir("/home/files/PY/Work/")

##### Run an alias in BASH SHELL
##### subprocess.call(["/bin/bash", "-i", "-c", "b2 1s &"])
##### Run an alias in BASH SHELL

##### Increase/Decrease AUDIO Volume command
subprocess.call(
    "pactl set-sink-volume @DEFAULT_SINK@ 90%", shell=True, executable="/bin/bash"
)
##### Increase/Decrease AUDIO Volume command

##### Sleep for 11 Seconds
time.sleep(11)

pd.set_option("display.max_row", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

colspecs = [
    (0, 31),
    (41, 49),
    (49, 55),
    (55, 61),
    (61, 66),
    (66, 70),
    (70, 74),
    (74, 78),
    (78, 82),
    (82, 89),
    (89, 96),
    (96, 101),
    (101, 106),
    (106, 111),
    (111, 117),
    (117, -1),
]  # (117, 124)

df0 = 0
##### df4=pd.read_fwf("R04.txt", header=[0, 1], index_col=None, colspecs=colspecs) ; df4.drop(df4.index[10:], inplace=True) ; df4=df4.fillna(0) ; df4['Seats', 'RES']=(df4['Seats', 'TOT'].astype(int) * 0.15).astype(int) ; df4['ROW']='4'+df4.index.astype(str) ; df4=df4.astype(int, errors='ignore') ; df4.columns ; df4.dtypes ; df4 ;
df4 = pd.read_fwf("R04.txt", header=[0, 1], index_col=None, colspecs=colspecs)
df4.drop(df4.index[10:], inplace=True)
df4 = df4.fillna(0)
df4["Seats", "RES"] = (df4["Seats", "TOT"].astype(int) * 0.15).astype(int)
df4["ROW"] = 40 + df4.index
df4 = df4.astype(int, errors="ignore")
df4.columns
df4.dtypes
df4

df5 = pd.read_fwf("R05.txt", header=[0, 1], index_col=None, colspecs=colspecs)
df5.drop(df5.index[10:], inplace=True)
df5 = df5.fillna(0)
df5["Seats", "RES"] = (df5["Seats", "TOT"].astype(int) * 0.15).astype(int)
df5["ROW"] = 50 + df5.index
df5 = df5.astype(int, errors="ignore")
df5.columns
df5.dtypes
df5

df6 = pd.read_fwf("R06.txt", header=[0, 1], index_col=None, colspecs=colspecs)
df6.drop(df6.index[10:], inplace=True)
df6 = df6.fillna(0)
df6["Seats", "RES"] = (df6["Seats", "TOT"].astype(int) * 0.15).astype(int)
df6["ROW"] = 60 + df6.index
df6 = df6.astype(int, errors="ignore")
df6.columns
df6.dtypes
df6

df7 = pd.read_fwf("R07.txt", header=[0, 1], index_col=None, colspecs=colspecs)
df7.drop(df7.index[10:], inplace=True)
df7 = df7.fillna(0)
df7["Seats", "RES"] = (df7["Seats", "TOT"].astype(int) * 0.15).astype(int)
df7["ROW"] = 70 + df7.index
df7 = df7.astype(int, errors="ignore")
df7.columns
df7.dtypes
df7

df8 = pd.read_fwf("R08.txt", header=[0, 1], index_col=None, colspecs=colspecs)
df8.drop(df8.index[10:], inplace=True)
df8 = df8.fillna(0)
df8["Seats", "RES"] = (df8["Seats", "TOT"].astype(int) * 0.15).astype(int)
df8["ROW"] = 80 + df8.index
df8 = df8.astype(int, errors="ignore")
df8.columns
df8.dtypes
df8

df9 = pd.read_fwf("R09.txt", header=[0, 1], index_col=None, colspecs=colspecs)
df9.drop(df9.index[10:], inplace=True)
df9 = df9.fillna(0)
df9["Seats", "RES"] = (df9["Seats", "TOT"].astype(int) * 0.15).astype(int)
df9["ROW"] = 90 + df9.index
df9 = df9.astype(int, errors="ignore")
df9.columns
df9.dtypes
df9

df10 = pd.read_fwf("R10.txt", header=[0, 1], index_col=None, colspecs=colspecs)
df10.drop(df10.index[10:], inplace=True)
df10 = df10.fillna(0)
df10["Seats", "RES"] = (df10["Seats", "TOT"].astype(int) * 0.15).astype(int)
df10["ROW"] = 100 + df10.index
df10 = df10.astype(int, errors="ignore")
df10.columns
df10.dtypes
df10

df11 = pd.read_fwf("R11.txt", header=[0, 1], index_col=None, colspecs=colspecs)
df11.drop(df11.index[10:], inplace=True)
df11 = df11.fillna(0)
df11["Seats", "RES"] = (df11["Seats", "TOT"].astype(int) * 0.15).astype(int)
df11["ROW"] = 110 + df11.index
df11 = df11.astype(int, errors="ignore")
df11.columns
df11.dtypes
df11

df12 = pd.read_fwf("R12.txt", header=[0, 1], index_col=None, colspecs=colspecs)
df12.drop(df12.index[10:], inplace=True)
df12 = df12.fillna(0)
df12["Seats", "RES"] = (df12["Seats", "TOT"].astype(int) * 0.15).astype(int)
df12["ROW"] = 120 + df12.index
df12 = df12.astype(int, errors="ignore")
df12.columns
df12.dtypes
df12

print("Before pd.concat([")

df = pd.concat([df4, df5, df6, df7, df8, df9, df10, df11, df12])
df.index
df["Category", "SCB CHANNEL Round – 4"] = (
    df["Category", "SCB CHANNEL Round – 4"].fillna("")
    + df["Category", "SCB CHANNEL Round - 5"].fillna("")
    + df["Category", "SCB CHANNEL Round - 6"].fillna("")
    + df["Category", "SCB CHANNEL Round - 7"].fillna("")
    + df["Category", "SCB CHANNEL Round - 8"].fillna("")
    + df["Category", "SCB CHANNEL Round – 9"].fillna("")
    + df["Category", "SCB CHANNEL Round - 10"].fillna("")
    + df["Category", "SCB Revised Round – 11"].fillna("")
    + df["Category", "SCB Round – 12"].fillna("")
)

print("Before df.drop")

df.drop(
    columns=[
        ("Category", "SCB CHANNEL Round - 5"),
        ("Category", "SCB CHANNEL Round - 6"),
        ("Category", "SCB CHANNEL Round - 7"),
        ("Category", "SCB CHANNEL Round - 8"),
        ("Category", "SCB CHANNEL Round – 9"),
        ("Category", "SCB CHANNEL Round - 10"),
        ("Category", "SCB Revised Round – 11"),
        ("Category", "SCB Round – 12"),
    ],
    inplace=True,
)

print("After df.drop")

df.columns
df.dtypes
df

df[("Seats", "RES1")] = ((((df["Seats"]["TOT"] - 3) / 1.05) * 0.15) * 0.75).astype(int)

print("Before df.reset_index")

df.reset_index(drop=True, inplace=True)

print("After df.reset_index")

df

cols = [i for i in df.columns]
cols[0] = ("Category", "SCB CHANNEL Round")
df.columns = pd.MultiIndex.from_tuples(cols)

by = [("Category", "SCB CHANNEL Round"), ("Gen", "Clos"), ("SCc", "Clo")]

by1 = [("Category", "SCB CHANNEL Round"), 'ROW', ("Gen", "Clos"), ("SCc", "Clo")]

df.sort_values(
    by=[("Category", "SCB CHANNEL Round"), ("SCc", "Clo"), ("Gen", "Clos")]
)
df.sort_values(by=by, ascending=False)

print( df.sort_values(by=by1, ascending=True) )

print(by, by1)

##def applycolor(dtF):
##    return ['background-color: lightgreen' if cell_v >=0 else
##    ('background-color: red') cell_v for cell_v in dtF]

##i=df.style.apply(applycolor, subset=df[pd.IndexSlice[df.filter(like="SC").columns]])
i = pd.IndexSlice[df.filter(like="SC").columns]
print(i)

df.filter(like="SC").columns
#####j=df.style.apply(applycolor, subset=df.filter(like="SC").columns)

colspecs = [ (0, 15), (15, 26), (26, 57), (57, -1), ]  # (57, 80)

##### df_email = pd.read_fwf("Shreya_2022_IISERB_roll_no_email.txt", header=[0, 1], index_col=None, colspecs=colspecs)
df_email = pd.read_fwf("Shreya_2022_IISERB_roll_no_email.txt", header=1, index_col=None, colspecs=colspecs)
##### df_email.drop(df_email.index[10:], inplace=True)
##### df_email = df_email.fillna(0)
##### df_email["Seats", "RES"] = (df_email["Seats", "TOT"].astype(int) * 0.15).astype(int)
##### df_email["ROW"] = 120 + df_email.index
df_email = df_email.astype(int, errors="ignore")
df_email.columns
df_email.dtypes
df_email

by2=['Roll_No.', 'Applicant_ID']
df_email1=df_email.sort_values(by=by2, ascending=True)
df_email1['ROW']=df_email1.index
df_email1.reset_index(drop=True, inplace=True)
##### df_email1.drop(columns='index', inplace=True)
df_email1.index ##### ( Output = RangeIndex(start=1, stop=391, step=1) )
df_email1.index=pd.RangeIndex(start=1, stop=391, step=1)
df_email1.drop(df_email1.index[383:], inplace=True)

df_email1

m_str="murmu|Jain|hreya|atel|ingh"
df_email1[df_email1["Candidate's_Name"].str.contains(m_str)]

row=iter( df_email1.values.tolist() )
print(next(row))

print(dir())

##### from PIL import Image
##### file = '/home/guest/Pictures/Shreya_2022_IISERB_TimeTable.jpeg'
##### fl1 = '/home/guest/Pictures/Shreya_2022_IISERB_TimeTable_001.jpeg'
##### img = Image.open(file)
##### img1 = img.convert('L')
##### img1 = img.rotate(270, Image.Resampling.NEAREST, True)
##### img1.save(fl1)


##### subprocess.call(["/bin/bash", "-i", "-c", "b2 1s &"])
subprocess.call(
    "pactl set-sink-volume @DEFAULT_SINK@ 70%", shell=True, executable="/bin/bash"
)

########################################################################
########################################################################

fmt_str0 = "{0:>5},{1:^28},{2:^13},{3:^13},{4:^9},{5:^31},{6:^9},{7:^7},{8:^7}"
fmt_str1 = "{0:>5},{1:^28},{2:<13},{3:<13},{4:<9},{5:<31},{6:9.2f},{7:7.2f},{8:7.2f}"

print("\n\t STANDARD DETAILS\n1. sys.argv \t\t: ", argv, len(argv))
print("2. SYS.EXECUTABLE \t: ", sys.executable)
print("3. SYS.VERSION \t\t: ", sys.version)
print("4. SYS.VERSION_INFO \t: ", sys.version_info)
print("5. SYS.PATH \t\t: ", sys.path)
print('6. SYS OS.ENVIRON["PATH"] \t: ', os.environ["PATH"])
print("7. SYS OS.ENVIRON \t\t: ", os.environ)

print("\n")

if len(argv) == 1:
    print("QUItting as len(argv) == ", len(argv))

elif argv[1] == "1":
    print(argv)
    # 1.)     .         .         .         .         .         .    20190419
    word = "Python"

    print('word="Python"  and result of word[1:]')
    print(word[1:])

    print(
        "repr( word ) := " + repr(word),
        ": repr( type( word )) := " + repr(type(word)),
        ": eval( 'word' ) := " + eval("word"),
    )
    print("rutherhk ")

# 1.)     0         0         0         0         0         0    20190419


elif argv[1] == "0":
    print(argv)
    print(argv, " : This is NOT Yet Ready ")  # DELETE
    pass  # DELETE
# 00.)    .         .         .         .         .         .    10101010

# 00.)    0         0         0         0         0         0    10101010


else:
    print("argv : NOT FIT    > ", argv, "\n")
    w2clist = [
        ("@avarakai", "31 jan 2020"),
        ("@jgopikrishnan70", "19-FEB-2020"),
        ("@governorswaraj", "19 FEB 2020"),
        ("@bababanaras", "19-FEB-2020"),
        ("@AstroAmigo", "19-FEB-2020"),
        ("@RulerOfGods1", "14-jan-2020"),
        ("@nailainayat", "06  jan 2020"),
        ("@RRRRRRRRRR", "7  Jan 2020 "),
        ("@CrimeJuris", "Apr 24, 2020"),
        ("@bluespec", "Apr 24, 2020"),
        ("@RudraVS", "Apr 24, 2020"),
        ("@EducateFwd", "Apr 24, 2020"),
        ("@dabi_tina", "Apr 24, 2020"),
        ("@ubuntu", "Apr 30, 2020"),
        ("@gnome", "Apr 24, 2020"),
        ("@60Minutes", "Apr 24, 2020"),
        ("@KangriCarrier", "Apr 24, 2020"),
        ("@RRRRRRRRRR", "7  Jan 2020 "),
        ("@Indiametdept", "17-jan-2020"),
        ("@swati_gs", "09-DEC-2019"),
        ("@RMCpost", "09-DEC-2019"),
        ("@VashiMant", "09-DEC-2019"),
        ("@BasantPonwar", "Jun 25, 2019"),
        ("@Swamy39", "21-DEC-2019"),
        ("@OfficialDGISPR", "19-DEC-2019"),
        ("@hujodaddy1", "18 may 2018"),
        ("@Vidyut", "24-DEC-2019"),
        ("@sidhant", "17 JUL 2019"),
        ("@AudreyTruschke", "17-DEC-2019"),
        ("@peaceforchange", "17-DEC-2019"),
        ("@Shehla_Rashid", "17-APR-2019"),
        ("@IJaising", "09-FEB-2018"),
        ("@Leopard212", "19-DEC-2019"),
        ("@Snowden", "19-DEC-2019"),
        ("@nitingokhale", "18-DEC-2019"),
        ("@BhaavnaArora", "18-DEC-2019"),
        ("@ANI", "31-DEC-2019"),
        ("@tavleen_singh", "25-DEC-2019"),
    ]
    w2clist.sort(key=lambda pair: pair[0])
    print(w2clist)
    print()
    ordered_list = [i[0] for i in w2clist]
    # print ( ordered_list )
    for i in ordered_list:
        print(i, end=" : ")

    w2clist.sort(key=lambda pair: CnvDate(pair[1]))
    print()
    print(len(w2clist))
    for i in w2clist:
        print("{0:^28} : {1}".format(i[0], CnvDate(i[1]).strftime(" %d %B, %Y - %A")))
    print()


print("\n\t STANDARD DETAILS\n1. SYS.ARGV       : ", argv, ",  # of args :", len(argv))
print('2. SYS OS.ENVIRON :  os.environ["PWD"] := ', os.environ["PWD"])
