setup = '''
CREATE EXTENSION IF NOT EXISTS pgrowlocks;
DROP TABLE IF EXISTS my_table;
CREATE TABLE my_table(id int, v text);
INSERT INTO my_table VALUES (1, 'a'), (2, 'b');
'''

with get_cursor(application_name='block_or_not_setup') as cur_setup:
    cur_setup.execute(setup)