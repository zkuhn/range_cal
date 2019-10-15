import QtQuick 2.5
import QtQuick.Window 2.1
import QtQuick.Controls 1.4

Item{
    
	Button{
	    x: 200
	    width: 200
	    height: 60  
	    text: "Add Sensors to fixtures"
	    onClicked: pageLoader.source = "fixtures.qml" 
	}
}