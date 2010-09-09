# Imports
import os
import sys
g = __import__('global')

#Get parameters script from Voinage's tutorial
def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
            params=sys.argv[2]
            cleanedparams=params.replace('?','')
            if (params[len(params)-1]=='/'):
                    params=params[0:len(params)-2]
            pairsofparams=cleanedparams.split('&')
            param={}
            for i in range(len(pairsofparams)):
                    splitparams={}
                    splitparams=pairsofparams[i].split('=')
                    if (len(splitparams))==2:
                            param[splitparams[0]]=splitparams[1]
    return param

# Get torrent or file status icon
def getIcon(isdir,active,complete,p):
	if isdir>1:
		icon = "dir"
		p=p+3
	elif isdir==0:
		icon = "file"
	else:
		icon = "file"
		p=p+3
	if active==1:
		if complete==1:
			iconcol = "green"
		else:
			if p==0: #Don't Download
				iconcol = "red"
			elif p==1: #Normal
				iconcol = "blue"
			elif p==2: #High
				iconcol = "yellow"
			#Now for downloads, not files
			elif p==3: #Idle
				iconcol = "orange"
			elif p==4: #Low
				iconcol = "purple"
			elif p==5: #Normal
				iconcol = "blue"
			elif p==6: #High
				iconcol = "yellow"
	else:
		iconcol = "red"	
	return os.path.join(g.__icondir__,icon+'_'+iconcol+'.png')

# Colour scheme
# Dld & File Completed: Green
# Dld & File P: High  : Yellow
# Dld & File P: Normal: Blue 
# Dld P: Low   : Purple
# Dld Priority: Idle  : Orange
# Dld Stopped & File Don't Download: Red

# Check to see if we can connect to rTorrent. If not ask, to open Settings page. Good practice for first time user experience!
def connectionOK(): 
	#establishing connection
	# TODO: Add checking to make sure it establishes correctly
	#try:
		g.rtc.system.client_version()
	#except:
	#	return False
	#else:
		return True;
#		dialog = xbmcgui.Dialog()
#		ret = dialog.yesno(__language__(30155),__language__(30156),__language__(30157))
#		if ret==True:
#			__addon__.openSettings()
#			connectionOK()
#		else:
#			mode='exit'