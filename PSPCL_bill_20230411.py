#!/usr/bin/env python3
#### #!/usr/bin/env python3 -u

#This is started on April 11, '2023

########################################################################
##### id(obj), eval(obj), dir(obj), type(obj), str(obj)
########################################################################
######################     Function Definitions   ######################
def print_this(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    print(str([k for k, v in callers_local_vars if v is var][0])+': '+str(var))

# Defining Functions
def fib(n):
    """Print a Fibonacci Series up to n."""
    print( "Printing a Fibonacci Series up to n" )
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, b+a
    print()

# Return a list of Fibonacci List of Numbers instead of Printing it
def fib2(n):    # Return Fibonacci Series up to n
    """Return a list containing the Fibonacci Series up to n."""
    print( "Returning a LIST of Fibonacci Series up to n" )
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)     # See Below
        a, b = b, b+a
    print( "result : ", result )
    return result

def test_f(fl):
    try:
        result = float( fl )
    except ValueError:
        result = 0.0
    return( result )

def test_f1(fl):
  if not fl:
      result=0
  else:
      result=fl
  return( float( result ) )

def CnvDate( Dt ):
    result = parse( Dt, ignoretz=True ) 
    # print ( " CnvDate :", Dt, ":", result, ":", type(result), ":", type(Dt), ":" )
    return( result )

def prnt_header( row ):
    print( fmt_str0.format( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8] ) )
    result = ( fmt_str0.format( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8] ) )
    return( result )

def prnt_row( row ):
    result = ( fmt_str1.format( row[0], str( CnvDate(row[1]).strftime( '%a %b %d %H:%M:%S IST %Y' ) ), row[2].strip('- '), row[3].strip(' -'), row[4].strip(' -'), row[5].strip('- '), test_f( row[6] ), test_f( row[7] ), test_f( row[8] ) ) )
    print( fmt_str1.format( row[0], str( CnvDate(row[1]) ), row[2].strip('- '), row[3].strip(' -'), row[4].strip(' -'), row[5].strip('- '), test_f( row[6] ), test_f( row[7] ), test_f( row[8] ) ) )
    return( result )

fmt_str15= '{0:>5},{1:^28},{3:<13},{5:<31},{6:9.2f},{7:7.2f},{8:7.2f}'
def prnt_row15( row ):
    result = ( fmt_str15.format( row[0], str( CnvDate(row[1]) ), row[2].strip('- '), row[3].strip(' -'), row[4].strip(' -'), row[5].strip('- '), test_f( row[6] ), test_f( row[7] ), test_f( row[8] ) ) )
    # print( fmt_str1.format( row[0], str( CnvDate(row[1]) ), row[2].strip('- '), row[3].strip(' -'), row[4].strip(' -'), row[5].strip('- '), test_f( row[6] ), test_f( row[7] ), test_f( row[8] ) ) )
    return( result )

######################     Function Definitions   ######################
########################################################################

########################################################################
######################     Built-IN Utilities     ######################
import argparse         # for parsing Command line Arguments
import csv              # 11, 12, 13
import inspect          # for inspecting variables and program code
import locale           # 11
import os               # for OS related utilities     # 5
import sys              # 13

import pandas           as pd
import numpy            as np
import matplotlib       as mlt

from datetime      import date              # for date related utilities
from datetime      import datetime          # for datetime related
from datetime      import timedelta
from dateutil      import parser            # parser for date
from dateutil      import relativedelta as rdelta
from dateutil.parser import parse   # 11, 12
from subprocess    import check_output      # for Shell Commands
from subprocess    import run
from sys           import argv              # command line arguments

######################     Built-IN Utilities     ######################
########################################################################

fmt_str0= '{0:>5},{1:^28},{2:^13},{3:^13},{4:^9},{5:^31},{6:^9},{7:^7},{8:^7}'
fmt_str1= '{0:>5},{1:^28},{2:<13},{3:<13},{4:<9},{5:<31},{6:9.2f},{7:7.2f},{8:7.2f}'

print ( '\n\t STANDARD DETAILS\n1. sys.argv \t\t: ', argv, len(argv) )
print ( '2. SYS.EXECUTABLE \t: ', sys.executable )
print ( '3. SYS.VERSION \t\t: ', sys.version )
print ( '4. SYS.VERSION_INFO \t: ', sys.version_info )
print ( '5. SYS.PATH \t\t: ', sys.path )
print ( '6. SYS OS.ENVIRON["PATH"] \t: ', os.environ['PATH'] )
print ( '7. SYS OS.ENVIRON \t\t: ', os.environ )

