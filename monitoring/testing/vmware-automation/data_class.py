class Group:
	dev __init__(self, name, begin_year, end_year)
		self.name		= name
		self.begin_year	= begin_year
		self.end_year 	= end_year

############
#
##### mysql create table query

CREATE TABLE groups (
	id			serial primary key,
	name		character varying,
	begin_year	smallint,
	end_year	smallint
)
##############

insert into groups(name, begin_year, end_year)
values("Metallica", 1981, null);

select * from groups where name = 'Metallica';

##### 
# same doing in Python
metallica = Group("Metallica", 1981, None)
metallica.name

DROP table groups;

### sanitirize your sql queries
# case of name -=- DROP table students;
name = "Robert'); DROP TABLE students;--"
select * from students where ( name = '{}' );*.format(name)

