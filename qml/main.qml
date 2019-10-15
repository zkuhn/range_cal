import QtQuick.Window 2.1
import QtQuick 2.5
import QtQuick.Controls 1.4

Window {
    id: win
    width: 600
    height: 400
    visible: true
    property int menuHeight: 150
    Rectangle{
        width:600
        height: menuHeight
	    Image{
	        source: "SAI-logo-over-dark.png"
	    }
    }
    Rectangle{
        width: parent.width
        height: parent.height - menuHeight
        x:0
        y:menuHeight
	    Item{
	        Loader { 
	            id: pageLoader 
	            anchors.fill: parent
	            source: "page.qml"
				onLoaded: {
		            ui_control.loader_changed(pageLoader.source)	
				}
	        }
	    }
    }
}
    