print ( "\n" )

if argv[1] == '1':
  print ( argv )
#1.)     .         .         .         .         .         .    20230219
  word="Python"

  print ('word="Python"  and result of word[1:]')
  print ( word[1:] )

  print ( 'repr( word ) := ' + repr( word ), ': repr( type( word )) := ' + repr( type( word ) ), ": eval( 'word' ) := " + eval( 'word' ) )
  print ( "rutherhk ")

#1.)     0         0         0         0         0         0    20230219







elif argv[1] == '2':
  print ( argv )
#2.)     .         .         .         .         .         .    20230219
  if_this_is_true = True
  if if_this_is_true :
      print ("Hey This is True ")

#2.)     0         0         0         0         0         0    20230219








else:
  print ( argv )
#main.)  .         .         .         .         .         .    20230219
  pd.set_option("display.max_row", None)
  pd.set_option("display.max_columns", None)
  pd.set_option("display.width", None)
  pd.set_option("display.max_colwidth", None)

  FileName  = 'PSPCL_bill_20230411.csv'
  PfileName = 'PSPCL_pym_20230413.csv'
  OfileName = 'PSPCL_bill.csv'
  SfileName = 'PSPCL_some.csv'

########################################################################

#####  df_Read = pd.read_fwf("PSPCL_bill_20230411.csv", header=[0, 1], index_col=None, colspecs=colspecs)
  df_Bill = pd.read_csv("PSPCL_bill_20230411.csv", header=[10], index_col=0, nrows=15)
  df=df_Bill.copy()
  id(df), id(df_Bill)

  df.columns
  df.index
  df.index.name
  df.dtypes
  df.info()

  df_index_name=df.index.name

  df.index=[i+1 for i in range(len(df.index))]
  df.index.name=df_index_name

  df.dropna(subset=['Bill No.'], inplace=True)

  cols=[i for i in df.columns]
  df.drop([cols[i] for i in [2, 3, 6, 8, 9, 10, 11, 12, 13, 14, 22, 27, 29, 30, 32]], 1, inplace=True)

  #####  df['Due Date']=pd.to_datetime(df['Due Date'], errors='ignore')
  ##### for i in [0, 1, 4, 5, 6]:
  #####   print(df.columns[i])
  #####   df[df.columns[i]]=pd.to_datetime(df[df.columns[i]], errors='ignore')

  ##### for i in [2, 3, 7, 8, 9, 10, 11, 13, 14, 15]:
  #####   print(df.columns[i])

  res = {}
  for i in [2, 3, 7, 8, 9, 10, 11, 13, 14, 15]:
    print(df.columns[i])
    res = res | {df.columns[i]: 'int64'}

  for i in [0, 1, 4, 5, 6]:
    print(df.columns[i])
    res = res | {df.columns[i]: 'datetime64[ns]'}

  res

  df=df.astype(res, copy=False, errors='ignore')
  df['Actual Bill'] = pd.to_numeric( df['Actual Bill'].str[3:-2], downcast='float')

  cols=['Date Time', 'Due Date', 'Bill No.', 'A/C No.', 'Issue Date', 'New Date', 'Old Date', 'New Units', 'Old Units', 'Tot Units', 'Fixed Chg', 'Energy Chg', 'Rentals', 'Taxes', 'Prev Amt', 'Arrears', 'Allowance', 'Net Bill Amt', 'Actual Bill', 'Pym Hist']

  df.columns=cols


########################################################################

##### df_email.drop(df_email.index[10:], inplace=True)
  df_PYM = pd.read_csv("PSPCL_pym_20230413.csv", header=[10], index_col=0, nrows=9)

  cols=df_PYM.columns
  usecols=cols

  df_PYM.drop(['Bill Cycle/Group', 'Sub Division Name', 'Amount in Words', 'Payment Status'], 1, inplace=True)

  df_PYM['Transaction Date']  = pd.to_datetime( df_PYM['Transaction Date'] )
  df_PYM['Amount Paid']  = pd.to_numeric( df_PYM['Amount Paid'].str[:-2], downcast='float' )

##### df_PYM['Bill Due Date'][:-1]  = pd.to_datetime( df_PYM['Bill Due Date'][:-1], errors='ignore' )

########################################################################




#main.)  0         0         0         0         0         0    20230219







print ("Always executed")
 
if __name__ == "__main__":
    print ("Executed when invoked directly")
else:
    print ("Executed when imported")
