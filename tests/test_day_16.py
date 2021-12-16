import pytest

import day_16.main as day16


@pytest.mark.parametrize("transmission, binary_transmission", [
    ("D2FE28", "110100101111111000101000"),
    ("38006F45291200", "00111000000000000110111101000101001010010001001000000000"),
    ("EE00D40C823060", "11101110000000001101010000001100100000100011000001100000")
])
def test_convert_transmission_to_binary(transmission, binary_transmission):
    decoder = day16.Decoder(transmission)
    assert decoder.binary_transmission == binary_transmission


@pytest.mark.parametrize("value_binary, expected_value", [
    ("101111111000101000", 2021),
    ("01010", 10),
    ("1000100100", 20),
    ("00001", 1),
    ("00010", 2),
    ("00011", 3),
])
def test_read_literal_value(value_binary, expected_value):
    decoder = day16.Decoder("")
    decoder.binary_transmission = value_binary
    _, value = decoder.read_literal_value(0)
    assert value == expected_value


@pytest.mark.parametrize("transmission, expected_value", [
    ("8A004A801A8002F478", 16),
    ("620080001611562C8802118E34", 12),
    ("C0015000016115A2E0802F182340", 23),
    ("A0016C880162017C3686B18A3D4780", 31),
])
def test_part_1(transmission, expected_value):
    decoder = day16.Decoder(transmission)
    decoder.parse_binary_transmission()
    assert decoder.part_1_answer == expected_value


@pytest.mark.parametrize("transmission, expected_value", [
    ("C200B40A82", 3),
    ("04005AC33890", 54),
    ("880086C3E88112", 7),
    ("CE00C43D881120", 9),
    ("D8005AC2A8F0", 1),
    ("F600BC2D8F", 0),
    ("9C005AC2F8F0", 0),
    ("9C0141080250320F1802104A08", 1),
])
def test_decoder_parse_transmission(transmission, expected_value):
    decoder = day16.Decoder(transmission)
    value = decoder.parse_binary_transmission()
    assert value == expected_value
