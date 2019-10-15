import QtQuick.Controls 2.5
import QtQuick 2.13

Item{
	Rectangle {
	
	    x: 0
	    y: 0
	    width: 600
	    height: 400
	    color: "grey"
		Label {
		    x: 10
		    y: 10
		    text: "Fixture 1 serial number:"
		}
		TextField{
		    id: fixture1
		    x: 210
		    y: 10
			text: ""
		}
		Label {
		    text: "Fixture 2 serial number:"
		    x: 10
		    y: 60
		}
		TextField{
			id: fixture2
			text: ""
			x: 210
		    y: 60
		}
		Label {
		    text: "Fixture 3 serial number:"
		    x: 10
		    y: 110
		}
		TextField{
			id: fixture3
			text: ""
			x: 210
		    y: 110
		}
		Button{
			text: "done"
		    x: 210
		    y: 160
		    // x: 100
		    width: 200
		    height: 60
		    onClicked: {
		    	ui_control.set_fixture_mapping(fixture1.text, fixture2.text, fixture3.text)
		    	pageLoader.source = "start_cycle.qml"
		    }
		}
	}
}