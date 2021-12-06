# How many passengers survived, and how many died?
SURVIVED = '''
            SELECT count(survived) FROM titanic_method_one
            WHERE survived = 1
            '''
NOT_SURVIVE = '''
                SELECT count(survived) FROM titanic_method_one
                WHERE survived = 0
                '''
# How many passengers were in each class?

PCLASS_ONE = '''
                SELECT COUNT(pclass) FROM titanic_method_one
                WHERE pclass = 1
             '''
PCLASS_TWO = '''
                SELECT COUNT(pclass) FROM titanic_method_one
                WHERE pclass = 2
             '''
PCLASS_THREE = '''
                SELECT COUNT(pclass) FROM titanic_method_one
                WHERE pclass = 3
             '''

# How many passengers survived/died within each class?
PCLASS_ONE_SURV = '''
                    SELECT COUNT(*) FROM titanic_method_one
                    WHERE pclass = 1 and survived = 1
                    '''

PCLASS_TWO_SURV = '''
                    SELECT COUNT(*) FROM titanic_method_one
                    WHERE pclass = 2 and survived = 1
                    '''

PCLASS_THREE_SURV = '''
                    SELECT COUNT(*) FROM titanic_method_one
                    WHERE pclass = 3 and survived = 1
                    '''


PCLASS_ONE_DIED = '''
                    SELECT COUNT(*) FROM titanic_method_one
                    WHERE pclass = 1 and survived = 0
                  '''

PCLASS_TWO_DIED = '''
                    SELECT COUNT(*) FROM titanic_method_one
                    WHERE pclass = 2 and survived = 0
                  '''

PCLASS_THREE_DIED = '''
                    SELECT COUNT(*) FROM titanic_method_one
                    WHERE pclass = 3 and survived = 0
                  '''
# What was the average age of survivors vs nonsurvivors?
AVERAGE_AGE_DIED = '''
                    SELECT AVG(age) FROM titanic_method_one
                    WHERE survived = 0
                    '''
AVERAGE_AGE_SURV = '''
                    SELECT AVG(age) FROM titanic_method_one
                    WHERE survived = 1
                    '''
# What was the average age of each passenger class?
PCLASS_ONE_AVG_AGE = '''
                    SELECT AVG(age) FROM titanic_method_one
                    WHERE pclass = 1
                '''
PCLASS_TWO_AVG_AGE = '''
                    SELECT AVG(age) FROM titanic_method_one
                    WHERE pclass = 2
                '''
PCLASS_THREE_AVG_AGE = '''
                    SELECT AVG(age) FROM titanic_method_one
                    WHERE pclass = 3
                '''
# What was the average fare by passenger class? By survival?
PCLASS_ONE_AVG_FARE = '''SELECT AVG(fare) FROM titanic_method_one
                         WHERE pclass = 1'''

PCLASS_TWO_AVG_FARE = '''SELECT AVG(fare) FROM titanic_method_one
                         WHERE pclass = 2'''

PCLASS_THREE_AVG_FARE = '''SELECT AVG(fare) FROM titanic_method_one
                         WHERE pclass = 3'''

PCLASS_AVG_FARE_SURV = '''
                        SELECT AVG(fare) FROM titanic_method_one
                        WHERE survived = 1
                        '''
PCLASS_AVG_FARE_DIED = '''
                        SELECT AVG(fare) FROM titanic_method_one
                        WHERE survived = 1
                        '''
# How many siblings/spouses aboard on average, by passenger class? By survival?
PCLASS_ONE_SIB_SPOUS_AVG = '''
                            SELECT AVG(siblings_spouses_aboard) FROM titanic_method_one
                            WHERE pclass = 1
                            '''

PCLASS_TWO_SIB_SPOUS_AVG = '''
                            SELECT AVG(siblings_spouses_aboard) FROM titanic_method_one
                            WHERE pclass = 2
                            '''

PCLASS_THREE_SIB_SPOUS_AVG = '''
                            SELECT AVG(siblings_spouses_aboard) FROM titanic_method_one
                            WHERE pclass = 3
                            '''

AVG_ONE_SIB_SPOUS_SURV = '''
                            SELECT AVG(siblings_spouses_aboard) FROM titanic_method_one
                            WHERE survived = 1
                            '''

AVG_THREE_SIB_SPOUS_DIED = '''
                            SELECT AVG(siblings_spouses_aboard) FROM titanic_method_one
                            WHERE survived = 0
                            '''
# How many parents/children aboard on average, by passenger class? By survival?

PCLASS_ONE_SIB_SPOUS_AVG = '''
                            SELECT AVG(parents_children_aboard) FROM titanic_method_one
                            WHERE pclass = 1
                            '''

PCLASS_TWO_SIB_SPOUS_AVG = '''
                            SELECT AVG(parents_children_aboard) FROM titanic_method_one
                            WHERE pclass = 2
                            '''

PCLASS_THREE_SIB_SPOUS_AVG = '''
                            SELECT AVG(parents_children_aboard) FROM titanic_method_one
                            WHERE pclass = 3
                            '''

AVG_SIB_SPOUS_SURV = '''
                            SELECT AVG(parents_children_aboard) FROM titanic_method_one
                            WHERE survived = 1
                            '''

AVG_SIB_SPOUS_DIED = '''
                            SELECT AVG(parents_children_aboard) FROM titanic_method_one
                            WHERE survived = 0
                            '''
# Do any passengers have the same name?
NAME_COUNT = '''SELECT COUNT(name) FROM titanic_method_one'''

DISTINCT_NAME_COUNT = '''SELECT COUNT(DISTINCT name) FROM titanic_method_one'''
