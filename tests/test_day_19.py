import numpy as np

import day_19.main as day19


def test_apply_rotations():
    scanners = day19.parse_input(str.splitlines("""--- scanner 0 ---
-1,-1,1
-2,-2,2
-3,-3,3
-2,-3,1
5,6,-4
8,0,7

--- scanner 0 ---
1,-1,1
2,-2,2
3,-3,3
2,-1,3
-5,4,-6
-8,-7,0

--- scanner 0 ---
-1,-1,-1
-2,-2,-2
-3,-3,-3
-1,-3,-2
4,6,5
-7,0,8

--- scanner 0 ---
1,1,-1
2,2,-2
3,3,-3
1,3,-2
-4,-6,5
7,0,8

--- scanner 0 ---
1,1,1
2,2,2
3,3,3
3,1,2
-6,-4,-5
0,7,-8"""))
    scanner = scanners.pop(-1)
    beacons = [tuple([x for x in beacon]) for beacon in scanner.beacons]

    rotations = [
        [[0, 0, -1],
         [-1, 0, 0],
         [0, 1, 0]],
        [[0, 0, 1],
         [0, -1, 0],
         [1, 0, 0]],
        [[0, -1, 0],
         [-1, 0, 0],
         [0, 0, -1]],
        [[0, 1, 0],
         [1, 0, 0],
         [0, 0, -1]]
    ]

    for i, (scanner, rotation) in enumerate(zip(scanners, rotations)):
        for relative_position, absolute_position in zip(scanner.beacons, beacons):
            assert day19.to_absolute_position(rotation, relative_position, np.zeros(3)) == absolute_position
            assert day19.to_relative_position(rotation, absolute_position, np.zeros(3)) == relative_position


def test_valid_rotations():
    x, y, z = 1, 2, 3
    ground_truth = [
        # x is facing x
        [x, y, z],
        [x, -z, y],
        [x, -y, -z],
        [x, z, -y],
        # x is facing -x
        [-x, -y, z],
        [-x, -z, -y],
        [-x, y, -z],
        [-x, z, y],
        # x is facing y
        [-z, x, -y],
        [y, x, -z],
        [z, x, y],
        [-y, x, z],
        # x is facing -y
        [z, -x, -y],
        [y, -x, z],
        [-z, -x, y],
        [-y, -x, -z],
        # x is facing z
        [-y, -z, x],
        [z, -y, x],
        [y, z, x],
        [-z, y, x],
        # x is facing -z
        [z, y, -x],
        [-y, z, -x],
        [-z, -y, -x],
        [y, -z, -x]
    ]
    ground_truth = {tuple(rotation) for rotation in ground_truth}

    one_one_one = np.array([x, y, z])
    rotation_matrices = day19.generate_rotation_matrices()

    rotations = set()
    for R, expected in zip(rotation_matrices, ground_truth):
        rotations.add(tuple(R @ one_one_one))
    assert len(rotations) == 24
    assert np.all(rotations == ground_truth)


def test_match():
    scanners = day19.parse_input(str.splitlines("""--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14"""))

    # Use scanner 0 as reference
    scanner_0 = scanners[0]
    # i.e. scanner 0 is at (0, 0, 0), not translated, and not rotated
    known_beacons = {tuple([x for x in beacon]) for beacon in scanner_0.beacons}

    scanner_1 = scanners[1]
    matched, known_beacons = scanner_1.match(known_beacons)
    assert matched is True
    assert tuple(scanner_1.position) == (68, -1246, -43)

    scanner_4 = scanners[4]
    matched, known_beacons = scanner_4.match(known_beacons)
    assert matched is True
    assert tuple(scanner_4.position) == (-20, -1133, 1061)

    scanner_2 = scanners[2]
    matched, known_beacons = scanner_2.match(known_beacons)
    assert matched is True
    assert tuple(scanner_2.position) == (1105, -1205, 1229)

    scanner_3 = scanners[3]
    matched, known_beacons = scanner_3.match(known_beacons)
    assert matched is True
    assert tuple(scanner_3.position) == (-92, -2380, -20)

    assert len(known_beacons) == 79


def test_part_one():
    scanners = day19.parse_input(str.splitlines("""--- scanner 0 ---
    404,-588,-901
    528,-643,409
    -838,591,734
    390,-675,-793
    -537,-823,-458
    -485,-357,347
    -345,-311,381
    -661,-816,-575
    -876,649,763
    -618,-824,-621
    553,345,-567
    474,580,667
    -447,-329,318
    -584,868,-557
    544,-627,-890
    564,392,-477
    455,729,728
    -892,524,684
    -689,845,-530
    423,-701,434
    7,-33,-71
    630,319,-379
    443,580,662
    -789,900,-551
    459,-707,401

    --- scanner 1 ---
    686,422,578
    605,423,415
    515,917,-361
    -336,658,858
    95,138,22
    -476,619,847
    -340,-569,-846
    567,-361,727
    -460,603,-452
    669,-402,600
    729,430,532
    -500,-761,534
    -322,571,750
    -466,-666,-811
    -429,-592,574
    -355,545,-477
    703,-491,-529
    -328,-685,520
    413,935,-424
    -391,539,-444
    586,-435,557
    -364,-763,-893
    807,-499,-711
    755,-354,-619
    553,889,-390

    --- scanner 2 ---
    649,640,665
    682,-795,504
    -784,533,-524
    -644,584,-595
    -588,-843,648
    -30,6,44
    -674,560,763
    500,723,-460
    609,671,-379
    -555,-800,653
    -675,-892,-343
    697,-426,-610
    578,704,681
    493,664,-388
    -671,-858,530
    -667,343,800
    571,-461,-707
    -138,-166,112
    -889,563,-600
    646,-828,498
    640,759,510
    -630,509,768
    -681,-892,-333
    673,-379,-804
    -742,-814,-386
    577,-820,562

    --- scanner 3 ---
    -589,542,597
    605,-692,669
    -500,565,-823
    -660,373,557
    -458,-679,-417
    -488,449,543
    -626,468,-788
    338,-750,-386
    528,-832,-391
    562,-778,733
    -938,-730,414
    543,643,-506
    -524,371,-870
    407,773,750
    -104,29,83
    378,-903,-323
    -778,-728,485
    426,699,580
    -438,-605,-362
    -469,-447,-387
    509,732,623
    647,635,-688
    -868,-804,481
    614,-800,639
    595,780,-596

    --- scanner 4 ---
    727,592,562
    -293,-554,779
    441,611,-461
    -714,465,-776
    -743,427,-804
    -660,-479,-426
    832,-632,460
    927,-485,-438
    408,393,-506
    466,436,-512
    110,16,151
    -258,-428,682
    -393,719,612
    -211,-452,876
    808,-476,-593
    -575,615,604
    -485,667,467
    -680,325,-822
    -627,-443,-432
    872,-547,-609
    833,512,582
    807,604,487
    839,-516,451
    891,-625,532
    -652,-548,-490
    30,-46,-14"""))

    answer = day19.part_one(scanners)
    assert answer == 79