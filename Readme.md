#### ZTFMulti-ObjectTool*

*The formal name hasn't been decided yet.

Written by Qinchun Ma & Zhaoxuan Liu from Peking University.

*A brief code help you sort out the cumbersome multi-object metadata downloaded from ZTF.*

You can use it to derive light curves of Zwicky Transient Facility data from Multi-Object Search results.

##### Dependence: Astropy

##### Usage:

Zwicky Transient Facility

https://irsa.ipac.caltech.edu/Missions/ztf.html

-->Catalog Search

-->Select the data release(DR) number

-->Multi-Object Search

-->Upload your multiple object table which is in ASCII.ipac format and choose the search radius

​	You can test your table's validity in https://irsa.ipac.caltech.edu/applications/TblValidator/

​	Details about IPAC format can also be found in the links in this page.

-->Run Query

-->Click on the 'save' bottom. And save the search results in IPAC format.

​	The search results include several light curves for each source. We only need the light curves with the most epochs.

-->Run the list.py to get a sub-list of the search results which only contains only one light curve for every source in each filter.

-->Upload the output list and run Query again in the 'one to one match' mode.

-->Select all and click on the 'To Time Series Tool' bottom.

-->Download the lc.fits and run the multi.py.

​	If you are updating your light curves for new DR, please delete the former ones because we use 'open +a' to write the new lightcurve.txt.

##### Notes

1. For Windows user, you may need to run the following code first to read the ipac type table properly.

   ```python
   ascii.core.TableOutputter.default_converters[0] = ascii.core.convert_numpy(np.int64)
   ```

2. If your table is longer than ~4000, the Light Cure generator may crash down. You may need to separate the table to some sub-tables.
3. Our method is written in the code comments making it easy to rewrite to meet different needs.
