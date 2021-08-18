/* Welcome to the SQL mini project. You will carry out this project partly in
the PHPMyAdmin interface, and partly in Jupyter via a Python connection.

This is Tier 1 of the case study, which means that there'll be more guidance for you about how to 
setup your local SQLite connection in PART 2 of the case study. 

The questions in the case study are exactly the same as with Tier 2. 

PART 1: PHPMyAdmin
You will complete questions 1-9 below in the PHPMyAdmin interface. 
Log in by pasting the following URL into your browser, and
using the following Username and Password:

URL: https://sql.springboard.com/
Username: student
Password: learn_sql@springboard

The data you need is in the "country_club" database. This database
contains 3 tables:
    i) the "Bookings" table,
    ii) the "Facilities" table, and
    iii) the "Members" table.

In this case study, you'll be asked a series of questions. You can
solve them using the platform, but for the final deliverable,
paste the code for each solution into this script, and upload it
to your GitHub.

Before starting with the questions, feel free to take your time,
exploring the data, and getting acquainted with the 3 tables. */


/* QUESTIONS 
/* Q1: Some of the facilities charge a fee to members, but some do not.
Write a SQL query to produce a list of the names of the facilities that do. */
SELECT name
FROM Facilities 
WHERE membercost > 0;

Answers:
name
Tennis Court 1
Tennis Court 2
Massage Room 1
Massage Room 2
Squash Court

/* Q2: How many facilities do not charge a fee to members? */
SELECT COUNT(*)
FROM Facilities
WHERE membercost = 0;

Answer:
4

/* Q3: Write an SQL query to show a list of facilities that charge a fee to members,
where the fee is less than 20% of the facility's monthly maintenance cost.
Return the facid, facility name, member cost, and monthly maintenance of the
facilities in question. */
SELECT facid, name, membercost, monthlymaintenance
FROM Facilities
WHERE membercost > 0 
	AND membercost < 0.2 * monthlymaintenance;
	
Answers:
facid	name	membercost	monthlymaintenance	
0	Tennis Court 1	5.0	200
1	Tennis Court 2	5.0	200
4	Massage Room 1	9.9	3000
5	Massage Room 2	9.9	3000
6	Squash Court	3.5	80

/* Q4: Write an SQL query to retrieve the details of facilities with ID 1 and 5.
Try writing the query without using the OR operator. */
SELECT *
FROM Facilities
WHERE facid IN (1, 5);

Answers:
monthlymaintenance	facid	name	membercost	guestcost	initialoutlay	
200	1	Tennis Court 2	5.0	25.0	8000
3000	5	Massage Room 2	9.9	80.0	4000

/* Q5: Produce a list of facilities, with each labelled as
'cheap' or 'expensive', depending on if their monthly maintenance cost is
more than $100. Return the name and monthly maintenance of the facilities
in question. */
SELECT 
	name,
	monthlymaintenance,
	CASE WHEN monthlymaintenance > 100 THEN 'expensive'
	ELSE 'cheap' END AS maintenance_value
FROM Facilities;

Answers:
name	monthlymaintenance	maintenance_value	
Tennis Court 1	200	expensive
Tennis Court 2	200	expensive
Badminton Court	50	cheap
Table Tennis	10	cheap
Massage Room 1	3000	expensive
Massage Room 2	3000	expensive
Squash Court	80	cheap
Snooker Table	15	cheap
Pool Table	15	cheap

/* Q6: You'd like to get the first and last name of the last member(s)
who signed up. Try not to use the LIMIT clause for your solution. */
SELECT firstname, surname
	FROM Members
	WHERE joindate = (SELECT MAX(joindate) FROM Members);

Answer:
firstname	surname	
Darren	Smith

