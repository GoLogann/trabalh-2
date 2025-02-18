from maquina_refrigerante import maquina_refri

def test_validate_vending_machine_1() -> None:
    sequence = ("100", "50", "50")
    expected = "101"
    result = maquina_refri.process_sequence(sequence)
    print(f"\nSequence {sequence}: Expected: {expected}, Result: {result}")
    assert result == expected

def test_validate_vending_machine_2() -> None:
    sequence = ("100", "50", "50", "50", "50")
    expected = "10101"
    result = maquina_refri.process_sequence(sequence)
    print(f"\nSequence {sequence}: Expected: {expected}, Result: {result}")
    assert result == expected

def test_validate_vending_machine_3() -> None:
    sequence = ("100", "50", "50", "50", "50", "50", "50", "50", "50", "50")
    expected = "1010101010"
    result = maquina_refri.process_sequence(sequence)
    print(f"\nSequence {sequence}: Expected: {expected}, Result: {result}")
    assert result == expected

def test_validate_vending_machine_4() -> None:
    sequence = ("25", "100", "25", "50")
    expected = "0101"
    result = maquina_refri.process_sequence(sequence)
    print(f"\nSequence {sequence}: Expected: {expected}, Result: {result}")
    assert result == expected

def test_validate_vending_machine_5() -> None:
    sequence = ("100", "100", "50", "50")
    expected = "1111"
    result = maquina_refri.process_sequence(sequence)
    print(f"\nSequence {sequence}: Expected: {expected}, Result: {result}")
    assert result == expected

def test_validate_vending_machine_6() -> None:
    sequence = ("25", "25", "25", "25")
    expected = "0010"
    result = maquina_refri.process_sequence(sequence)
    print(f"\nSequence {sequence}: Expected: {expected}, Result: {result}")
    assert result == expected

def test_validate_vending_machine_7() -> None:
    sequence = ("25", "25", "50", "25")
    expected = "0001"
    result = maquina_refri.process_sequence(sequence)
    print(f"\nSequence {sequence}: Expected: {expected}, Result: {result}")
    assert result == expected