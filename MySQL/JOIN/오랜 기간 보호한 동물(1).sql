# https://school.programmers.co.kr/learn/courses/30/lessons/59044
SELECT I.NAME, I.DATETIME from ANIMAL_INS I
left join ANIMAL_OUTS O
on I.ANIMAL_ID = O.ANIMAL_ID
where O.ANIMAL_ID is null
order by I.DATETIME
limit 3
