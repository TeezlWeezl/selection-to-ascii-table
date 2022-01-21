import win32clipboard as clp
from prettytable import PrettyTable
import sys

def genTable(data):

  data = data.replace('\r','').replace('·', ' ').replace('#', ' # ').split('\n')
  data = [line.split('#') for line in data]
  data = [[col.strip() for col in row] for row in data]

  tbl = PrettyTable()
  tbl.hrules = True
  tbl.field_names = data[0]
  for i, row in enumerate(data):
    if i == 0:
      continue
    tbl.add_row(data[i])

  return tbl

clp.OpenClipboard()
clp.EmptyClipboard()
clp.SetClipboardText(genTable(sys.argv[1]).get_string(), clp.CF_TEXT)
clp.CloseClipboard()