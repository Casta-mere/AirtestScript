#$language = "VBScript"
#$interface = "1.0"

crt.Screen.Synchronous = True

Sub Main
	While 1
	crt.Screen.WaitForString "GetSN end true"
	crt.sleep 2000
	crt.Screen.Send chr(13)
	crt.sleep 1000
	crt.Screen.Send "root" & chr(13)
	crt.sleep 1000
	crt.Screen.Send "fCdJMZLZ+GU4" & chr(13)
	crt.sleep 1000
	crt.Screen.Send "tail -f  /tmp/closelicamera.log"
	WEnd
End Sub
