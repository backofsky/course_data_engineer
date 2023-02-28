CREATE TABLE web (
    id integer,
    timestamp bigint,
    type varchar(20),
    page_id integer,
    tag varchar(20),
    sign boolean
);

CREATE TABLE lk (
    id integer,
    user_id integer,
    fio varchar(255),
    dbd date,
    dpa timestamp
);

INSERT INTO web
VALUES     (1, 1637627426, 'visit', 101, 'Sport', True),
           (1, 1637621667, 'scroll', 101, 'Sport', True),
           (1, 1637621620, 'click', 101, 'Sport', True),
           (1, 1637621762, 'visit', 102, 'Politics', True),
           (1, 1637628565, 'click', 102, 'Politics', True),
           (1, 1637625861, 'visit', 103, 'Sport', True),
           (2, 1637628001, 'visit', 104, 'Politics', True),
           (2, 1637628201, 'scrol', 104, 'Politics', True),
           (2, 1637628151, 'click', 104, 'Politics', True),
           (2, 1638628200, 'visit', 105, 'Business', True),
           (2, 1638628226, 'click', 105, 'Business', True),
           (2, 1637628317, 'visit', 106, 'Business', True),
           (2, 1637628359, 'scrol', 106, 'Business', True),
           (3, 1637628422, 'visit', 101, 'Sport', False),
           (3, 1637828486, 'scroll', 101, 'Sport', False),
           (4, 1637628505, 'visit', 106, 'Business', False),
           (5, 1637628511, 'visit', 101, 'Sport', True),
           (5, 1637628901, 'click', 101, 'Sport', True),
           (4, 1637628926, 'visit', 102, 'Politics', False),
           (5, 1637628976, 'click', 102, 'Politics', True),
           (4, 1637999111, 'click', 101, 'Politics', False),
           (4, 1638888999, 'click', 102, 'Politics', False)


INSERT INTO lk
VALUES
    (101,1,'Никифоров Август Арестович','2000-05-05','2021-10-29'),
    (102,2,'Кудимов Алексей Алексеевич','1998-07-13','2021-11-22'),
    (105,5,'Музин Владимир Владимирович','1995-02-10','2021-11-23')