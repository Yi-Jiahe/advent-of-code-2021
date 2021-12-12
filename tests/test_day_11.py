import day_11.main as day11


def test_step():
    levels = day11.parse_input(str.splitlines("""11111
19991
19191
19991
11111"""))
    # Step 1
    levels, flashes = day11.step(levels)
    assert levels == day11.parse_input(str.splitlines("""34543
40004
50005
40004
34543"""))
    assert flashes == 9
    # Step 2
    levels, flashes = day11.step(levels)
    assert levels == day11.parse_input(str.splitlines("""45654
    51115
    61116
    51115
    45654"""))


def test_part_1():
    total_flashes = 0

    levels = day11.parse_input(str.splitlines("""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""))
    # Step 1
    levels, flashes = day11.step(levels)
    total_flashes += flashes
    assert levels == day11.parse_input(str.splitlines("""6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637"""))
    # Step 2
    levels, flashes = day11.step(levels)
    total_flashes += flashes
    assert levels == day11.parse_input(str.splitlines("""8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848"""))
    # Step 3
    levels, flashes = day11.step(levels)
    total_flashes += flashes
    assert levels == day11.parse_input(str.splitlines("""0050900866
8500800575
9900000039
9700000041
9935080063
7712300000
7911250009
2211130000
0421125000
0021119000"""))
    # Step 4
    levels, flashes = day11.step(levels)
    total_flashes += flashes
    assert levels == day11.parse_input(str.splitlines("""2263031977
0923031697
0032221150
0041111163
0076191174
0053411122
0042361120
5532241122
1532247211
1132230211"""))
    # Step 5
    levels, flashes = day11.step(levels)
    total_flashes += flashes
    assert levels == day11.parse_input(str.splitlines("""4484144000
2044144000
2253333493
1152333274
1187303285
1164633233
1153472231
6643352233
2643358322
2243341322"""))
    # Step 6
    levels, flashes = day11.step(levels)
    total_flashes += flashes
    assert levels == day11.parse_input(str.splitlines("""5595255111
3155255222
3364444605
2263444496
2298414396
2275744344
2264583342
7754463344
3754469433
3354452433"""))
    # Step 7
    levels, flashes = day11.step(levels)
    total_flashes += flashes
    assert levels == day11.parse_input(str.splitlines("""6707366222
4377366333
4475555827
3496655709
3500625609
3509955566
3486694453
8865585555
4865580644
4465574644"""))
    # Step 8
    levels, flashes = day11.step(levels)
    total_flashes += flashes
    assert levels == day11.parse_input(str.splitlines("""7818477333
5488477444
5697666949
4608766830
4734946730
4740097688
6900007564
0000009666
8000004755
6800007755"""))
    # Step 9
    levels, flashes = day11.step(levels)
    total_flashes += flashes
    assert levels == day11.parse_input(str.splitlines("""9060000644
7800000976
6900000080
5840000082
5858000093
6962400000
8021250009
2221130009
9111128097
7911119976"""))
    # Step 10
    levels, flashes = day11.step(levels)
    total_flashes += flashes
    assert levels == day11.parse_input(str.splitlines("""0481112976
0031112009
0041112504
0081111406
0099111306
0093511233
0442361130
5532252350
0532250600
0032240000"""))
    assert total_flashes == 204

    for i in range(10):
        levels, flashes = day11.step(levels)
        total_flashes += flashes
    # After step 20
    assert levels == day11.parse_input(str.splitlines("""3936556452
5686556806
4496555690
4448655580
4456865570
5680086577
7000009896
0000000344
6000000364
4600009543"""))

    for i in range(10):
        levels, flashes = day11.step(levels)
        total_flashes += flashes
    # After step 30
    assert levels == day11.parse_input(str.splitlines("""0643334118
4253334611
3374333458
2225333337
2229333338
2276733333
2754574565
5544458511
9444447111
7944446119"""))

    for i in range(10):
        levels, flashes = day11.step(levels)
        total_flashes += flashes
    # After step 40
    assert levels == day11.parse_input(str.splitlines("""6211111981
0421111119
0042111115
0003111115
0003111116
0065611111
0532351111
3322234597
2222222976
2222222762"""))


def test_part_2():
    levels = day11.parse_input(str.splitlines("""5483143223
    2745854711
    5264556173
    6141336146
    6357385478
    4167524645
    2176841721
    6882881134
    4846848554
    5283751526"""))
    for i in range(200):
        levels, flashes = day11.step(levels)
        if flashes == 100:
            break
    assert i + 1 == 195
