# Imports
import xbmcgui
import xbmcplugin
from functions import *
g = __import__('global')

#Main program code	
def main():
#	addonMenu();
	dlds = []
	dlds = g.rtc.d.multicall('main', "d.get_name=", "d.get_hash=", "d.get_completed_chunks=", "d.get_size_chunks=", "d.get_size_files=", "d.get_directory=", "d.is_active=", "d.get_complete=", "d.get_priority=", "d.is_multi_file=", "d.get_size_bytes=" )
	dlds_len = len(dlds)

	for dld in dlds:
		dld_name = dld[0]
		dld_hash = dld[1]
		dld_completed_chunks = dld[2]
		dld_size_chunks = dld[3]
		dld_percent_complete = dld_completed_chunks*100/dld_size_chunks
		dld_size_files = dld[4]
		dld_directory = dld[5]
		dld_is_active = dld[6]
		dld_complete = dld[7]
		dld_priority = dld[8]
		dld_is_multi_file = dld[9]
		dld_get_size_bytes = dld[10]
		tbn=getIcon(dld_size_files,dld_is_active,dld_complete,dld_priority)		
		
		if dld_is_active==1:
			cm_action = g.__lang__(30101),"xbmc.runPlugin(%s?mode=action&method=d.stop&arg1=%s)" % ( sys.argv[0], dld_hash)
		else:
			cm_action = g.__lang__(30100),"xbmc.runPlugin(%s?mode=action&method=d.start&arg1=%s)" % ( sys.argv[0], dld_hash)
		if dld_percent_complete<100:
			li_name = dld_name+' ('+str(dld_percent_complete)+'%)'
		else:
			li_name = dld_name	

		cm = [cm_action, \
			(g.__lang__(30102),"xbmc.runPlugin(%s?mode=action&method=d.erase&arg1=%s)" % ( sys.argv[0], dld_hash)), \
			(g.__lang__(30120),"xbmc.runPlugin(%s?mode=action&method=d.set_priority&arg1=%s&arg2=3)" % ( sys.argv[0], dld_hash)), \
			(g.__lang__(30121),"xbmc.runPlugin(%s?mode=action&method=d.set_priority&arg1=%s&arg2=2)" % ( sys.argv[0], dld_hash)), \
			(g.__lang__(30122),"xbmc.runPlugin(%s?mode=action&method=d.set_priority&arg1=%s&arg2=1)" % ( sys.argv[0], dld_hash)), \
			(g.__lang__(30123),"xbmc.runPlugin(%s?mode=action&method=d.set_priority&arg1=%s&arg2=0)" % ( sys.argv[0], dld_hash))]	
			
		li = xbmcgui.ListItem( \
			label=li_name, \
			iconImage=tbn, thumbnailImage=tbn)
		li.addContextMenuItems(items=cm,replaceItems=True)		
		if dld_size_files>1:
			if not xbmcplugin.addDirectoryItem(int(sys.argv[1]), \
				sys.argv[0]+"?mode=files&hash="+dld_hash+"&numfiles="+str(dld_size_files), \
				li,isFolder=True,totalItems=dlds_len): break
		else:
			if not xbmcplugin.addDirectoryItem(int(sys.argv[1]), \
				sys.argv[0]+"?mode=play&arg1="+str(dld_complete)+"&url="+urllib.quote_plus(xbmc.translatePath(os.path.join(dld_directory,dld_name))), \
				li,totalItems=dlds_len): break
	xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)