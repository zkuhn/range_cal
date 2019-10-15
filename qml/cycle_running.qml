import QtQuick 2.5
import QtQuick.Window 2.1
import QtQuick.Controls 1.4

Item{
    
	Label{
	    x: 200 
	    width: 200
	    height: 60
	    text: "Calibration Cycle Running: \n Data will be saved in sensor_data folder, \n and graphs will appear at cycle completion."
	}
	Button{
	    //x: 200 
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