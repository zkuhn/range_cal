import persist as p

def test_save():
    
    mapper = p.CalibrationMapper()
    mapper.persist("555", 7.0, 46.2, [(24,56), (25.5, 58)] )
    
    data = mapper.load_calibration("555")
    
    print(data)
    
    assert data['A'] == 7.0
    assert data['B'] == 46.2