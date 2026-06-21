-- Not Boring Movies

/* Write your PL/SQL query statement below */
SELECT *
FROM CINEMA
WHERE MOD(id,2)=1 
AND ID NOT IN (SELECT ID FROM CINEMA WHERE DESCRIPTION ='boring')
ORDER BY RATING DESC;