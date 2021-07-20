from astropy.io import ascii


# select the max observation number of light curves
def maxtable(f, list):
    table = f[list]
    now = 0
    newtable = []
    for i in range(len(table['oid']) - 1):
        if table['cntr_01'][i + 1] == table['cntr_01'][now]:
            if table['nobsrel'][i + 1] > table['nobsrel'][now]:
                now = i + 1
        else:
            newtable.append(list[now])
            now = i + 1
    newtable.append(list[now])
    return (newtable)


# For Windows user, you may need to run the following code first to read the ipac type table properly.
#ascii.core.TableOutputter.default_converters[0] = ascii.core.convert_numpy(np.int64)

# read the list. The result catalog format is ascii.ipac.
f = ascii.read('irsa_catalog_search_results_tbl.tbl')

name = f['name_01']
oid = f['oid']
fc = f['filtercode']

# divide the list into different bands
i_list = []
for i in range(len(name)):
    if fc[i] == 'zi':
        i_list.append(i)
table_i = maxtable(f, i_list)

g_list = []
for i in range(len(name)):
    if fc[i] == 'zg':
        g_list.append(i)
table_g = maxtable(f, g_list)

r_list = []
for i in range(len(name)):
    if fc[i] == 'zr':
        r_list.append(i)
table_r = maxtable(f, r_list)

# combine list
ln = table_i + table_g + table_r

# save the new list
ascii.write(f[ln], 'list.tbl', format='ipac', overwrite=True)
# After doing this, you need to upload the list.tbl to the query system and run the query in the "one to on match" Mode.

# If your table is longer than ~4000, the Light Cure generator may crash down. You may need to separate the table
# to some sub-tables.