/* Q7: Produce a list of all members who have used a tennis court.
Include in your output the name of the court, and the name of the member
formatted as a single column. Ensure no duplicate data, and order by
the member name. */
SELECT DISTINCT t.name, member_name AS Member_Name
FROM Bookings AS b
	JOIN (SELECT memid, CONCAT(surname, ',', firstname) AS member_name FROM Members) AS m
	ON b.memid = m.memid
	JOIN (SELECT name, facid FROM Facilities) AS t
	ON b.facid = t.facid
WHERE b.facid IN (SELECT facid FROM Facilities WHERE name LIKE 'Tennis Court%')
ORDER BY member_name;

Answers:
name	Member_Name	
Tennis Court 2	Bader,Florence
Tennis Court 1	Bader,Florence
Tennis Court 1	Baker,Anne
Tennis Court 2	Baker,Anne
Tennis Court 2	Baker,Timothy
Tennis Court 1	Baker,Timothy
Tennis Court 1	Boothe,Tim
Tennis Court 2	Boothe,Tim
Tennis Court 1	Butters,Gerald
Tennis Court 2	Butters,Gerald
Tennis Court 1	Coplin,Joan
Tennis Court 1	Crumpet,Erica
Tennis Court 2	Dare,Nancy
Tennis Court 1	Dare,Nancy
Tennis Court 1	Farrell,David
Tennis Court 2	Farrell,David
Tennis Court 1	Farrell,Jemima
Tennis Court 2	Farrell,Jemima
Tennis Court 1	Genting,Matthew
Tennis Court 2	GUEST,GUEST
Tennis Court 1	GUEST,GUEST
Tennis Court 1	Hunt,John
Tennis Court 2	Hunt,John
Tennis Court 1	Jones,David
Tennis Court 2	Jones,David
Tennis Court 1	Jones,Douglas
Tennis Court 1	Joplette,Janice
Tennis Court 2	Joplette,Janice
Tennis Court 1	Owen,Charles
Tennis Court 2	Owen,Charles

/* Q8: Produce a list of bookings on the day of 2012-09-14 which
will cost the member (or guest) more than $30. Remember that guests have
different costs to members (the listed costs are per half-hour 'slot'), and
the guest user's ID is always 0. Include in your output the name of the
facility, the name of the member formatted as a single column, and the cost.
Order by descending cost, and do not use any subqueries. */
SELECT name as facility_name, CONCAT(surname, ",", firstname) AS member_name, guestcost
	FROM Bookings AS b
	JOIN Facilities AS f
		ON b.facid = f.facid
	JOIN Members AS m
		ON b.memid = m.memid
	WHERE b.starttime LIKE "2012-09-14%"
		AND guestcost > 30
	ORDER BY guestcost DESC;

Answers:
facility_name	member_name	guestcost	
Massage Room 2	GUEST,GUEST	80.0
Massage Room 1	GUEST,GUEST	80.0
Massage Room 1	Stibbons,Ponder	80.0
Massage Room 1	Farrell,Jemima	80.0
Massage Room 1	Tracy,Burton	80.0
Massage Room 2	Bader,Florence	80.0
Massage Room 1	Smith,Jack	80.0
Massage Room 1	Farrell,Jemima	80.0
Massage Room 1	GUEST,GUEST	80.0
Massage Room 1	GUEST,GUEST	80.0
Massage Room 1	Genting,Matthew	80.0

/* Q9: This time, produce the same result as in Q8, but using a subquery. */
SELECT name as facility_name, member_name, guestcost
	FROM Bookings AS b
	JOIN (SELECT facid, name, guestcost FROM Facilities WHERE guestcost > 30) AS f
		ON b.facid = f.facid
	JOIN (SELECT memid, CONCAT(surname, ",", firstname) AS member_name FROM Members) AS m
			ON b.memid = m.memid
	WHERE b.starttime LIKE "2012-09-14%"
	ORDER BY guestcost DESC;

