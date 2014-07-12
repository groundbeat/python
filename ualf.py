from pandas import read_csv;
ualf_file = "c:\\_data\\2013.06.ualf";
ualf_header = ['ualf_version','net_type','year','month','day','hour','minute','second','nanosecond','latitude','longitude','altitude','peak_current','rnp','multiplicity','sensors','dof','eangle','emajor','eminor','chi','rise','ptz','slope','icloud','iangle','isignal','itime'];
ualf_data = read_csv(ualf_file,sep='\t',header=None,names=ualf_header);
