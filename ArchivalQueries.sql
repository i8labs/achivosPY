delete from Test  where TEST_ID NOT IN (SELECT DISTINCT TEST_ID FROM Transaction where TEST_ID IS NOT NULL);
delete from Test_Content  where TEST_ID NOT IN (SELECT DISTINCT TEST_ID FROM Transaction where TEST_ID IS NOT NULL);

