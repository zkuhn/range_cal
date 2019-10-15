import QtQuick 2.5
import QtQuick.Window 2.1
import QtQuick.Controls 1.4

Item{
    
	Button{
	    x: 200 
	    width: 200
	    height: 60
	    text: "Start Calibration Cycle"
	    onClicked: {
	        pageLoader.source = "cycle_running.qml"
	        ui_control.start_cycle()
        } 
	}
	Button{
	    x: 200
	    y: 100
	    width: 200
	    height: 60
	    text: "Return Home"
	    onClicked: {
	        pageLoader.source = "page.qml"
        } 
	}
}