Creates maps using cellular automata rather than the more popular perlin noise method.

2-5 generations or cellular automata and a land percentage between 40-60% tend to create the best looking maps.

Note: there is not a singular cellular automata algorithm, the one used in this code turns a cell into land(#) if 5-7 of its neighbours are land.
     the function "cellular_automata" is where you can change the rules.   
```
............#####....##...............#####.......
...........#######..###.##...........######.......
......####.######...###.##.........########.......
.##...####....##...####............###...#####....
.##...####....##...####............##....#####....
.##..#####...##########.....##..........#######...
....#####.....########.....###..........#.#####...
...#######........####.....##.##.........####.....
..####...##.......#####.......##.......######.....
.#####..............####.#............######......
.###...........##....##.##...........#..#..#......
..#............##....##.............#....#..#.....
....##...............###..........##..............
....###.......###....###.........###..............
.....##.......####....###.........#...............
.##.........######................................
.###....##.####.##..........##....................
.##.....###.##............######.#................
...#....###...............####.##.................
.........#.................##.....................
```
