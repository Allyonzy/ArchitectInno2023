create table if not exists college
(
    id bigint primary key ,
    name varchar not null ,
    size integer not null  default 100
);

insert into college(id, name, size) values (10, 'КФУ',50000);
insert into college(id, name, size) values (20, 'МГУ',38000);
insert into college(id, name, size) values (30, 'МФТИ',7000);
insert into college(id, name, size) values (40, 'Иннополис',1077);
insert into college(id, name, size) values (50, 'Сколково',1070);

drop table if exists student;

create table student
(
    id bigint primary key ,
    city varchar not null ,
    name varchar not null ,
    telegram_contact varchar not null,
    college_id bigint not null,
    constraint fk_college_id foreign key (college_id) references college(id)
);

insert into student(id, city, name, telegram_contact, college_id) values (10, 'Казань','Иван Иванов','@ivanov1991',10);
insert into student(id, city, name, telegram_contact, college_id) values (20, 'Москва','Екатерина Андреева','@kate_',20);
insert into student(id, city, name, telegram_contact, college_id) values (30, 'Новосибирск','Анна Потапова','@apotap',30);
insert into student(id, city, name, telegram_contact, college_id) values (40, 'Казань','Ильяс Мухаметшин','@ilyas',40);
insert into student(id, city, name, telegram_contact, college_id) values (50, 'Москва','Сергей Петров','@spetrov',50);

create table course
(
    id bigint primary key ,
    name varchar not null,
    is_online boolean not null  DEFAULT false,
    amount_of_students integer check ( amount_of_students >= 1 ),
    college_id bigint NOT NULL,

    constraint fk_course_college_id foreign key (college_id) references college(id)
);

insert into course(id, name, is_online, amount_of_students, college_id) values (10,'Введение в РСУБД', true, 300 , 10);
insert into course(id, name, is_online, amount_of_students, college_id) values (20,'Data Mining', true, 10 , 20);
insert into course(id, name, is_online, amount_of_students, college_id) values (30,'Нейронные сети', true, 25 , 30);
insert into course(id, name, is_online, amount_of_students, college_id) values (40,'Цифровая трансформация', true, 50 , 40);
insert into course(id, name, is_online, amount_of_students, college_id) values (50,'Актерское мастерство', false, 15 , 50);


create table student_on_course
(
    id bigint primary key ,
    student_id bigint not null ,
    course_id bigint not null ,
    student_rating integer not null DEFAULT 50 check ( student_rating BETWEEN 0 and 100 ),
    finished_date date,
    constraint fk_student_id foreign key (student_id) references student(id),
    constraint fk_course_id foreign key (course_id) references course(id)
);

insert into student_on_course(id, student_id, course_id, student_rating, finished_date) VALUES (10,10,10,75, null);
insert into student_on_course(id, student_id, course_id, student_rating, finished_date) VALUES (20,10,20,83, null);
insert into student_on_course(id, student_id, course_id, student_rating, finished_date) VALUES (30,10,40,40, null);

insert into student_on_course(id, student_id, course_id, student_rating, finished_date) VALUES (40,20,50,95, '2022-12-12');

insert into student_on_course(id, student_id, course_id, student_rating, finished_date) VALUES (50,30,30,76, '2022-12-12');
insert into student_on_course(id, student_id, course_id, student_rating, finished_date) VALUES (60,30,40,42, null);

insert into student_on_course(id, student_id, course_id, student_rating, finished_date) VALUES (70,40,10,76, null);
insert into student_on_course(id, student_id, course_id, student_rating, finished_date) VALUES (80,40,20,83, null);
insert into student_on_course(id, student_id, course_id, student_rating, finished_date) VALUES (90,40,50,96, null);

insert into student_on_course(id, student_id, course_id, student_rating, finished_date) VALUES (100,50,10,12, null);
insert into student_on_course(id, student_id, course_id, student_rating, finished_date) VALUES (110,50,20,21, null);
insert into student_on_course(id, student_id, course_id, student_rating, finished_date) VALUES (120,50,30,56, null);
insert into student_on_course(id, student_id, course_id, student_rating, finished_date) VALUES (130,50,40,92, null);