Answer:
facility_name	member_name	guestcost	
Massage Room 1	GUEST,GUEST	80.0
Massage Room 1	Stibbons,Ponder	80.0
Massage Room 1	Farrell,Jemima	80.0
Massage Room 1	Tracy,Burton	80.0
Massage Room 2	Bader,Florence	80.0
Massage Room 1	Smith,Jack	80.0
Massage Room 1	Farrell,Jemima	80.0
Massage Room 1	GUEST,GUEST	80.0
Massage Room 1	GUEST,GUEST	80.0
Massage Room 1	Genting,Matthew	80.0
Massage Room 2	GUEST,GUEST	80.0

/* PART 2: SQLite
/* We now want you to jump over to a local instance of the database on your machine. 

Copy and paste the LocalSQLConnection.py script into an empty Jupyter notebook, and run it. 

Make sure that the SQLFiles folder containing thes files is in your working directory, and
that you haven't changed the name of the .db file from 'sqlite\db\pythonsqlite'.

You should see the output from the initial query 'SELECT * FROM FACILITIES'.

Complete the remaining tasks in the Jupyter interface. If you struggle, feel free to go back
to the PHPMyAdmin interface as and when you need to. 

You'll need to paste your query into value of the 'query1' variable and run the code block again to get an output.
 
QUESTIONS:
/* Q10: Produce a list of facilities with a total revenue less than 1000.
The output of facility name and total revenue, sorted by revenue. Remember
that there's a different cost for guests and members! */
SELECT *
FROM
(
SELECT 
    f.name,
    SUM(CASE WHEN b.memid !=0 THEN (f.membercost * b.slots) 
        ELSE (f.guestcost * b.slots) END) AS total_revenue
FROM Facilities AS f
LEFT JOIN Bookings AS b ON f.facid = b.facid
GROUP BY f.name
) AS subquery
WHERE total_revenue < 1000
ORDER BY total_revenue;

Answers:
name	total_revenue
0	Table Tennis	180
1	Snooker Table	240
2	Pool Table	270

/* Q11: Produce a report of members and who recommended them in alphabetic surname,firstname order */
SELECT m1.firstname || ' ' || m1.surname AS member_name, m2.firstname || ' ' || m2.surname AS recommender_name
           FROM members AS m1
           JOIN members AS m2
           	ON m1.recommendedby = m2.memid
           WHERE m1.recommendedby = m2.memid
           ORDER BY m1.surname, m1.firstname;

Answers:
	member_name	recommender_name
0	Florence Bader	Ponder Stibbons
1	Anne Baker	Ponder Stibbons
2	Timothy Baker	Jemima Farrell
3	Tim Boothe	Tim Rownam
4	Gerald Butters	Darren Smith

/* Q12: Find the facilities with their usage by member, but not guests */
SELECT f.name, b.memid, m.firstname || ' ' || m.surname AS member_name, COUNT(b.memid) AS COUNT_member_usage
            FROM Bookings AS b
            JOIN Facilities AS f
                ON b.facid = f.facid
            JOIN Members AS m
                ON b.memid = m.memid
            WHERE b.memid != 0
            GROUP BY b.facid, b.memid;

Answers:
name	memid	member_name	COUNT_member_usage
0	Tennis Court 1	2	Tracy Smith	30
1	Tennis Court 1	3	Tim Rownam	6
2	Tennis Court 1	4	Janice Joplette	19
3	Tennis Court 1	5	Gerald Butters	57
4	Tennis Court 1	6	Burton Tracy	31

/* Q13: Find the facilities usage by month, but not guests */
SELECT f.name AS facility_name, strftime('%m', starttime) AS month, COUNT(b.memid) AS COUNT_usage
            FROM Bookings AS b
            JOIN Facilities AS f
                ON b.facid = f.facid
            JOIN Members AS m
                ON b.memid = m.memid
            WHERE b.memid != 0
            GROUP BY b.facid, month;

Answers:
facility_name	month	COUNT_usage
0	Tennis Court 1	07	65
1	Tennis Court 1	08	111
2	Tennis Court 1	09	132
3	Tennis Court 2	07	41
4	Tennis Court 2	08	109
